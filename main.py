"""Module that starts the hud editor code"""

# ====================================================================================================
#     Information
# ====================================================================================================

# ====================================================================================================
#     Imports
# ====================================================================================================

import os

# these lines prevent python from running without console with pythonw
from loguru import logger as logger
from shared_utils.functions import loguru_setup_logging_filter

from src.utils.functions import run_startup_checks_and_actions, show_start_gui

# from packages.game.game import Game
# from packages.utils.functions import load_data

# ====================================================================================================
#     Auto-execute
# ====================================================================================================


print(f"Logger instance before setup: {type(logger)}")
loguru_setup_logging_filter("DEBUG", "include", ["shared_managers.hwnd_manager"])


run_startup_checks_and_actions()
show_start_gui()
