"""Debug"""
# pylint: disable=unused-import, unused-variable, unnecessary-pass
import os
import sys

from loguru import logger

from debug.game import debug_game_set_states_synced_and_installed
from debug.hotkeys import enable_debug_hotkeys
from debug.hud import get_hud_debug_instance
from utils.constants import DATA_MANAGER


def main_misc_debug():
    """Debug"""
    logger.info("This is an info message")
    # get_hud_debug_instance()


def setup_debugging_environment():
    """Debug"""
    print("Setting up debug environment!")

    # Clear the terminal
    os.system("cls")

    # Setup
    configure_debug_logging()
    debug_game_set_states_synced_and_installed()
    enable_debug_hotkeys()


def configure_debug_logging():
    """Configure debug logging"""
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    # logger.add(sys.stderr, level="DEBUG")
    # logger.add(sys.stderr, filter=lambda record: "hud.descriptions" in record["name"], level="DEBUG")
    # logger.add(sys.stderr, filter=lambda record: "game.installer" in record["name"], level="DEBUG")
    # logger.add(sys.stderr, filter=lambda record: "hud.syncer" in record["name"], level="DEBUG")
    # logger.add(sys.stderr, filter=lambda record: "gui.browser" in record["name"], level="DEBUG")
    # logger.add(sys.stderr, filter=lambda record: "gui.start" in record["name"], level="DEBUG")
    # logger.add(sys.stderr, filter=lambda record: "shared_managers.hotkey_manager" in record["name"], level="DEBUG")
    logger.debug("Configured debug logging")


# Debugging function with variable parameters
def debug_function_variable_params(*args):
    """Debug"""
    print(f"debug_function args={args}")
