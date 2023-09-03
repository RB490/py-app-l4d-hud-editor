"""Debug"""
import os

from loguru import logger

from debug.game import debug_game_set_states_synced_and_installed
from debug.hotkeys import enable_debug_hotkeys
from utils.persistent_data_manager import PersistentDataManager


def main_misc_debug():
    """Debug"""
    logger.info("This is an info message")


def setup_debugging_environment():
    """Debug"""
    os.system("cls")  # Clear the terminal
    print("Started debugging!")
    debug_game_set_states_synced_and_installed()
    enable_debug_hotkeys()


# Debugging function with variable parameters
def debug_function_variable_params(*args):
    """Debug"""
    print(f"debug_function args={args}")


def debug_data_manager():
    "debug data manager"
    data_manager = PersistentDataManager()
    PersistentDataManager().save()
    result = data_manager.data
    result = data_manager.print()
    result = data_manager.get("game_mode")
    print(f"result={result}")
