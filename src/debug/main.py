"""Debug"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name

import logging

from debug.editor_menu import main_debug_editor_menu
from debug.game import main_debug_game
from debug.gui import main_debug_gui
from debug.misc import main_misc_debug, setup_debugging_environment
from debug.vpk import debug_vpk_class
from shared_utils.logging_manager import get_logger

logger = get_logger(__name__, log_level=logging.DEBUG)


def main_debug():
    "Main debug function"
    setup_debugging_environment()

    # main_misc_debug()
    # main_debug_editor_menu()
    # main_debug_gui()
    # debug_vpk_class()
    
    # this is for debugging duplicate print messages
    # logger.debug("some debug print statement in main_debug() #1")
    main_debug_game()
    # logger.debug("some debug print statement in main_debug() #2")
    input("Finished debugging! Press enter to exit...")
