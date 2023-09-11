"""Debug"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name

import logging
import sys

from loguru import logger

from debug.editor_menu import main_debug_editor_menu
from debug.game import main_debug_game
from debug.gui import main_debug_gui
from debug.misc import main_misc_debug, setup_debugging_environment
from tests.test_hud_syncer import unit_test_hud_syncer

# from shared_utils.functions import show_message


def main_debug():
    "Main debug function"

    setup_debugging_environment()

    # show_message("msg")

    # verify_directory
    # unit_test_hud_syncer()
    # main_misc_debug()
    main_debug_gui()
    # main_debug_editor_menu()
    # debug_vpk_class()
    # debug_id_handler()
    # main_debug_game()

    input("Finished debugging! Press enter to exit...")
