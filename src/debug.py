"""Module for debugging"""
# pylint: disable=unused-import

import os
import sys

from game.game import Game
from game.manager import DirectoryMode
from gui.browser import get_debug_gui_browser_instance
from gui.start import GuiHudStart, debug_gui_start
from hud.hud import debug_hud
from utils.constants import EDITOR_AUTOEXEC_PATH, PROJECT_ROOT, SCRIPT_DIR
from utils.functions import get_steam_info, load_data
from utils.shared_utils import show_message

os.system("cls")  # clear terminal


# setup classes
persistent_data = load_data()
# create initial singleton game class
# debug_hud()
game_instance = Game(persistent_data)
steam_info = get_steam_info(persistent_data)
DIR_MODE = "dev"
# installation_id_file = game_instance.manager.get_id_file_name(DIR_MODE)
# result = game_instance.manager.set_directory_manually(DirectoryMode.DEVELOPER)

# result = game_instance.manager.get_main_dir(DirectoryMode.USER)
# result = game_instance.manager.get_cfg_dir(DirectoryMode.DEVELOPER)
# result = game_instance.manager.activate_mode(DirectoryMode.DEVELOPER)
# result = game_instance.manager.activate_mode(DirectoryMode.USER)
# result = game_instance.manager.get_installation_state(DirectoryMode.DEVELOPER)
result = game_instance.manager.run_installer(manually_select_dir=False)
print(f"result={result}")


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
