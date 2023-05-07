"""Module for debugging"""
# pylint: disable=unused-import
import os
from modules.classes.game import Game
from modules.classes.gui_editor_menu import debug_gui_editor_menu
from modules.classes.hud import Hud, debug_hud
from modules.classes.hud_descriptions import debug_hud_descriptions
from modules.utils.functions import load_data, retrieve_hud_name_for_dir

os.system("cls")  # clear terminal
persistent_data = load_data()
game_instance = Game(persistent_data)
hud_instance = Hud(game_instance)
# debug_hud()

print(f"Game version: {game_instance.get_version()}")
debug_gui_editor_menu(persistent_data, game_instance, hud_instance)
# hud_dir = "D:\\Programming and projects\\l4d-addons-huds\\4. l4d2-2020HUD\\source"
# hud_name = retrieve_hud_name_for_dir(hud_dir)
# print(hud_name)
# debug_hud_browser()
# debug_hud_descriptions()
input("Finished! Press enter to continue..")
