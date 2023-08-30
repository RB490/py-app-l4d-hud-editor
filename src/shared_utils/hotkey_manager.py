import logging

import keyboard

from shared_utils.logging_manager import LoggerManager
from shared_utils.shared_utils import Singleton

logger_manager = LoggerManager(__name__, level=logging.INFO)
# logger_manager = LoggerManager(__name__, level=logging.WARNING)
logger = logger_manager.get_logger()


class HotkeyManager(metaclass=Singleton):
    def __init__(self):
        self.hotkeys = {}  # Store registered hotkeys
        logger.debug("HotkeyManager instance created.")

    def add_hotkey(self, hotkey, callback, suppress=True):
        if hotkey in self.hotkeys:
            raise ValueError(f"Hotkey '{hotkey}' already exists.")
        
        keyboard.add_hotkey(hotkey, callback, suppress=suppress)
        self.hotkeys[hotkey] = callback
        logger.info("Added hotkey: %s", hotkey)

    def remove_hotkey(self, hotkey):
        if hotkey in self.hotkeys:
            keyboard.remove_hotkey(hotkey)
            del self.hotkeys[hotkey]
            logger.info("Removed hotkey: %s", hotkey)
        else:
            logger.warning("Attempted to remove non-existent hotkey: %s", hotkey)

    def list_hotkeys(self):
        hotkey_list = list(self.hotkeys.keys())
        logger.debug("List of hotkeys: %s", hotkey_list)
        return hotkey_list


# Example of how to use the HotkeyManager class
def hotkey_showcase_hotkey_manager():
    print("hotkey_showcase_hotkey_manager: F10 hotkey pressed!")


def showcase_hotkey_manager():
    hotkey_manager = HotkeyManager()
    hotkey_manager.add_hotkey("F10", hotkey_showcase_hotkey_manager, suppress=True)

    print("Registered hotkeys:", hotkey_manager.list_hotkeys())

    input("Press Enter to remove the F10 hotkey...")

    hotkey_manager.remove_hotkey("F10")

    print("Registered hotkeys after removal:", hotkey_manager.list_hotkeys())
