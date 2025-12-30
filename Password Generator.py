import tkinter as tk
import random
import string
def generate_password():
    length_text = length_entry.get()
    if length_text == "":
        result_label.config(text="Please enter password length")
        return
    if not length_text.isdigit():
        result_label.config(text="Length must be a number")
        return
    length = int(length_text)
    if length <= 0:
        result_label.config(text="Length must be greater than zero")
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    result_label.config(text=password)
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x220")
root.resizable(False, False)
title = tk.Label(root, text="Password Generator", font=("Arial", 16))
title.pack(pady=10)
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)
generate_btn = tk.Button(root, text="Generate", command=generate_password)
generate_btn.pack(pady=10)
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack(pady=10)
root.mainloop()

