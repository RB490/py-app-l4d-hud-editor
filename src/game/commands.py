# pylint: disable=protected-access, c-extension-no-member
"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
import ctypes
import os
import time

import pyautogui
import win32api
import win32con
import win32gui
from shared_managers.hwnd_manager import HwndManager

from src.game.constants import DirectoryMode
from src.game.video_settings_modifier import VideoSettingsModifier
from src.utils.constants import DATA_MANAGER, HOTKEY_EXECUTE_AUTOEXEC, KEY_MAP, KEY_SCANCODES
from src.utils.functions import click_at


class GameCommands:
    """Sub class of the game class

    Everything related to sending the game commands such as
    - Sending direct console commands
    - Taking 'custom' input such as 'reloadFonts' or 'giveAllItems' and executing the correlating cmds"""

    def __init__(self, game_class):
        self.game = game_class
        self.data_manager = DATA_MANAGER
        self.hwnd_utils = HwndManager()

        self.show_ui_panel = None
        self.previous_ui_panel = None
        self.is_inspect_hud_enabled = False

    def execute(self, input_command):
        """Execute game commands"""

        if not self.game.window.is_running():
            print("Not executing command! Game isn't running.")
            return
        if not input_command:
            raise ValueError("No input command available!")

        # Save the handle of the currently focused window
        focused_hwnd = self.hwnd_utils.save_focus_state()

        output_command = self._get_mapped_command(input_command.lower())

        # re-show ui panel if set
        if self.show_ui_panel and "debug_zombie_panel" in self.show_ui_panel:
            output_command += f"; wait; {self.show_ui_panel}"
        else:
            output_command += f"; wait; showpanel {self.show_ui_panel}"

        # write command to file
        command_file = os.path.join(
            self.game.dir.get_main_dir(DirectoryMode.DEVELOPER), "cfg", "hud_editor_command.cfg"
        )
        with open(command_file, "w", encoding="utf-8") as file_handle:
            file_handle.write(output_command)

        # close ui panel if needed
        game_hwnd = self.game.window.get_hwnd()
        if self.previous_ui_panel in ["team", "info"]:
            self.hwnd_utils.send_keys_in_foreground(game_hwnd, ["alt", "f4"])

        # toggle inspect hud (vgui_drawtree)
        if self.is_inspect_hud_enabled:
            self.hwnd_utils.send_keys_in_foreground(game_hwnd, ["alt", "f4"])
            output_command += "; vgui_drawtree 1; wait; "

        # execute command
        self.hwnd_utils.send_keys_in_background(game_hwnd, [HOTKEY_EXECUTE_AUTOEXEC])
        print(f"Executed command: '{output_command}'")

        # perform mouse clicks
        if self.data_manager.get("reload_mouse_clicks_enabled"):
            click_at(self.data_manager.get("reload_mouse_clicks_coord_1"))
            click_at(self.data_manager.get("reload_mouse_clicks_coord_2"))

        # reopen menu
        if self.data_manager.get("reload_reopen_menu_on_reload"):
            time.sleep(0.25)  # wait until completely finished
            pyautogui.press("esc")
            time.sleep(0.025)  # ensure the key presses are both detected
            pyautogui.press("esc")

        # save previous panel to perform actions
        self.previous_ui_panel = self.show_ui_panel

        # resetore game position
        self.game.window.restore_saved_position()

        # handle commands with 'mat_setvideomode' because the game will take mouse focus
        if "mat_setvideomode" in output_command:
            game_hwnd = self.game.window.get_hwnd()

            if game_hwnd is not focused_hwnd:
                # focus the game first. because else it bugs out and focus will be set correctly to focused_hwnd,
                # but game will still have focus of the mouse.
                self.hwnd_utils.focus(game_hwnd)
                # Restoring the saved focus state
                self.hwnd_utils.restore_focus_state()

    def _get_mapped_command(self, input_command):
        """Map the input command to its corresponding game command."""
        give_all_guns = (
            "give pistol; give pistol_magnum; give autoshotgun; give shotgun_chrome; "
            + "give pumpshotgun; give shotgun_spas; give smg; give smg_mp5; give smg_silenced; "
            + "give rifle_ak47; give rifle_sg552; give rifle; give rifle_m60; give rifle_desert; "
            + "give hunting_rifle; give sniper_military; give sniper_awp; give sniper_scout; "
            + "give weapon_grenade_launcher"
        )
        give_all_melees = (
            "give chainsaw; give frying_pan; give electric_guitar; give katana; " + "give machete; give tonfa"
        )
        give_all_pickups = (
            "give vomitjar; give molotov; give pipe_bomb; "
            + "give first_aid_kit; give defibrilator; give adrenaline; give pain_pills"
        )

        command_map = {
            "reload_hud": "hud_reloadscheme",
            "reload_menu": "ui_reloadscheme",
            "reload_materials": "mat_reloadallmaterials",
            "reload_all": "hud_reloadscheme; ui_reloadscheme; mat_reloadallmaterials; "
            + self._get_reload_fonts_command(),
            "reload_fonts": self._get_reload_fonts_command() + "; hud_reloadscheme; ui_reloadscheme",
            "hide_world": "r_drawWorld 0; r_drawEntities 0",
            "show_world": "r_drawWorld 1; r_drawEntities 1",
            "give_all_items": give_all_guns + "; " + give_all_melees + "; " + give_all_pickups,
            "give_all_guns": give_all_guns,
            "give_all_melees": give_all_melees,
            "give_all_pickups": give_all_pickups,
        }
        return command_map.get(input_command, input_command)

    def _get_reload_fonts_command(self):
        """
        Retrieve the console command for reloading the game fonts.
        This can be done with mat_setvideomode by resizing the game or toggling fullscreen.

        Process:
            1. Get the current video settings
            2. Resize the game to 1 by 1 pixel
            3. Restore original video settings

        Info:
            mat_setvideomode <width> <height> <fullscreen bool, true = windowed> <borderless bool, true = borderless>
            Note: this command doesn't have any effect when the current video settings are identical
        """

        video_settings_modifier = VideoSettingsModifier(
            os.path.join(self.game.dir.get_main_dir(DirectoryMode.DEVELOPER), "cfg")
        )
        video_settings = video_settings_modifier.load_video_settings()

        # retrieve current video settings
        if video_settings is not None:
            video_settings_modifier.set_fullscreen(0)
            width = video_settings_modifier.get_width()
            height = video_settings_modifier.get_height()
            has_border = video_settings_modifier.get_nowindowborder()
            is_fullscreen = 1
        else:
            # use default video settings
            width = 1920
            height = 1080
            has_border = 1
            is_fullscreen = 1

        # resize the game to be really small
        output = f"mat_setvideomode 1 1 {int(is_fullscreen)} {int(has_border)}"

        # restore the specified settings
        output += f";mat_setvideomode {width} {height} {int(is_fullscreen)} {int(has_border)}"

        return output

    def set_inspect_hud(self, status: bool) -> None:
        """Set inspect hud status for usage in the execute method"""
        if status:
            print("HUD inspection enabled.")
            self.is_inspect_hud_enabled = True
        else:
            print("HUD inspection disabled.")
            self.is_inspect_hud_enabled = False
        self.execute("vgui_drawtree 1")

    def set_ui_panel(self, panel):
        """Set & show ui panel for usage in the execute method"""

        # set panel to be shown
        self.show_ui_panel = panel

        print(f"set_ui_panel: {panel}")
