# pylint: disable=unused-variable, missing-module-docstring, missing-function-docstring, line-too-long
import os
import shutil

from debug.hud import get_hud_debug_instance
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.vdf import VDFModifierGUI
from utils.constants import DEVELOPMENT_DIR
from utils.functions import get_backup_path


def get_debug_gui_browser_instance(persistent_data):
    "debug_gui_browser"
    print("debug_browser")
    hud_inc = get_hud_debug_instance(persistent_data)  # set active debug hud to load files into browser

    return GuiHudBrowser(persistent_data)


def debug_descriptions_gui(persistent_data):
    descriptions_gui = descriptions.GuiHudDescriptions(
        persistent_data, get_debug_gui_browser_instance(persistent_data)
    )
    descriptions_gui.load_file("scripts\\hudlayout.res")
    # descriptions_gui.hud.desc.remove_entry("scripts\\custom_hudlayout.res")
    # descriptions_gui.load_file("scripts\\custom_hudlayout.res")
    descriptions_gui.run()


def debug_vdf_gui(persistent_data):
    """Debug GUI"""

    # vdf file
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )
    # vdf_path = os.path.join(DEVELOPMENT_DIR, "debug", "vdf", "large_scoreboard - [$X360] BackgroundImage Control.res")

    # vdf file backup
    vdf_path_backup = get_backup_path(vdf_path)
    shutil.copy2(vdf_path, vdf_path_backup)

    app = VDFModifierGUI(persistent_data, vdf_path_backup)
    app.run()
