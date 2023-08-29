"""A class for managing window focus and mouse position."""
# pylint: disable=import-outside-toplevel, c-extension-no-member
import pyautogui
import win32gui

from utils.functions import focus_hwnd


class WindowFocusManager:
    """
    A class for managing window focus and mouse position.
    """

    def __init__(self):
        """
        Initialize the WindowFocusManager.
        """
        self.saved_hwnd = None
        self.saved_mouse_pos = None

    def get_focused_hwnd(self):
        """
        Get the handle of the currently focused window.

        Returns:
            int: The window handle (HWND) of the focused window.
        """
        return win32gui.GetForegroundWindow()

    def save_focus_state(self):
        """
        Save the current focus state and mouse position.

        Returns:
            int: The window handle (HWND) of the saved focused window.
        """
        self.saved_hwnd = self.get_focused_hwnd()
        self.saved_mouse_pos = pyautogui.position()
        return self.saved_hwnd

    def restore_focus_state(self):
        """
        Restore the saved focus state and mouse position.
        """
        if self.saved_hwnd:
            focus_hwnd(self.saved_hwnd)
        if self.saved_mouse_pos:
            pyautogui.moveTo(self.saved_mouse_pos)


def manage_focus_example():
    """
    Example usage of the WindowFocusManager class for managing window focus and mouse position.
    """
    import time

    focus_manager = WindowFocusManager()

    # Saving the current focus state
    focus_manager.save_focus_state()

    # Simulate some action that changes the focused window and mouse position
    # For example, you might want to open a different application or move the mouse
    print("Restoring focus & mousepos in 3 seconds")
    time.sleep(3)

    # Restoring the saved focus state
    focus_manager.restore_focus_state()
