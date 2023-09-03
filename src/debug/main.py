"""Debug"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name

from debug.editor_menu import main_debug_editor_menu
from debug.gui import main_debug_gui
from debug.misc import setup_debugging_environment
from debug.vpk import debug_vpk_class


def main_debug():
    "Main debug function"
    setup_debugging_environment()
    # main_misc_debug()
    # main_debug_editor_menu()
    main_debug_gui()
    # debug_vpk_class()
    input("Finished debugging! Press enter to exit...")
