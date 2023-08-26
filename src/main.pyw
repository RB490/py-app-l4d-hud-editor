"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os
from utils.functions import perform_checks_before_starting_program

from utils.persistent_data import PersistentDataManager

# from packages.game.game import Game
# from packages.utils.functions import load_data

os.system("cls")  # clear terminal

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

# ----------------------------------
#     Load persistent data
# ----------------------------------

data_manager = PersistentDataManager()

# ----------------------------------
#     Do stuff
# ----------------------------------

perform_checks_before_starting_program()

# create initial singleton game class
# game_instance = Game(persistent_data)
# hud_instance = Hud(game_instance)
# hud_select = GuiHudSelect(persistent_data, game_instance, hud_instance)

# ----------------------------------
#     Finish
# ----------------------------------

input("End of auto-execute (Press enter to exit)...")
