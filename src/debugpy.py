"""Module for debugging"""
# pylint: disable=unused-import

import os
import unittest

from game.dir_id_handler import debug_id_handler
from game.game import debug_game_class
from gui.browser import get_debug_gui_browser_instance
from gui.start import GuiHudStart
from hud.hud import Hud
from tests.test_hud_syncer import TestHudSyncer, debug_hud_syncer

# from hud.syncer_new import debug_new_hud_syncer
from utils.functions import load_data, save_data

os.system("cls")  # clear terminal


persistent_data = load_data()
debug_game_class(persistent_data)

# start_gui = GuiHudStart(persistent_data)
# start_gui.run()

# hud_inc = Hud(persistent_data)

# browse = get_debug_gui_browser_instance(persistent_data)
# browse.run()

# debug_hud_syncer()

input("Finished! Press enter to continue..")
