from PIL import Image
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, CircleModuleDrawer, GappedSquareModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def generate_qr_with_logo(data, logo_path, output_path, qr_color=(0, 0, 0), background_color=None, module_style='rounded'):
    
    if module_style == 'square':
        module_drawer = SquareModuleDrawer()
    elif module_style == 'circle':
        module_drawer = CircleModuleDrawer()
    elif module_style == 'gapped_square':
        module_drawer = GappedSquareModuleDrawer()
    else:
        module_drawer = RoundedModuleDrawer()  

    # Generate QR Code
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Customize the QR Code (Color and Style)
    if background_color:
        qr_img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=module_drawer,
            color_mask=RadialGradiantColorMask(back_color=background_color, center_color=qr_color, edge_color=qr_color)
        ).convert('RGB')
    else:
        qr_img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=module_drawer,
            color_mask=RadialGradiantColorMask(back_color=(255, 255, 255), center_color=qr_color, edge_color=qr_color)
        ).convert('RGBA')
        qr_img = remove_background(qr_img)

    # Add the logo to the QR Code
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Calculate the logo size and position
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 4  # Logo size is 1/4th of the QR code size
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            
            # Calculate position to paste the logo
            logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            qr_img.paste(logo, logo_position, logo)
        except Exception as e:
            print(f"Error: Unable to open logo image. {e}")
            return

    # Save or Display the QR Code
    qr_img.save(output_path)
    qr_img.show()

def remove_background(qr_img):
    # Convert QR image to RGBA (if not already) and make white background transparent
    datas = qr_img.getdata()

    new_data = []
    for item in datas:
        # change all white (also shades of whites)
        # pixels to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    qr_img.putdata(new_data)
    return qr_img

# Collecting input from the user
if __name__ == "__main__":
    data = input("Enter the data or URL to encode in the QR code: ")
    logo_path = input("Enter the path to the logo image (leave empty if no logo): ").strip()
    output_path = input("Enter the output file path for the QR code image (with .png extension for transparency): ")
    
    # Optional: Collect color preferences from the user
    qr_color = tuple(map(int, input("Enter QR code color in RGB format (e.g., 0, 0, 0 for black): ").split(',')))

    use_background = input("Do you want a background color? (yes/no): ").strip().lower()
    
    if use_background == 'yes':
        background_color = tuple(map(int, input("Enter background color in RGB format (e.g., 255, 255, 255 for white): ").split(',')))
    else:
        background_color = None  # No background, make it transparent
    
    # New: Ask the user for the module style
    print("Choose QR code module style: ")
    print("1. Square (default)")
    print("2. Circle")
    print("3. Rounded")
    print("4. Gapped Square")
    style_choice = input("Enter the number of your preferred style: ").strip()

    if style_choice == '2':
        module_style = 'circle'
    elif style_choice == '3':
        module_style = 'rounded'
    elif style_choice == '4':
        module_style = 'gapped_square'
    else:
        module_style = 'square'  # Default

    # Generate the QR code with the provided inputs
    generate_qr_with_logo(data, logo_path, output_path, qr_color, background_color, module_style)
