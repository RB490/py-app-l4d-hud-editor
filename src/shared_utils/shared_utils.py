"""Shared utility functions"""
# pylint: disable=c-extension-no-member, broad-exception-caught
import os
import re
import sys
import tkinter as tk
from tkinter import messagebox
from typing import Dict, Type

import psutil
import win32api
import win32con
import win32gui
import win32process
from ahk import AHK


def add_empty_menu_separator(menu):
    empty_separator_label = " "  # Space as the label
    menu.add_command(label=empty_separator_label, state=tk.DISABLED, font=("Helvetica", 1))  # Small font size


def create_lambda_command(func, *args):
    # pylint: disable=line-too-long
    """
    The `create_lambda_command` method takes in a function `func`
    and any number of positional arguments `*args`
    and returns a lambda function that, when called,
    will execute the given function with the supplied arguments.

    :param self: the instance of the class that the method belongs to.
    :param func: the function that will be executed by the lambda command returned from this method.
    :param *args: any number of positional arguments that will be passed to the function when
        called through the returned lambda command.

    :return: A lambda function that executes the input function `func` with its corresponding arguments `args`.

    #Example:
        campaign_submenu.add_command(
            label=map_name, command=self.create_lambda_command(self.handler.load_map, map_name, map_code)
        )
        > so when this menu entry is selected self.handler.load_map gets called with map_name and map_code

    This method is useful for creating a function on-the-fly that takes no arguments
    but still needs to execute some code with certain values or variables.
    By using a lambda function created by `create_lambda_function`,
    you can defer binding the arguments until later when needed.
    This technique is also known as partial evaluation or currying,
    and it is commonly used in functional programming.
    """
    return lambda: func(*args)


def replace_text_between_quotes(input_string, replacement_text):
    """Replace text between quotes. Multiple double quotes supported"""
    pattern = r'"([^"]*)"'
    replaced_string = re.sub(pattern, f'"{replacement_text}"', input_string)
    return replaced_string


def verify_directory(directory, error_message):
    """Reduces clutter. Example: if not verify_directory(source_dir, "Could not retrieve source directory!"):"""
    if not os.path.isdir(directory):
        print(error_message)
        return False
    return True


def is_subdirectory(parent_dir, child_dir):
    """
    Check if a directory is a subdirectory of another directory.

    Args:
        parent_dir (str): The parent directory.
        child_dir (str): The potential subdirectory.

    Returns:
        bool: True if child_dir is a subdirectory of parent_dir, False otherwise.
    """
    parent_path = os.path.abspath(parent_dir)
    child_path = os.path.abspath(child_dir)

    # Normalize paths to handle different path separators and case sensitivity
    parent_path = os.path.normcase(parent_path)
    child_path = os.path.normcase(child_path)

    # Normalize paths to handle different path separators and case sensitivity
    parent_path = os.path.normpath(parent_path)
    child_path = os.path.normpath(child_path)

    if child_path.startswith(parent_path):
        print(f"{child_dir} is a subdirectory of {parent_dir}")
        return True
    else:
        print(f"{child_dir} is not subdirectory of {parent_dir}")
        return False


def move_window_with_ahk(window_title, new_x, new_y):
    "Move window: https://pypi.org/project/ahk/"
    ahk = AHK()

    try:
        win = ahk.find_window(title=window_title)  # Find the opened window
        win.move(new_x, new_y)
        print(f"Moved {window_title} -> {new_x}x{new_y}")
    except Exception:
        print("Failed to move window using AHK")


def move_hwnd_to_position(hwnd, position):
    """
    Move a window (specified by its hwnd) to the desired position on the screen.

    Args:
        hwnd (int): The handle of the window to be moved.
        position (str or tuple or dict): The desired position on the screen.
            It can be a predefined position (str) from the list of predefined_positions,
            a tuple (x, y) with specific coordinates, or a dictionary {'x': x, 'y': y}.

    Raises:
        ValueError: If the position format is invalid.
    """
    predefined_positions = {
        "Center": (0.5, 0.5),
        "Top Left": (0, 0),
        "Top Right": (1, 0),
        "Bottom Left": (0, 1),
        "Bottom Right": (1, 1),
        "Top": (0.5, 0),
        "Bottom": (0.5, 1),
        "Left": (0, 0.5),
        "Right": (1, 0.5),
    }

    rect = win32gui.GetWindowRect(hwnd)
    win_width = rect[2] - rect[0]
    win_height = rect[3] - rect[1]

    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    if position is None or position == "":
        print("No position provided, defaulting to center!")
        position = "Center"

    if position in predefined_positions:
        win_x, win_y = predefined_positions[position]
        win_x = int(win_x * (screen_width - win_width))
        win_y = int(win_y * (screen_height - win_height))
    elif isinstance(position, tuple):
        win_x, win_y = position
    elif isinstance(position, dict) and "x" in position and "y" in position:
        win_x, win_y = position["x"], position["y"]
    else:
        raise ValueError("Invalid position format")

    win32gui.SetWindowPos(hwnd, None, win_x, win_y, win_width, win_height, win32con.SWP_NOZORDER)

    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    window_executable = os.path.basename(psutil.Process(pid).exe())
    print(f"Moved '{window_executable}' to position ({win_x}, {win_y})")


def close_process_executable(executable):
    "Close process based on executable"
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == executable:
            proc.kill()
            proc.wait()  # Wait for the process to fully terminate
            break


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
