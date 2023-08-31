# pylint: disable=broad-exception-caught, import-outside-toplevel, no-member, c-extension-no-member, bare-except
"""Functions used throughout the program"""
import os
import random
import string
import sys
import time
import tkinter as tk
from tkinter import filedialog

import psutil
import pyautogui

from game.game import Game
from shared_utils.shared_utils import show_message
from utils.persistent_data_manager import PersistentDataManager

from .constants import BACKUP_APPEND_STRING, IMAGES_DIR_EXT


def get_browser_gui():
    "There can only be one main Tkinter GUI using root.mainloop() at oncee"
    from gui.browser import GuiHudBrowser
    from gui.start import GuiHudStart

    # destroy other main gui
    start_gui = GuiHudStart()

    if not start_gui.get_mainloop_started():
        raise ValueError("Retrieved browser GUI without having started mainloop() first")

    browser_gui = GuiHudBrowser(start_gui.root)
    browser_gui.treeview_refresh(browser_gui.treeview)
    browser_gui.show()
    return browser_gui


def show_start_gui():
    "There can only be one main Tkinter GUI using root.mainloop() at oncee"
    from gui.start import GuiHudStart

    start_gui = GuiHudStart()
    start_gui.show()
    return


def count_files_and_dirs(path):
    "Count files and directories"
    total_files = 0
    total_subdirs = 0

    for _, dirs, files in os.walk(path):
        total_subdirs += len(dirs)
        total_files += len(files)

    return total_files, total_subdirs


def get_backup_path(file_path):
    """Get a backup path by appending 'append backup string' to the input file path"""
    backup_path = file_path + BACKUP_APPEND_STRING
    return backup_path


def get_backup_filename(file_name):
    """Get a backup file name by appending 'append backup string' to the input file path"""
    backup_file_name = file_name + BACKUP_APPEND_STRING
    return backup_file_name


def get_image_for_file_extension(input_path):
    "Retrieve image for file extension"

    # Get the file extension
    file_extension = os.path.splitext(input_path)[1]

    if not file_extension:
        return os.path.join(IMAGES_DIR_EXT, "folder.ico")

    # Define the file types and their corresponding icons
    file_types = {
        ".txt": os.path.join(IMAGES_DIR_EXT, "text.ico"),
        ".res": os.path.join(IMAGES_DIR_EXT, "resource.ico"),
        ".cfg": os.path.join(IMAGES_DIR_EXT, "config.ico"),
        ".jpg": os.path.join(IMAGES_DIR_EXT, "image.ico"),
        ".png": os.path.join(IMAGES_DIR_EXT, "image.ico"),
        ".vmt": os.path.join(IMAGES_DIR_EXT, "resource.ico"),
        ".vtf": os.path.join(IMAGES_DIR_EXT, "image.ico"),
    }

    # Get the corresponding image path or return "warning.png"
    output_image_path = file_types.get(file_extension, os.path.join(IMAGES_DIR_EXT, "error.ico"))

    # print(f"Retrieved image for {input_path} -> {output_image_path}")
    return output_image_path


def generate_random_string(length=8):
    "Generate random string"
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def rename_with_timeout(src, dst, timeout=5):
    """Try to rename src to dst within timeout seconds.

    This aims to work around some possible exceptions:
    - A program that's shutting down is still temporary locking them
    - Miscelanious operating system issue where renaming fails once but is fine the next time"""
    start = time.time()

    print(f"Renaming {src} -> {dst} with timeout: {timeout}")

    while True:
        try:
            os.rename(src, dst)
            return True
        except Exception:
            if time.time() - start > timeout:
                print("Failed to rename!")
                return False
            else:
                time.sleep(0.1)


def prompt_for_folder(title):
    """Prompt user for a folder"""
    return filedialog.askdirectory(title=title)


def wait_process_close(executable, timeout=None):
    "Wait for a process to close (if it exists)"

    # Get the list of processes with the same name as the executable
    processes = [p for p in psutil.process_iter() if p.name() == executable]
    # If no processes are found, return immediately
    if not processes:
        print(f"{executable} is not running!")
        return False

    # Otherwise, wait for the processes to terminate or until timeout is reached
    print(f"Waiting for {executable} to close")
    start = time.time()
    while True:
        # Check if any process is still alive
        alive = any(p.is_running() for p in processes)
        # If not, return
        if not alive:
            print(f"Process {executable} closed!")
            return True
        # Otherwise, check the elapsed time if timeout is provided
        if timeout is not None:
            elapsed = time.time() - start
            # If timeout is reached, raise an exception
            if elapsed >= timeout:
                print(f"Process {executable} did not close after {timeout} seconds")
                return False
        # Sleep for a short interval and repeat
        time.sleep(0.1)


def get_dir_size(path):
    """Retrieve directory size in bytes"""
    total = 0
    with os.scandir(path) as scandir_result:
        for entry in scandir_result:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_dir_size_in_gb(path):
    """Retrieve directory size in gigaytes"""
    size_in_bytes = get_dir_size(path)
    size_in_gb = round(size_in_bytes / (1024**3), 2)
    output = f"{size_in_gb} GB"
    return output


def move_cursor_to(coordinates):
    # pylint: disable=invalid-name
    """
    Moves the mouse cursor to the specified (x, y) coordinate on screen.

    Arguments:
    coordinates -- a tuple with (x, y) values representing the desired cursor position.
    """
    x, y = coordinates[0], coordinates[1]
    pyautogui.moveTo(x, y)


def click_at(coordinates):
    # pylint: disable=invalid-name
    """
    Performs a left mouse click at the specified (x, y) coordinate on screen.

    Arguments:
    coordinates -- a tuple with (x, y) values representing the desired click position.
    """
    x, y = coordinates[0], coordinates[1]
    pyautogui.click(x, y)


def get_mouse_position_on_click(callback):
    """
    Calls the callback function with the x, y coordinates of where the user clicks the mouse on the screen.

    This function creates a fullscreen window that listens for a mouse click event.
    When clicked, it destroys the window and calls the callback function with the (x,y) coordinates of the click.
    If the user cancels the operation or closes the window, the function calls the callback function with (None,None).
    """
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # make window fullscreen
    root.attributes("-topmost", True)  # keep window on top
    root.attributes("-alpha", 0.1)  # set transparency to 0.5 (125/255)
    root.overrideredirect(True)  # remove window decorations

    def on_click(event):
        pos_x, pos_y = event.x_root, event.y_root
        print(f"Mouse clicked at ({pos_x}, {pos_y})")
        root.destroy()  # destroy the window when mouse is clicked
        callback(pos_x, pos_y)

    root.bind("<ButtonPress>", on_click)
    root.mainloop()


def preform_checks_to_prepare_program_start():
    """Run vital checks before starting program so i don't need to add them everywhere"""
    game = Game()

    # warn about dev being out of date
    if game.dir.dev_out_of_date():
        show_message("Developer directory is out of date!\nConsider updating it", "warning")

    # verify validity of ID file structure
    try:
        game.dir.check_for_invalid_id_file_structure()
    except Exception as e_info:
        raise ValueError(f"Invalid ID file structure! Fix it before running program: {e_info}") from e_info


def save_and_exit_script():
    """Exit the script"""
    # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
    from hud.hud import Hud

    hud_instance = Hud()
    hud_instance.edit.finish_editing(open_start_gui=False)
    PersistentDataManager().save()
    sys.exit()
