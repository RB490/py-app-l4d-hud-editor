# pylint: disable=protected-access
"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
import ctypes
import os
import time

import pyautogui
import win32api
import win32con
import win32gui

from game.constants import DirectoryMode
from game.video_settings_modifier import VideoSettingsModifier
from utils.constants import HOTKEY_EXECUTE_AUTOEXEC, KEY_MAP, KEY_SCANCODES
from utils.functions import click_at, focus_hwnd
from utils.persistent_data import PersistentDataManager


class GameCommands:
    """Sub class of the game class

    Everything related to sending the game commands such as
    - Sending direct console commands
    - Taking 'custom' input such as 'reloadFonts' or 'giveAllItems' and executing the correlating cmds"""

    def __init__(self, game_class):
        self.game = game_class
        self.data_manager = PersistentDataManager()

        self.show_ui_panel = None
        self.previous_ui_panel = None
        self.is_inspect_hud_enabled = False

    def execute(self, input_command):
        """Execute game commands"""
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
        if self.previous_ui_panel in ["team", "info"]:
            self.send_keys_in_foreground(["alt", "f4"])

        # toggle inspect hud (vgui_drawtree)
        if self.is_inspect_hud_enabled:
            self.send_keys_in_foreground(["alt", "f4"])
            output_command += "; vgui_drawtree 1; wait; "

        # execute command
        self.send_keys_in_background([HOTKEY_EXECUTE_AUTOEXEC])
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

    def _get_mapped_command(self, input_command):
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

    def send_keys_in_foreground(self, keys):
        # pylint: disable=c-extension-no-member
        """
        Send specified keys to game

        Notes:
            This works in menus, but not ingame. For example:
            - Alt+F4 is detected great for closing vgui_drawtree
            - Chat detects these keypresses. Also while in the 'escape' ingame main menu
            - Normal commands like executing something bound to 'o' don't get detected
        """
        # Get window handle
        game_hwnd = self.game.window.get_hwnd()

        # Check if the window handle is valid
        if not win32gui.IsWindow(game_hwnd):
            return

        # Save the handle of the currently focused window
        focused_hwnd = win32gui.GetForegroundWindow()

        focus_hwnd(game_hwnd)
        for key in keys:
            win32api.keybd_event(KEY_MAP[key.lower()], 0, 0, 0)
            # print(f"Holding down key: {KEY_MAP[key.lower()]}")
        for key in reversed(keys):
            win32api.keybd_event(KEY_MAP[key.lower()], 0, win32con.KEYEVENTF_KEYUP, 0)
            # print(f"Releasing key: {KEY_MAP[key.lower()]}")

        # Restore focus to the previously focused window
        if game_hwnd is not focused_hwnd:
            focus_hwnd(focused_hwnd)

    def send_keys_in_background(self, keys):
        # pylint: disable=c-extension-no-member
        """
        Sends one or more key presses to the game window using the Windows API.

        Notes:
            This works ingame, but not in menus. For example:
            - Sending alt+f4 to close vgui_drawtree 1 doesn't work
            - Sending 'space' to jump does work

        Sources:
        - Key scancodes: https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
        - Keyup scancode: https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-keyup
        - Keydown scancode: https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-keydown
        """

        # Get window handle
        hwnd = self.game.window.get_hwnd()

        # Check if the window handle is valid
        if not win32gui.IsWindow(hwnd):
            return

        wm_keydown = 0x100
        wm_keyup = 0x101

        for key in keys:
            scancode = KEY_SCANCODES[key.lower()]
            keydown_param = scancode << 16 | 1
            ctypes.windll.user32.SendMessageW(hwnd, wm_keydown, 0, keydown_param)
        for key in reversed(keys):
            scancode = KEY_SCANCODES[key.lower()]
            keyup_param = scancode << 16 | 1 | 0x20000000
            ctypes.windll.user32.SendMessageW(hwnd, wm_keyup, 0, keyup_param)
