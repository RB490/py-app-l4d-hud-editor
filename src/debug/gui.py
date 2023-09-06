# pylint: disable=unused-variable, missing-module-docstring, missing-function-docstring, line-too-long, unused-import, unreachable
import os
import random
import shutil
import string
import time
import tkinter as tk

from debug.hud import get_hud_debug_instance
from game.constants import DirectoryMode
from game.game import Game
from gui import descriptions
from gui.about import GuiAbout
from gui.browser import GuiHudBrowser
from gui.popup import GuiEditorMenuPopup
from gui.progress import ProgressGUI
from gui.start import GuiHudStart
from gui.vdf import VDFModifierGUI
from shared_utils.shared_utils import get_invisible_tkinter_root
from shared_utils.splash_gui import splash_gui_example
from utils.constants import DEVELOPMENT_DIR
from utils.functions import get_backup_path, show_start_gui
from utils.get_user_input import get_user_input


def main_debug_gui():
    "debug gui"

    # start
    # show_start_gui()

    # browser
    # debug_browser_gui()  # & also properly editor menu

    # splash
    # splash_gui_example()
    #
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


def debug_about_gui():
    invis_root = get_invisible_tkinter_root()
    gui_about = GuiAbout(invis_root)
    gui_about.show()


def debug_browser_gui():
    "debug_gui_browser"
    print("debug_browser")
    hud_inc = get_hud_debug_instance()  # set active debug hud to load files into browser

    # root = get_invisible_tkinter_root()

    # game_class = Game()
    # game_class.window.run(DirectoryMode.DEVELOPER)

    # browser = GuiHudBrowser(root)
    # browser.show()
    start_instance = GuiHudStart()
    # start_instance.browser.show()
    start_instance.show(hide=True, callback="debug_show_browser_gui")  # start mainloop

    return


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


def debug_progress_gui():
    "debug installer gui"

    # temp
    # total_steps = 1
    # gui = ProgressGUI("Uninstalling", 350, 60, total_steps)  # Create the GUI instance
    # gui.show()
    # return

    total_steps = 150000
    gui = ProgressGUI("Debugging", 250, 60, total_steps)  # Create the GUI instance
    gui.show()

    # gui.update_progress("asdf asdf asdf asdf ")
    # gui.update_progress("asdf asdf asdf asdf ")

    for step in range(total_steps):
        random_length = random.randint(1, 3)
        # random_length = random.randint(1, 10)
        # random_length = random.randint(1, 100)
        # random_length = random.randint(1, 500)
        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=random_length))
        # gui.update_progress(f"step: {step + 1}: ..\\j3BVF1P\\left4dead2 {random_string}")
        gui.update_progress(f"{random_string*10}")
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

    root = get_invisible_tkinter_root()
    app = VDFModifierGUI(root, vdf_path_backup)
    app.show()
