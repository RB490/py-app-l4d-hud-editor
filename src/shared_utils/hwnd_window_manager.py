"""
This module provides a utility class for managing windows using their HWND (handle),
including methods to check process status, retrieve focused HWND, get process name, move windows, and focus windows.
"""
# pylint: disable=c-extension-no-member, broad-exception-caught, invalid-name, logging-fstring-interpolation
import ctypes
import functools
import logging
import os
import time

import psutil
import pyautogui
import win32api
import win32con
import win32gui
import win32process

from shared_utils.logging_manager import LoggingManager

logging_manager = LoggingManager(__name__, level=logging.INFO)
log = logging_manager.get_logger()


def hwnd_is_running_check(func):
    "Check if hwnd is running"

    @functools.wraps(func)
    def wrapper(self, hwnd, *args, **kwargs):
        if not self.running(hwnd):
            return None
        return func(self, hwnd, *args, **kwargs)

    return wrapper


class HwndWindowUtils:
    """
    This module provides a utility class for managing windows using their
    HWND (handle), including methods to check process status, retrieve focused HWND,
    get process name, move windows, and focus windows.
    """

    def __init__(self):
        self.saved_hwnd = None
        self.saved_mouse_pos = None
        self.hwnd_process_mapping = {}

    def get_hwnd_from_process_name_with_timeout_and_optionally_ram_usage(
        self, process_name, timeout, ram_usage_mb=None
    ):
        """
        Wait until a process is running and optionally consumes a specified amount of RAM.
        Return HWND if the process is found within the timeout and, if specified, RAM usage is reached,
        otherwise return None.

        :param process_name: The process name.
        :type process_name: str
        :param timeout: The maximum time to wait in seconds.
        :type timeout: float
        :param ram_usage_mb: The RAM usage in MB (optional).
        :type ram_usage_mb: int or None
        :return: hwnd: int or None
        :rtype: int or None

        Example:
            hwnd = wait_for_process_with_timeout("your_process_name.exe", timeout=60, ram_usage_mb=222)
            if hwnd is not None:
                log.debug(f"Process found with HWND: {hwnd}")
            else:
                log.debug("Process not found within the specified timeout or RAM usage.")
        """
        log.info(f"Waiting {timeout} seconds for '{process_name}' to run with RAM usage: {ram_usage_mb} MB")

        start_time = time.time()
        while time.time() - start_time <= timeout:
            try:
                for process in psutil.process_iter(attrs=["name", "pid", "memory_info"]):
                    if process.info["name"].lower() == process_name.lower():
                        if ram_usage_mb is not None:
                            process_memory_info = process.info["memory_info"]
                            ram_used_mb = process_memory_info.rss / (1024 * 1024)  # Convert bytes to MB
                            if ram_used_mb < ram_usage_mb:
                                continue

                        hwnd = self.get_hwnd_from_process_name(process_name)
                        log.debug(f"'{process_name}' is running!")
                        return hwnd
            except psutil.NoSuchProcess:
                pass

            time.sleep(0.1)

        log.debug(f"Process '{process_name}' not found within the specified timeout of {timeout} seconds.")
        return None

    def get_hwnd_from_process_name(self, process_name):
        # pylint: disable=c-extension-no-member
        """
        Retrieves the window handle for a process based on its process name.
        """
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"].lower() == process_name.lower():  # .lower() to ignore caption
                pid = proc.pid
                handle_list = []

                def callback(handle, handle_list):
                    handle_list.append(handle)

                win32gui.EnumWindows(callback, handle_list)
                for handle in handle_list:
                    if win32process.GetWindowThreadProcessId(handle)[1] == pid:
                        self.set_process_name(handle, process_name)
                        log.debug(f"Set {process_name} HWND ({handle})")
                        return handle
        return None

    def get_hwnd_focused(self):
        """Retrieve hwnd from focused window"""
        hwnd = win32gui.GetForegroundWindow()
        self.get_process_name(hwnd)
        log.debug(f"Focused hwnd = {hwnd}")
        return hwnd

    def set_process_name(self, hwnd, process_name):
        """Set process name"""
        self.hwnd_process_mapping[hwnd] = process_name
        log.debug(f"Set HWND {hwnd} process name: {process_name}")

    def get_process_name(self, hwnd):
        """Retrieve process name if not already set"""

        # lookup process name if needed
        if hwnd not in self.hwnd_process_mapping:
            process_name = self.running(hwnd)
            self.set_process_name(hwnd, process_name)

        # return process name
        process_name = self.hwnd_process_mapping.get(hwnd, None)
        log.debug(f"Retrieved process name '{process_name}' for HWND {hwnd}")
        return process_name

    @hwnd_is_running_check
    def wait_close(self, hwnd, timeout=None):
        "Wait for a window to close (if it exists)"

        process_name = self.get_process_name(hwnd)

        # Otherwise, wait for the window to be destroyed or until timeout is reached
        log.info(f"Waiting for {process_name} to close")
        start = time.time()
        while True:
            # Check if the window still exists
            exists = win32gui.IsWindow(hwnd)
            # If not, return
            if not exists:
                log.info(f"{process_name} closed!")
                return True
            # Otherwise, check the elapsed time if timeout is provided
            if timeout is not None:
                elapsed = time.time() - start
                # If timeout is reached, return
                if elapsed >= timeout:
                    log.warning(f"{process_name} did not close after {timeout} seconds")
                    return False
            # Sleep for a short interval and repeat
            time.sleep(0.1)

    def close(self, hwnd):
        """Close window"""
        user32 = ctypes.windll.user32
        user32.PostMessageW(hwnd, 0x0010, 0, 0)  # 0x0010 is the message code for WM_CLOSE
        log.info(f"Closed {self.get_process_name(hwnd)}!")

    def running(self, hwnd):
        """Confirm whether hwnd is running. Also works if invisible. Sets & returns process name"""
        if not hwnd:
            logging.warning(f"Running() did not receive a HWND! '{hwnd}'. Cancelling HWND operation!")
            return False

        process_name = None  # Initialize the variable before the try block
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)
            is_running = psutil.pid_exists(pid)
            process_name = process.name()
            self.set_process_name(hwnd, process_name)
            log.debug(f"Process {process_name} is {'running!' if is_running else 'not running!'}")
            return process_name
        except psutil.NoSuchProcess:
            log.warning(f"Process {process_name} not found!")
            return False

    @hwnd_is_running_check
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
            log.debug("No position provided, defaulting to center!")
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

        log.debug(f"Moved '{self.get_process_name(hwnd)}' to position ({win_x}, {win_y})")

    @hwnd_is_running_check
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

        # Set the window to the foreground
        try:
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            log.debug(f"Error while setting foreground window: {e}")

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

        log.debug(f"Focused {self.get_process_name(hwnd)}!")

    def save_focus_state(self):
        """
        Save the current focus state and mouse position.

        Returns:
            int: The window handle (HWND) of the saved focused window.
        """
        self.saved_hwnd = self.get_hwnd_focused()
        self.saved_mouse_pos = pyautogui.position()
        log.debug(f"Saved focus state to {self.get_process_name(self.saved_hwnd)}!")
        return self.saved_hwnd

    def restore_focus_state(self):
        """
        Restore the saved focus state and mouse position.
        """
        if self.saved_hwnd:
            self.focus(self.saved_hwnd)
        if self.saved_mouse_pos:
            pyautogui.moveTo(self.saved_mouse_pos)
        log.debug(f"Restored focus state to {self.get_process_name(self.saved_hwnd)}!")


def showcase_hwnd_window_manager():
    """Showcase class"""
    hwnd_utils = HwndWindowUtils()

    # set hwnd
    print("Retrieving focused HWND in 1 second")
    time.sleep(1)
    hwnd = hwnd_utils.get_hwnd_focused()

    # perform action
    input("Press enter to perform HWND action")
    result = hwnd_utils.get_process_name(hwnd)
    hwnd_utils.move(hwnd, "Center")
    hwnd_utils.focus(hwnd)

    # display result
    print(f"result={result}")
