# pylint: disable=unused-variable, missing-module-docstring, missing-function-docstring, line-too-long
import os
import shutil

from debug.hud import get_hud_debug_instance
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.vdf import VDFModifierGUI
from utils.constants import DEVELOPMENT_DIR
from utils.functions import get_backup_path
from utils.get_user_input import get_user_input


def get_debug_gui_browser_instance():
    "debug_gui_browser"
    print("debug_browser")
    hud_inc = get_hud_debug_instance()  # set active debug hud to load files into browser

    return GuiHudBrowser()

def debug_get_user_input():
    def handle_user_input(result):
        """Handle user input"""
        print("User entered:", result)
        # Your code here

    get_user_input("Enter Name", "What is your name?", handle_user_input)

def debug_descriptions_gui():
    descriptions_gui = descriptions.GuiHudDescriptions(get_debug_gui_browser_instance())
    descriptions_gui.load_file("scripts\\hudlayout.res")
    # descriptions_gui.hud.desc.remove_entry("scripts\\custom_hudlayout.res")
    # descriptions_gui.load_file("scripts\\custom_hudlayout.res")
    descriptions_gui.show()


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

    app = VDFModifierGUI(vdf_path_backup)
    app.show()
