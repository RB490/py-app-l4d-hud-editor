"""Show message module. Print & messagebox"""
import os
import subprocess
import sys
from tkinter import messagebox
import tkinter as tk

def open_file_or_directory(file_path):
    """Run specified path. Either opening a file or directory correctly"""
    # Check if file path exists
    if not os.path.exists(file_path):
        print(f"File path {file_path} does not exist.")
        return

    # Check if file path is a file or folder
    if os.path.isdir(file_path):
        # Open the folder in the default file explorer
        subprocess.Popen(["explorer", file_path])
    elif os.path.isfile(file_path):
        # Run the file as a file
        subprocess.run(file_path, shell=True, check=False)
    print(f"Opened {file_path}.")

def show_message(msg, msgbox_type="info"):
    """Show message by prnting it and showing in a messagebox if running as .pyw"""
    # Always print the message
    print(msg)

    # If running in windowed mode (.pyw) and a valid msgbox_type is provided, show the messagebox
    if msgbox_type and os.path.splitext(sys.argv[0])[1].lower() == ".pyw":
        valid_msgbox_types = {
            "info": messagebox.showinfo,
            "warning": messagebox.showwarning,
            "error": messagebox.showerror,
            "question": messagebox.askquestion,
            "yesno": messagebox.askyesno,
            "okcancel": messagebox.askokcancel,
        }

        if msgbox_type in valid_msgbox_types:
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            valid_msgbox_types[msgbox_type]("Message Box Title", msg)
        else:
            print("Invalid message box type. Available options: info, warning, error, question, yesno, okcancel")
