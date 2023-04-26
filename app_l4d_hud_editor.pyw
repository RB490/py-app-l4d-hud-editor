"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os
import atexit

# pylint: disable=unused-import
from modules.classes.class_hud_select_gui import debug_hud_select_gui

# pylint: disable=unused-import
from modules.classes.class_hud_syncer import debug_hud_syncer

from modules.classes.class_game import Game
from modules.classes.class_installer import Installer
from modules.classes.class_hud_edit import HudEdit
from modules.utils.constants import PERSISTENT_DATA, SCRIPT_NAME
from modules.utils.constants import NEW_HUD_DIR
from modules.utils.functions import load_data, save_data_on_exit

# from modules.class_game import Game

os.system("cls")  # clear terminal

# ====================================================================================================
#     Load persistent data
# ====================================================================================================

PERSISTENT_DATA = load_data()

# Register the save_data_on_exit function to be called when the script exits
atexit.register(save_data_on_exit, PERSISTENT_DATA)

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

game_instance = Game(PERSISTENT_DATA)
installer_instance = Installer(PERSISTENT_DATA, game_instance)
hud_edit = HudEdit(game_instance)

# debug_hud_syncer()
# debug_hud_select_gui(PERSISTENT_DATA, installer_instance)
# installer_instance.run_update_or_repair()
# installer_instance.run_update_or_repair("repair")

hud_edit.finish_editing()

input(f"{SCRIPT_NAME}: End of auto-execute (Press enter to exit)")
