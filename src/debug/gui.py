# pylint: disable=unused-variable, missing-module-docstring, missing-function-docstring, line-too-long, unused-import
import os
import random
import shutil
import string
import time

from debug.hud import get_hud_debug_instance
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.progress import ProgressGUI
from gui.start import GuiHudStart
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
    descriptions_gui = descriptions.GuiHudDescriptions()
    descriptions_gui.load_file("scripts\\hudlayout.res")
    descriptions_gui.show()
    # descriptions_gui.hud.desc.remove_entry("scripts\\custom_hudlayout.res")
    # descriptions_gui.load_file("scripts\\custom_hudlayout.res")


def debug_start_gui():
    "Show start gui"
    start_instance = GuiHudStart()
    start_instance.show()


def debug_progress_gui():
    "debug installer gui"

    # total_steps = len(installation_steps)
    total_steps = 150000
    gui = ProgressGUI("Debugging", 600, 60, total_steps)  # Create the GUI instance

    # gui.update_progress("asdf asdf asdf asdf ")
    # gui.update_progress("asdf asdf asdf asdf ")

    for step in range(total_steps):
        random_length = random.randint(1, 10)
        # random_length = random.randint(1, 100)
        # random_length = random.randint(1, 500)
        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=random_length))
        gui.update_progress(f"step: {step + 1}: ..\\j3BVF1P\\left4dead2 {random_string}")
        # time.sleep(0.4)
        # time.sleep(2)

    # gui.update_progress("this is!")
    # input("enter to cintieeiej")
    # gui.update_progress(
    #     "this is some text explaining the current stepthis is some text explaining the current stepthis is some text explaining the current step!"
    # )
    # gui.update_progress("this is some text explaining the current step!")


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
