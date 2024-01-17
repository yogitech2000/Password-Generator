'''
prerequiresites 
================
1.Python 3x (preinstalled Tkinter module)
2.Pypercip module(copy to clipboard)


'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import choice
import string

def generate_password():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_special_chars = special_chars_var.get()
    use_numbers = numbers_var.get()

    characters = ""
    if use_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #string.ascii_uppercase
    if use_lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz" #string.ascii_lowercase
    if use_special_chars:
        characters += "@$" #string.punctuation
    if use_numbers:
        characters += string.digits

    if not characters:
        messagebox.showinfo("Error", "Please select at least one option.")
        return

    password = ''.join(choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def reset_password():
    length_var.set(8)
    uppercase_var.set(True)
    lowercase_var.set(True)
    special_chars_var.set(True)
    numbers_var.set(True)
    password_var.set("")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Variables
length_var = tk.IntVar(value=8)
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Widgets
length_label = ttk.Label(root, text="Password Length:")
length_entry = ttk.Entry(root, textvariable=length_var, width=5)
uppercase_checkbox = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
lowercase_checkbox = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
special_chars_checkbox = ttk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
numbers_checkbox = ttk.Checkbutton(root, text="Numbers", variable=numbers_var)
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
reset_button = ttk.Button(root, text="Reset", command=reset_password)
password_entry = ttk.Entry(root, textvariable=password_var, state="readonly")

# Layout
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")
lowercase_checkbox.grid(row=1, column=1, padx=10, pady=5, sticky="w")
special_chars_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")
numbers_checkbox.grid(row=2, column=1, padx=10, pady=5, sticky="w")
generate_button.grid(row=3, column=0, columnspan=2, pady=10)
copy_button.grid(row=4, column=0, columnspan=2, pady=5)
reset_button.grid(row=5, column=0, columnspan=2, pady=5)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Run the main loop
root.mainloop()

