# pylint: disable=unused-variable, missing-module-docstring, missing-function-docstring, line-too-long, unused-import, unreachable
import os
import random
import shutil
import string
import time
import tkinter as tk

from shared_gui.base import example_create_main_and_sub_gui
from shared_gui.progress import ProgressGUI, debug_progress_gui
from shared_gui.splash_gui import splash_gui_example
from shared_utils.functions import get_invisible_tkinter_root

from debug.hud import get_hud_debug_instance
from gui import descriptions
from src.game.constants import DirectoryMode
from src.game.game import Game
from src.gui.about import GuiAbout
from src.gui.browser import GuiHudBrowser
from src.gui.popup import GuiEditorMenuPopup
from src.gui.start import GuiHudStart
from gui.vdf_tool import VDFModifierGUI
from src.utils.constants import DEVELOPMENT_DIR
from src.utils.functions import get_backup_path, show_start_gui
from src.utils.get_user_input import get_user_input


def main_debug_gui():
    "debug gui"

    # start
    show_start_gui()

    # browser
    # debug_browser_gui()  # & also properly editor menu

    # splash
    # splash_gui_example()

    # popup
    # debug_popup_gui()

    # vdf gui
    # debug_vdf_gui()

    # descriptions
    # debug_descriptions_gui()

    # user input (used to retrieve game command)
    # debug_get_user_input()

    # installer
    # debug_progress_gui()

    # about
    # debug_about_gui()

    # basegui
    # example_create_main_and_sub_gui()


def debug_popup_gui():
    """Debug gui class"""
    # pylint: disable=unused-variable
    root = get_invisible_tkinter_root()
    # app = GuiEditorMenuPopup(root)
    app = GuiEditorMenuPopup(root, debug_instantly_show_menu=True)
    app.show(hide=True)
    # app.show(hidden=True)


def debug_get_user_input():
    def handle_user_input(result):
        """Handle user input"""
        print("User entered:", result)
        # Your code here

    get_user_input("Enter Name", "What is your name?", handle_user_input)


def debug_descriptions_gui():
    root = get_invisible_tkinter_root()
    descriptions_gui = descriptions.GuiHudDescriptions(root)
    descriptions_gui.load_file("scripts\\hudlayout.res")
    # descriptions_gui.show()
    # descriptions_gui.hud.desc.remove_entry("custom_hudlayout.res")
    # descriptions_gui.load_file("custom_hudlayout.res")


def debug_vdf_gui():
    """Debug GUI"""

    # vdf file
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )
    # vdf_path = os.path.join(DEVELOPMENT_DIR, "debug", "vdf", "large_scoreboard - [$X360] BackgroundImage Control.res")

    # vdf file backup
    vdf_path_backup = get_backup_path(vdf_path)
    shutil.copy2(vdf_path, vdf_path_backup)

    root = get_invisible_tkinter_root()
    app = VDFModifierGUI(root, vdf_path_backup)
    app.show()
