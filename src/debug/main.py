"""Module for debugging"""
# pylint: disable=unused-import, unused-variable, unused-argument, undefined-variable

import os

import vdf  # type: ignore

from debug.game import debug_game_class
from debug.hud import get_hud_debug_instance
from gui import descriptions
from gui.browser import GuiHudBrowser
from gui.popup import GuiEditorMenuPopupContextmenu
from gui.start import GuiHudStart, show_start_gui
from hud.hud import Hud
from utils.constants import DEVELOPMENT_DIR
from utils.functions import load_data
from utils.shared_utils import is_subdirectory
from utils.vdf import debug_vdf_class


def debug_main():
    "Main debug func"
    os.system("cls")  # clear terminal
    print("debug_main")
    persistent_data = load_data()

    debug_game_class(persistent_data)
    # debug_gui(persistent_data)

    # hud = get_hud_debug_instance(persistent_data)
    # result = hud.get_all_files_dict()
    # result = hud.get_files_dict()

    # show_start_gui(persistent_data)
    # debug_vdf_class()

    # vdf_path = os.path.join(
    #     DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    # )
    # vdf_obj = vdf.load(open(vdf_path, encoding="utf-8"))

    # # Iterate through each control and increase the "xpos" value
    # for controls in vdf_obj.values():
    #     print(f"controls={controls}")

    #     for control in controls:
    #         print(f"control={control}")

    #         for key in controls[control]:
    #             print(f"key={key}")

    #             if "xpos" in key:
    #                 print("modifying xpos")
    #                 try:
    #                     # current_xpos = int(control["xpos"])
    #                     current_xpos = int(controls[control][key])
    #                     increased_xpos = current_xpos + 100  # Increase by 100 units
    #                     controls[control][key] = str(increased_xpos)
    #                 except ValueError:
    #                     print(f"Error for: {control}")
    #                     pass  # Skip if "xpos" is not a valid integer
    #             # print(f"this is a test335: {vdf.dumps(control, pretty=True)}")

    # # vdf.dump(video_settings, f_handle, pretty=True)
    # result = vdf.dumps(vdf_obj, pretty=True)
    # # print(vdf_obj.values())
    # print(f"result={result}")

    input("Finished debugging! Press enter to continue..")


def debug_gui(persistent_data):
    "debug gui"

    # descriptions
    # descriptions_gui = descriptions.GuiHudDescriptions(persistent_data, "scripts\\hudlayout.res")
    # descriptions_gui.run()

    # start
    # show_start_gui(persistent_data)

    # browser
    # browse = get_debug_gui_browser_instance(persistent_data)
    # browse.run()

    # editor menu gui
    # my_editor_menu_gui = GuiEditorMenuPopupContextmenu(persistent_data)
    # my_editor_menu_gui.run()
    # my_editor_menu_gui.show()


def get_debug_gui_browser_instance(persistent_data):
    "debug_gui_browser"
    print("debug_browser")
    hud_inc = get_hud_debug_instance(persistent_data)  # set active debug hud to load files into browser

    return GuiHudBrowser(persistent_data)
