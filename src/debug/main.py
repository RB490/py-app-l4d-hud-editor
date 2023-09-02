# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable, invalid-name

from debug.gui import main_debug_gui
from debug.misc import main_misc_debug


def main_debug():
    "Main debug function"
    main_misc_debug()
    # main_debug_gui()
    input("Finished debugging! Press enter to exit...")
