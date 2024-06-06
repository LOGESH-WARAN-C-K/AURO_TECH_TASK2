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
