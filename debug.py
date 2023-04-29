"""Module for debugging"""
import os

# pylint: disable=unused-import
from modules.classes.hud import debug_hud
from modules.classes.hud_descriptions import debug_hud_descriptions

os.system("cls")  # clear terminal
debug_hud()
# debug_hud_browser()
# debug_hud_descriptions()
input("Finished! Press enter to continue..")
