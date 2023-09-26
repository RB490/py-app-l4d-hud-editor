"""Debug hotkeys"""
import threading

from loguru import logger
from shared_managers.hotkey_manager import HotkeyManager


def enable_debug_hotkeys():
    """Debug hotkeys"""

    # Set up hotkeys
    hotkey_manager = HotkeyManager()
    hotkey_manager.add_hotkey("F10", debugging_hotkey, suppress=True)

    logger.debug("Configured debug hotkeys")


# Execute debugging hotkey method in a separate thread
def execute_debugging_hotkey_method_in_thread():
    "Debug hotkey in the main thread in case it takes longer and causes issues with the keyboard module"
    thread = threading.Thread(target=debugging_hotkey)
    thread.start()
    print("Thread finished!!!")


# Debugging hotkey function
def debugging_hotkey():
    "Debug hotkey"
    print("Hotkey debugging method!")
    # debug_popup_gui()
    # hotkey_manager = HotkeyManager()
    # print(hotkey_manager.list_hotkeys())
