# AURO_TECH_TASK2

Sure! Below is a detailed `README.md` file for your QR Code Generator project.

```markdown
# QR Code Generator

This project is a Python script for generating QR codes for provided input data, such as URLs, text, or other information. It allows users to easily encode information into QR codes, which can then be decoded using any standard QR code reader.

## Features

- Generate QR codes from URLs, text, or other information.
- Customize the QR code version, box size, and border size.
- Save the generated QR code as an image file.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- `qrcode` library for generating QR codes.
- `Pillow` library for handling image files.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/qr-code-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd qr-code-generator
    ```
3. Install the required libraries:
    ```bash
    pip install qrcode[pil]
    ```

## Usage

To run the QR Code Generator script:

1. Open a terminal and navigate to the project directory.
2. Execute the script using Python:
    ```bash
    python qr_code_generator.py
    ```
3. Follow the prompts to enter the data, filename, version, box size, and border size.

### Example

Here's an example of how to use the script:

```plaintext
Enter the data (URL or text) to encode in the QR code: https://example.com
Enter the filename to save the QR code (default is 'qrcode.png'): example_qr.png
Enter the version of the QR code (default is 1): 1
Enter the box size of the QR code (default is 10): 10
Enter the border size of the QR code (default is 4): 4
QR code saved as example_qr.png
```

The script will generate a QR code with the specified data and save it as an image file named `example_qr.png`.

## Script Overview

### QRCodeGenerator Class

This class is responsible for creating and saving QR codes.

- **Attributes**:
  - `data`: The input data to encode in the QR code.
  - `filename`: The name of the file to save the QR code image.
  - `version`: The version of the QR code (size of the QR code).
  - `box_size`: The size of each box in the QR code.
  - `border`: The border size of the QR code.

- **Methods**:
  - `generate_qr()`: Generates and saves the QR code as an image file.

### Main Function

The script's main function handles user input and initializes the QRCodeGenerator class with the provided parameters.

```python
import qrcode
from PIL import Image

class QRCodeGenerator:
    def __init__(self, data, filename='qrcode.png', version=1, box_size=10, border=4):
        self.data = data
        self.filename = filename
        self.version = version
        self.box_size = box_size
        self.border = border

    def generate_qr(self):
        # Create QR code instance
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.box_size,
            border=self.border,
        )

        # Add data to the QR code
        qr.add_data(self.data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(self.filename)
        print(f"QR code saved as {self.filename}")

if __name__ == "__main__":
    # Example data to encode
    data = input("Enter the data (URL or text) to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code (default is 'qrcode.png'): ") or 'qrcode.png'
    version = int(input("Enter the version of the QR code (default is 1): ") or 1)
    box_size = int(input("Enter the box size of the QR code (default is 10): ") or 10)
    border = int(input("Enter the border size of the QR code (default is 4): ") or 4)

    qr_generator = QRCodeGenerator(data, filename, version, box_size, border)
    qr_generator.generate_qr()
```

## Customization

You can customize the following parameters when generating the QR code:

- **Data**: The input data to be encoded into the QR code (e.g., URL or text).
- **Filename**: The name of the file to save the QR code image.
- **Version**: The version of the QR code, which determines the size (default is 1).
- **Box Size**: The size of each box in the QR code grid (default is 10).
- **Border**: The thickness of the border around the QR code (default is 4).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses the following libraries:
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)
```

This `README.md` file provides a comprehensive overview of the QR Code Generator project, including installation instructions, usage details, and a script overview. Replace `https://github.com/your-username/qr-code-generator.git` with the actual URL of your GitHub repository.
