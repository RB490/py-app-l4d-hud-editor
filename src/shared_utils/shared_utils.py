"""Shared utility functions"""
# pylint: disable=c-extension-no-member, broad-exception-caught, broad-exception-raised, logging-fstring-interpolation
import os
import re
import shutil
import sys
import tempfile
import tkinter as tk
from tkinter import Menu, messagebox
from typing import Any, Callable, Dict, Type, TypeVar

from ahk import AHK
from loguru import logger

T = TypeVar("T", bound="Singleton")

def create_and_open_temp_file(file_path):
    """Create a temporary directory, copy the file, and open the temporary file."""
    # Create a temporary directory in %temp%
    temp_dir = tempfile.mkdtemp(dir=os.environ.get('TEMP'))

    # Get the file name from the original path
    file_name = os.path.basename(file_path)

    # Create a temporary file path in the temporary directory
    temp_file_path = os.path.join(temp_dir, file_name)

    # Copy the content of the original file to the temporary file
    shutil.copy(file_path, temp_file_path)

    # Open the temporary file
    os.startfile(temp_file_path)

def get_invisible_tkinter_root() -> tk.Tk:
    """Retrieve invisible tkinter root gui"""
    root = tk.Tk()
    root.withdraw()
    return root


def add_empty_menu_separator(menu: Menu) -> None:
    """Add empty menu item to act as separator.

    Args:
        menu (Menu): The menu to which the separator should be added.
    """
    empty_separator_label: str = " "  # Space as the label
    menu.add_command(label=empty_separator_label, state=tk.DISABLED, font=("Helvetica", 1))  # Small font size


def create_lambda_command(func: Callable[..., Any], *args: Any) -> Callable[[], Any]:
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


def replace_text_between_quotes(input_string: str, replacement_text: str) -> str:
    """
    Replace text between quotes. Multiple double quotes supported.

    Args:
        input_string (str): The input string containing quoted text.
        replacement_text (str): The text to replace the quoted text with.

    Returns:
        str: The modified string with replaced text.
    """
    pattern = r'"([^"]*)"'
    replaced_string = re.sub(pattern, f'"{replacement_text}"', input_string)
    return replaced_string


def verify_directory(directory: str, error_message: str) -> bool:
    """
    Reduces clutter. Example: if not verify_directory(source_dir, "Could not retrieve source directory!"):

    Args:
        directory (str): The directory path to verify.
        error_message (str): The error message to print if the directory doesn't exist.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    if not os.path.isdir(directory):
        print(error_message)
        return False
    return True


def is_subdirectory(parent_dir: str, child_dir: str) -> bool:
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
        print(f"{child_dir} is not a subdirectory of {parent_dir}")
        return False


def copy_directory(src_dir, dest_dir):
    """Copy the files from a source directory to a destination directory, overwriting if necessary.

    This function recursively copies files from the source directory to the destination
    directory, preserving the directory structure. Any existing files in the destination
    directory will be overwritten.

    Benefits of using this function as opposed to shutil.copytree:
    - shutil.copytree needs the destination directory to not exist, while this function merges them
    - i can see individual files printed out in console

    Args:
        src_dir (str): The path to the source directory.
        dest_dir (str): The path to the destination directory.

    Returns:
        None
    """

    try:
        # Normalize paths
        src_dir = os.path.normpath(src_dir)
        dest_dir = os.path.normpath(dest_dir)

        # Verify and create destination directory if needed
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        elif not os.path.isdir(dest_dir):
            raise NotADirectoryError(f"The destination directory {dest_dir} is not valid.")

        # Build a list of source files to be copied
        src_files = [os.path.join(root, filename) for root, _, files in os.walk(src_dir) for filename in files]

        # Raise exception if no source files found
        if not src_files:
            raise Exception(f"No files in the source directory: {src_dir}")

        logger.info(f"Copying files '{src_dir}' -> '{dest_dir}'")

        # Copy each source file to the destination
        for src_path in src_files:
            relative_path = os.path.relpath(src_path, src_dir)
            dest_path = os.path.join(dest_dir, relative_path)

            # Create the destination directory if it doesn't exist
            relative_dir = os.path.dirname(dest_path)
            if not os.path.exists(relative_dir):
                os.makedirs(relative_dir)

            # Attempt to copy the file, handle errors
            try:
                shutil.copy2(src_path, dest_path)
                logger.debug(f"Copied {src_path} -> {dest_path}")
            except shutil.Error as copy_error:
                logger.error(f"Copy error: {copy_error}")
            except Exception as general_error:
                logger.error(f"An error occurred: {general_error}")

    except Exception as err_info:
        logger.error(f"An error occurred during copy files in directory: {err_info}")
    else:
        logger.info(f"Copied files '{src_dir}' -> '{dest_dir}'")


def move_window_with_ahk(window_title: str, new_x: int, new_y: int) -> None:
    """
    Move window: https://pypi.org/project/ahk/

    Args:
        window_title (str): The title of the window to move.
        new_x (int): The new x-coordinate of the window.
        new_y (int): The new y-coordinate of the window.
    """
    ahk = AHK()

    try:
        win = ahk.find_window(title=window_title)  # Find the opened window
        win.move(new_x, new_y)  # type: ignore
        print(f"Moved {window_title} -> {new_x}x{new_y}")
    except Exception:
        print("Failed to move window using AHK")


def show_message(msg: str, msgbox_type: str = "info", title: str = "") -> Any:
    """
    Show a message and optionally a message box.

    Args:
        msg (str): The message to display.
        msgbox_type (str, optional): Type of message box to display:
            ("info", "warning", "error", "question", "yesno", "okcancel"). Defaults to "info".
        title (str, optional): Title for the message box. Defaults to the script name.

    Returns:
        Any: The response from the message box (if shown).
    """
    # Retrieve variables
    script_extension: str = os.path.splitext(sys.argv[0])[1].lower()
    script_name: str = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    script_name_long: str = script_name + script_extension

    # Always print the message
    print(msg)

    # If running in windowed mode (.pyw) and a valid msgbox_type is provided, show the messagebox
    if not title:
        title = script_name_long
    else:
        title = script_name_long + " - " + title
    # if msgbox_type and script_extension == ".pyw":
    if msgbox_type:
        valid_msgbox_types: Dict[str, Callable[[str, str], Any]] = {
            "info": messagebox.showinfo,  # type: ignore
            "warning": messagebox.showwarning,  # type: ignore
            "error": messagebox.showerror,  # type: ignore
            "question": messagebox.askquestion,  # type: ignore
            "yesno": messagebox.askyesno,  # type: ignore
            "okcancel": messagebox.askokcancel,  # type: ignore
        }

        if msgbox_type in valid_msgbox_types:
            # Capture the response of the messagebox
            response: Any = valid_msgbox_types[msgbox_type](title, msg)

            # Return the response to the caller
            return response
        else:
            raise ValueError(
                "Invalid message box type. Available options: info, warning, error, question, yesno, okcancel"
            )


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

    def __call__(cls: Type[T], *args, **kwargs) -> T:  # type: ignore
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]  # type: ignore
