"""Debug"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name

import logging
import sys

from loguru import logger

from debug.editor_menu import main_debug_editor_menu
from debug.game import main_debug_game
from debug.gui import main_debug_gui
from debug.misc import main_misc_debug, setup_debugging_environment
from shared_utils.shared_utils import show_message
from tests.test_hud_syncer import unit_test_hud_syncer


def main_debug():
    "Main debug function"

    setup_debugging_environment()

    # unit_test_hud_syncer()
    # main_misc_debug()
    # main_debug_gui()
    # main_debug_editor_menu()
    # debug_vpk_class()
    # debug_id_handler()
    # main_debug_game()

    input("Finished debugging! Press enter to exit...")
