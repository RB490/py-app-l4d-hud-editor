"""
HotkeyManager.
"""
import keyboard
from loguru import logger

from shared_utils.shared_utils import Singleton


class HotkeyManager(metaclass=Singleton):
    """
    Initialize an instance of HotkeyManager.
    """

    def __init__(self):
        """
        Initialize an instance of HotkeyManager.
        """
        self.hotkeys = {}  # Store registered hotkeys
        logger.debug("HotkeyManager instance created.")

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
        logger.debug(f"Added hotkey: {hotkey}")

    def hotkey_exists(self, hotkey):
        """
        Check if a hotkey is already registered.

        Args:
            hotkey (str): The hotkey to check.

        Returns:
            bool: True if the hotkey is already registered, False otherwise.
        """
        return hotkey in self.hotkeys

    def remove_hotkey(self, hotkey):
        """
        Remove a registered hotkey.

        Args:
            hotkey (str): The hotkey to be removed.
        """
        if hotkey in self.hotkeys:
            keyboard.remove_hotkey(hotkey)
            del self.hotkeys[hotkey]
            logger.debug(f"Removed hotkey: {hotkey}")
        else:
            logger.debug(f"Attempted to remove non-existent hotkey: {hotkey}")

    def list_hotkeys(self):
        """
        List all currently registered hotkeys.

        Returns:
            list: A list of strings representing the registered hotkeys.
        """
        hotkey_list = list(self.hotkeys.keys())
        logger.debug(f"List of hotkeys: {hotkey_list}")
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
