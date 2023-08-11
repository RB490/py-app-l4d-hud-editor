"""Module for debugging"""
# pylint: disable=unused-import

import os

from packages.game.game import Game
from packages.gui.browser import get_debug_gui_browser_instance
from packages.gui.start import GuiHudStart, debug_gui_start
from packages.hud.hud import debug_hud
from packages.utils.functions import load_data
from packages.utils.shared_utils import show_message

os.system("cls")  # clear terminal


# setup classes
persistent_data = load_data()
# create initial singleton game class
# debug_hud()
# game_instance = Game(persistent_data)
# result = game_instance.manager.run_installer()
# game_instance.activate_mode("dev")
# game_instance.activate_mode("dev")
# print(f'debug: result: {result}')
# result = game_instance.manager._prompt_start("install")
# result = game_instance.manager.get_dir("dev")

# result = game_instance.manager.is_installed("user")

# show_message("some message", "info", "mytitle")

# game_instance2 = Game(persistent_data)
# installer_instance = GameManager(persistent_data, game_instance)
# debug_gui_start(persistent_data)
# debug_gui_start(persistent_data)
# my_browser = get_debug_gui_browser_instance(persistent_data)
# my_browser.run()

# start_instance = GuiHudStart(persistent_data)
# start_instance.destroy_gui()
start_instance = GuiHudStart(persistent_data)
start_instance.run()


input("Finished! Press enter to continue..")
