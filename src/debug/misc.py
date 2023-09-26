"""Debug"""
# pylint: disable=unused-import, unused-variable, unnecessary-pass
import os
import sys

from loguru import logger

from debug.game import debug_game_set_states_synced_and_installed
from debug.hotkeys import enable_debug_hotkeys
from debug.hud import get_hud_debug_instance
from src.utils.constants import DATA_MANAGER
from shared_utils.functions import loguru_setup_logging_filter

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
    # loguru_setup_logging_filter("INFO")
    loguru_setup_logging_filter("DEBUG")
    
    # filter_modules = ["compiler.compiler"]
    # loguru_setup_logging_filter("DEBUG", "include", filter_modules)
    
    logger.debug("Configured debug logging")


# Debugging function with variable parameters
def debug_function_variable_params(*args):
    """Debug"""
    print(f"debug_function args={args}")
