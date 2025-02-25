import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def encrypt_message():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.png")])
    if not file_path:
        return

    msg = entry_message.get()
    password = entry_password.get()

    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    img = cv2.imread(file_path)

    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    output_path = file_path.replace(".", "_encrypted.")
    cv2.imwrite(output_path, img)

    messagebox.showinfo("Success", f"Encrypted image saved at:\n{output_path}")


# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Encrypt")

tk.Label(root, text="Enter Secret Message:").pack()
entry_message = tk.Entry(root, width=50)
entry_message.pack()

tk.Label(root, text="Enter Password:").pack()
entry_password = tk.Entry(root, width=50, show="*")
entry_password.pack()

btn_encrypt = tk.Button(root, text="Select Image & Encrypt", command=encrypt_message)
btn_encrypt.pack()

root.mainloop()
