import cv2
import tkinter as tk
from tkinter import filedialog, messagebox


def decrypt_message():
    file_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.jpg *.png")])
    if not file_path:
        return

    password = entry_password.get()

    if not password:
        messagebox.showerror("Error", "Password cannot be empty!")
        return

    img = cv2.imread(file_path)

    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0

    try:
        for _ in range(255):  # Assuming message length max 255
            char = c[img[n, m, z]]
            if char == '\0':  # Stop at null character
                break
            message += char
            n += 1
            m += 1
            z = (z + 1) % 3
    except KeyError:
        messagebox.showerror("Error", "Failed to retrieve the message. Wrong password or corrupted file!")
        return

    messagebox.showinfo("Decrypted Message", f"Message: {message}")


# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Decrypt")

tk.Label(root, text="Enter Password:").pack()
entry_password = tk.Entry(root, width=50, show="*")
entry_password.pack()

btn_decrypt = tk.Button(root, text="Select Image & Decrypt", command=decrypt_message)
btn_decrypt.pack()

root.mainloop()
