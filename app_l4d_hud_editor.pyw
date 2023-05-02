"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os
import atexit
from modules.classes.game import Game
from modules.classes.gui_hud_select import GuiHudSelect
from modules.classes.hud import Hud
from modules.utils.functions import load_data, save_data_on_exit

os.system("cls")  # clear terminal

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

# ----------------------------------
#     Load persistent data
# ----------------------------------

persistent_data = load_data()

# Register the save_data_on_exit function to be called when the script exits
atexit.register(save_data_on_exit, persistent_data)

# ----------------------------------
#     Do stuff
# ----------------------------------

game_instance = Game(persistent_data)
hud_instance = Hud(game_instance)
hud_select = GuiHudSelect(persistent_data, game_instance, hud_instance)

# ----------------------------------
#     Finish
# ----------------------------------

input("End of auto-execute (Press enter to exit)")
