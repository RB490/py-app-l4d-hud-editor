"""
HotkeyManager.
"""
import logging

import keyboard

from shared_utils.logging_manager import LoggingManager
from shared_utils.shared_utils import Singleton

logging_manager = LoggingManager(__name__, level=logging.INFO)
# logging_manager = LoggingManager(__name__, level=logging.DEBUG)
log = logging_manager.get_logger()


class HotkeyManager(metaclass=Singleton):
    """
    Initialize an instance of HotkeyManager.
    """

    def __init__(self):
        """
        Initialize an instance of HotkeyManager.
        """
        self.hotkeys = {}  # Store registered hotkeys
        log.debug("HotkeyManager instance created.")

    def add_hotkey(self, hotkey, callback, suppress=True):
        """
        Register a new hotkey.

        Args:
            hotkey (str): The hotkey combination, e.g., "Ctrl+Shift+A".
            callback (function): The function to be called when the hotkey is pressed.
            suppress (bool, optional): Whether to suppress the hotkey in the active application. Default is True.
        """
        if hotkey in self.hotkeys:
            raise ValueError(f"Hotkey '{hotkey}' already exists.")

        keyboard.add_hotkey(hotkey, callback, suppress=suppress)
        self.hotkeys[hotkey] = callback
        log.debug("Added hotkey: %s", hotkey)

    def remove_hotkey(self, hotkey):
        """
        Remove a registered hotkey.

        Args:
            hotkey (str): The hotkey to be removed.
        """
        if hotkey in self.hotkeys:
            keyboard.remove_hotkey(hotkey)
            del self.hotkeys[hotkey]
            log.debug("Removed hotkey: %s", hotkey)
        else:
            log.warning("Attempted to remove non-existent hotkey: %s", hotkey)

    def list_hotkeys(self):
        """
        List all currently registered hotkeys.

        Returns:
            list: A list of strings representing the registered hotkeys.
        """
        hotkey_list = list(self.hotkeys.keys())
        log.debug("List of hotkeys: %s", hotkey_list)
        return hotkey_list


# Example of how to use the HotkeyManager class
def hotkey_showcase_hotkey_manager():
    "debug"
    print("hotkey_showcase_hotkey_manager: F10 hotkey pressed!")


def showcase_hotkey_manager():
    "debug"
    hotkey_manager = HotkeyManager()
    hotkey_manager.add_hotkey("F10", hotkey_showcase_hotkey_manager, suppress=True)

    print("Registered hotkeys:", hotkey_manager.list_hotkeys())

    input("Press Enter to remove the F10 hotkey...")

    hotkey_manager.remove_hotkey("F10")

    print("Registered hotkeys after removal:", hotkey_manager.list_hotkeys())
