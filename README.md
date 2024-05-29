# QR Code Generator

### Features:
- Generate QR Codes: Easily generate QR codes for any URL.
- The generated QR code is saved as an image file (`qrimg.png`).

### Installation and Run Instructions:
- Clone the repo and run it in any IDE which supports Python.
- Type the URL you want to convert into a QR code and press Enter.
- The QR code for the entered URL will be generated and saved as `qrimg.png` in the project directory.

### Interesting Parts during the Build Process:
- It was interesting to learn how QR codes work and how they store data. Understanding the different parts of a QR code, like the error correction level and version, was fascinating. This knowledge helped in setting up the parameters for generating QR codes.
- The `qrcode` library in Python made the process of generating QR codes straightforward. Experimenting with different settings, like changing the box size and error correction level, was fun and educational. It was amazing to see how a few lines of code could create a functional QR code generator.

### Difficulties Faced and Solutions:
Ensuring the generated QR code image was of high quality was a challenge. By adjusting the `box_size` and `border` parameters, I was able to create a clear and readable QR code. Testing with different sizes and ensuring the QR code scanned correctly helped in fine-tuning these settings.

### Screenshots:
<img src="https://github.com/shubhhh19/Password-Generator/assets/126296317/789897df-469d-4abd-b488-d4fd5abe97b0" width="800" height="400">
