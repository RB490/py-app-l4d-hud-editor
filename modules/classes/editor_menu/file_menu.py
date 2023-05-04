# file_menu.py
import tkinter as tk


def create_file_menu(root):
    file_menu = tk.Menu(root)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As...", command=save_file_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Add a checkbutton for mute
    var = tk.BooleanVar()
    var.set(False)

    def toggle_mute():
        var.set(not var.get())
        if var.get():
            file_menu.entryconfig("Mute", label="Unmute", state="normal")
        else:
            file_menu.entryconfig("Mute", label="Mute", state="normal")
        print("this is a test")

    file_menu.add_checkbutton(label="Mute", variable=var, command=toggle_mute)
    # mute_menu = file_menu.add_checkbutton(label="Mute", variable=var, command=toggle_mute)

    return file_menu, var


def new_file():
    print("Creating a new file...")


def open_file():
    print("Opening a file...")


def save_file():
    print("Saving the current file...")


def save_file_as():
    print("Saving the current file as...")
