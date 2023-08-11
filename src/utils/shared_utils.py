"""Shared utility functions"""
import os
import sys
import tkinter as tk
from tkinter import messagebox
from typing import Dict, Type


class Singleton(type):
    """Metaclass for creating singleton classes.

    Example:
        class MySingleton(metaclass=Singleton):
            def __init__(self, value):
                self.value = value

            # Creating instances
            instance1 = MySingleton(42)
            instance2 = MySingleton(99)

            # Both instances are the same
            print(instance1 is instance2)  # Output: True
            print(instance1.value)         # Output: 99
            print(instance2.value)         # Output: 99
    """

    _instances: Dict[Type["Singleton"], "Singleton"] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def show_message(msg, msgbox_type="info", title=None):
    """
    Show message by printing it and showing in a messagebox if running as .pyw

    Args:
        msg (str): The message to be displayed.
        msgbox_type (str, optional): The type of messagebox to show ("info", "warning", "error",
            "question", "yesno", "okcancel"). Default is "info".
        title (str, optional): The title for the message box. Default is "Message Box".

    Returns:
        bool or None: For "yesno" and "okcancel" types, returns True if "Yes" or "OK" is clicked,
        and False if "No" or "Cancel" is clicked. For other types, returns None.

    Example:
        # Example usage
        response = show_message("This is a message.", "okcancel", "Confirmation")
        if response is not None:
            if response:
                print("User clicked OK")
            else:
                print("User clicked Cancel")
    """

    # Retrieve variables
    script_extension = os.path.splitext(sys.argv[0])[1].lower()
    script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    script_name_long = script_name + script_extension

    # Always print the message
    print(msg)

    # If running in windowed mode (.pyw) and a valid msgbox_type is provided, show the messagebox
    if not title:
        title = script_name_long
    else:
        title = script_name_long + " - " + title
    # if msgbox_type and script_extension == ".pyw":
    if msgbox_type:
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

            # Capture the response of the messagebox
            response = valid_msgbox_types[msgbox_type](title, msg)

            # Return the response to the caller
            return response
        else:
            raise ValueError(
                "Invalid message box type. Available options: info, warning, error, question, yesno, okcancel"
            )
