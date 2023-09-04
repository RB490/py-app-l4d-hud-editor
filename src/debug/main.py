"""Debug"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name

import logging
import sys

from loguru import logger

from debug.editor_menu import main_debug_editor_menu
from debug.game import main_debug_game
from debug.gui import main_debug_gui
from debug.misc import main_misc_debug, setup_debugging_environment
from debug.vpk import debug_vpk_class




def main_debug():
    "Main debug function"

    setup_debugging_environment()

    main_debug_gui()
    # main_misc_debug()
    # main_debug_editor_menu()
    # debug_vpk_class()

    # this is for debugging duplicate print messages
    # logger.debug("some debug print statement in main_debug() #1")
    # main_debug_game()
    # logger.debug("some debug print statement in main_debug() #2")
    input("Finished debugging! Press enter to exit...")
