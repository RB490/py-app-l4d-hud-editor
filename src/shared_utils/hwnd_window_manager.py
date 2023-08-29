"""
This module provides a utility class for managing windows using their HWND (handle),
including methods to check process status, retrieve focused HWND, get executable name, move windows, and focus windows.
"""
# pylint: disable=c-extension-no-member, broad-exception-caught, invalid-name
import os
import time

import psutil
import pyautogui
import win32api
import win32con
import win32gui
import win32process


class HwndWindowUtils:
    """
    This module provides a utility class for managing windows using their
    HWND (handle), including methods to check process status, retrieve focused HWND,
    get executable name, move windows, and focus windows.
    """

    def __init__(self):
        self.saved_hwnd = None
        self.saved_mouse_pos = None

    @staticmethod
    def get_hwnd_from_executable(executable_name):
        # pylint: disable=c-extension-no-member
        """
        Retrieves the window handle for a process based on its executable name.
        """
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] == executable_name:
                pid = proc.pid
                handle_list = []

                def callback(handle, handle_list):
                    handle_list.append(handle)

                win32gui.EnumWindows(callback, handle_list)
                for handle in handle_list:
                    if win32process.GetWindowThreadProcessId(handle)[1] == pid:
                        return handle
        return None

    @staticmethod
    def get_hwnd_focused():
        """Retrieve hwnd from focused window"""
        hwnd = win32gui.GetForegroundWindow()
        print(f"Focused hwnd = {hwnd}")
        return hwnd

    def running(self, hwnd):
        """Confirm whether hwnd is running. Also works if invisible"""
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)
            is_running = psutil.pid_exists(pid)
            process_executable = process.name()
            print(f"Process {process_executable} is {'running' if is_running else 'not running'}")
            return process_executable
        except psutil.NoSuchProcess:
            print("Process not found")
            return False

    def get_executable_name(self, hwnd):
        """Retrieve executable name"""
        # Verify hwnd param
        if not self.running(hwnd):
            return None

        return self.running(hwnd)

    def move(self, hwnd, position="Center"):
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
        # Verify hwnd param
        if not self.running(hwnd):
            return None

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

    def focus(self, hwnd):
        # pylint: disable=c-extension-no-member
        """
        Function to focus a window.

        Alternate way to do this:
            # use pywinauto to get around SetForegroundWindow error/limitation: https://stackoverflow.com/a/30314197
            # be aware that pywinauto moves the cursor. which has a side effect of
            # for example moving the camera in source games
            from pywinauto import Application
            game_app = Application().connect(handle=game_hwnd)
            game_app.top_window().set_focus()
        """

        # Verify hwnd param
        if not self.running(hwnd):
            print("Invalid window handle!")
            return None

        # Set the window to the foreground
        try:
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print("Error while setting foreground window:", e)

        # # If the window is minimized, restore it
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # # Bring the window to the top
        win32gui.BringWindowToTop(hwnd)

        # # Set the window's position and size to the foreground
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Set the window to topmost
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # Disable topmost
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

        # # Activate the window
        win32gui.SetActiveWindow(hwnd)  # <- this works for tkinter gui's in combination with topmost

        print(f"Focused hwnd: {hwnd}!")

    def save_focus_state(self):
        """
        Save the current focus state and mouse position.

        Returns:
            int: The window handle (HWND) of the saved focused window.
        """
        self.saved_hwnd = self.get_hwnd_focused()
        self.saved_mouse_pos = pyautogui.position()
        return self.saved_hwnd

    def restore_focus_state(self):
        """
        Restore the saved focus state and mouse position.
        """
        if self.saved_hwnd:
            self.focus(self.saved_hwnd)
        if self.saved_mouse_pos:
            pyautogui.moveTo(self.saved_mouse_pos)


def showcase_hwnd_window_manager():
    """Showcase class"""
    hwnd_utils = HwndWindowUtils()

    # set hwnd
    print("Retrieving focused HWND in 1 second")
    time.sleep(1)
    hwnd = hwnd_utils.get_hwnd_focused()

    # perform action
    input("Press enter to perform HWND action")
    result = hwnd_utils.get_executable_name(hwnd)
    hwnd_utils.move(hwnd, "Center")
    hwnd_utils.focus(hwnd)

    # display result
    print(f"result={result}")
