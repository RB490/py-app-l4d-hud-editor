"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os

from shared_utils.functions import loguru_setup_logging_filter

from src.utils.functions import run_startup_checks_and_actions, show_start_gui

# from packages.game.game import Game
# from packages.utils.functions import load_data

# ====================================================================================================
#     Auto-execute
# ====================================================================================================

# these lines prevent python from running without console with pythonw
# loguru_setup_logging_filter("DEBUG", "exclude", ["shared_managers.hwnd_manager"])


run_startup_checks_and_actions()
show_start_gui()
