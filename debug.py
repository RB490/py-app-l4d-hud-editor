"""Module for debugging"""
# pylint: disable=unused-import
import os
from modules.classes.game import Game
from modules.classes.gui_editor_menu import debug_gui_editor_menu
from modules.classes.hud import Hud, debug_hud
from modules.classes.hud_descriptions import debug_hud_descriptions
from modules.utils.functions import load_data

os.system("cls")  # clear terminal
persistent_data = load_data()
game_instance = Game(persistent_data)
hud_instance = Hud(game_instance)
# debug_hud()
debug_gui_editor_menu(persistent_data, game_instance, hud_instance)
# debug_hud_browser()
# debug_hud_descriptions()
input("Finished! Press enter to continue..")
