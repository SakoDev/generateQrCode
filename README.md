# QR Code Generator with Custom Logo and Styles

This Python script generates a QR code with a customizable design, including the ability to add a logo at the center and choose different QR code module styles. The script also allows for the QR code to have a transparent background behind the logo and to be saved as a PNG file.

## Features

- **Customizable QR Code Colors**: Define the colors of the QR code and background.
- **Logo Embedding**: Place a logo at the center of the QR code.
- **Multiple Module Styles**: Choose from square, circle, rounded, or gapped square modules.
- **Transparent Background Option**: Generate QR codes with a transparent background.

## Requirements

- Python 3.x
- Pillow (PIL)
- qrcode

## Installation

Before running the script, you need to install the required Python libraries:

```bash
pip install qrcode[pil] Pillow
```

## Usage

To run the script, execute the following command:

```bash
python main.py
```

You will be prompted to enter the following details:

1. **Data or URL**: The text or URL you want to encode in the QR code.
2. **Logo Path**: The path to the logo image file (leave empty if no logo is needed).
3. **Output File Path**: The path where the generated QR code image will be saved (with `.png` extension for transparency).
4. **QR Code Color**: The RGB color of the QR code (e.g., `0, 0, 0` for black).
5. **Background Color**: Whether you want a background color or not. If `yes`, specify the RGB value.
6. **Module Style**: Choose the style of the QR code modules:
   - `1` for Square (default)
   - `2` for Circle
   - `3` for Rounded
   - `4` for Gapped Square

### Example

"C:/Program Files/Python312/python.exe" c:/path_to_script/generateQrCode/main.py
Enter the data or URL to encode in the QR code: https://example.com
Enter the path to the logo image (leave empty if no logo): logo.png
Enter the output file path for the QR code image (with .png extension for transparency): qr.png
Enter QR code color in RGB format (e.g., 0, 0, 0 for black): 0,0,0
Do you want a background color? (yes/no): no
Choose QR code module style: 
1. Square (default)
2. Circle
3. Rounded
4. Gapped Square
Enter the number of your preferred style: 4


## Functionality Overview

### `generate_qr_with_logo(data, logo_path, output_path, qr_color, background_color, module_style)`

This function generates a QR code with the specified customizations.

- **Parameters**:
  - `data`: The content to be encoded in the QR code.
  - `logo_path`: Path to the logo image file.
  - `output_path`: The file path where the QR code image will be saved.
  - `qr_color`: RGB color tuple for the QR code.
  - `background_color`: RGB color tuple for the background or `None` for transparency.
  - `module_style`: The style of the QR code modules (`square`, `circle`, `rounded`, or `gapped_square`).

### `remove_background(qr_img)`

This helper function makes the white background of the QR code transparent, which is particularly useful when adding a logo.

## License

This project is licensed under the MIT License.

## Author

SakoDev - [SakoDev](https://github.com/SakoDev)

