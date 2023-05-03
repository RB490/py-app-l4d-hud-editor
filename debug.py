"""Module for debugging"""
# pylint: disable=unused-import
import os
from modules.classes.gui_editor_menu import debug_gui_editor_menu
from modules.classes.hud import debug_hud
from modules.classes.hud_descriptions import debug_hud_descriptions

os.system("cls")  # clear terminal
# debug_hud()
debug_gui_editor_menu()
# debug_hud_browser()
# debug_hud_descriptions()
input("Finished! Press enter to continue..")
