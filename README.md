Introduction
Image Steganography is the technique of hiding secret data within an image in such a way that the existence of the data is invisible. This project uses Python to implement a simple and secure image steganography system, with the added feature of password protection for both encryption and decryption processes.

Features
✅ Data Encryption: Hide secret text messages inside image pixels.
✅ Data Decryption: Retrieve hidden messages from encrypted images.
✅ Password Protection: Only users with the correct password can access hidden data.
✅ Graphical User Interface (GUI): A simple, user-friendly interface built with Tkinter.
✅ Separate Encryption & Decryption: Independent scripts for better usability and security.
✅ Automatic Image Saving: The encrypted image is saved with a new filename.
Technologies Used
Python 3.x — Main programming language.
OpenCV (cv2): For image manipulation and pixel data processing.
Tkinter: To create a simple graphical user interface.
OS Module: For file handling and image operations.
How to Run
1. Clone the repository
bash
Copy
Edit
git clone <your-repo-link>
cd ImageSteganography
2. Install dependencies
Ensure you have Python installed, then install required libraries:

bash
Copy
Edit
pip install opencv-python
3. Project Structure
bash
Copy
Edit
/ImageSteganography
│-- encrypt.py               # For hiding secret messages into images
│-- decrypt.py               # For revealing hidden messages from encrypted images
│-- sample_image.jpg         # Test image for encryption
│-- encrypted_image.jpg      # Output image after encryption
│-- README.md                # Project documentation
4. Run the programs
To encrypt a message into an image:

bash
Copy
Edit
python encrypt.py
Steps:

Enter your secret message.
Provide a password.
Select the image to hide the message.
The encrypted image will be saved as sample_image_encrypted.jpg.
To decrypt the hidden message:

bash
Copy
Edit
python decrypt.py
Steps:

Enter the password used during encryption.
Select the encrypted image.
The hidden message will be displayed.

Future Scope
🔒 Advanced Encryption: Integrate AES or RSA algorithms alongside steganography.
📱 Cross-Platform App: Build a mobile or web app for secure, encrypted image sharing.
🖼️ Multiple File Formats: Expand support to BMP, TIFF, and GIF formats.
🚀 Batch Processing: Allow users to encrypt/decrypt multiple images at once.
🕵️ Anti-Detection Algorithms: Implement noise reduction and steganalysis-resistance methods.
Contributors
Manasadevi J— Blockchain Developer and Python Programmer.
