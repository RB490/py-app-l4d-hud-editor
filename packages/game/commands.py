"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
import os
import ctypes
import vdf

# import pyautogui
import time
import win32gui
import win32con
import win32api
from pywinauto import Application
from packages.utils.constants import KEY_MAP, KEY_SCANCODES

# import pydirectinput
from packages.utils.functions import get_steam_info


class GameCommands:
    """Sub class of the game class

    Everything related to sending the game commands such as
    - Sending direct console commands
    - Taking 'custom' input such as 'reloadFonts' or 'giveAllItems' and executing the correlating cmds"""

    def __init__(self, persistent_data, game_class):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.game = game_class
        self.show_ui_panel = None
        self.previous_ui_panel = None

    def set_ui_panel(self, panel):
        """Set & show ui panel"""

        # set panel to be shown
        self.show_ui_panel = panel

        print(f"set_ui_panel: {panel}")

    def _send_keys_in_foreground(self, keys):
        # pylint: disable=c-extension-no-member
        """
        Send specified keys to game

        Notes:
            This works in menus, but not ingame. For example:
            - Alt+F4 is detected great for closing vgui_drawtree
            - Chat detects these keypresses. Also while in the 'escape' ingame main menu
            - Normal commands like executing something bound to 'o' don't get detected
        """
        game_hwnd = self.game.get_hwnd()

        # Save the handle of the currently focused window
        focused_hwnd = win32gui.GetForegroundWindow()

        win32gui.SetForegroundWindow(game_hwnd)
        win32gui.BringWindowToTop(game_hwnd)
        for key in keys:
            win32api.keybd_event(KEY_MAP[key.lower()], 0, 0, 0)
            # print(f"Holding down key: {KEY_MAP[key.lower()]}")
        for key in reversed(keys):
            win32api.keybd_event(KEY_MAP[key.lower()], 0, win32con.KEYEVENTF_KEYUP, 0)
            # print(f"Releasing key: {KEY_MAP[key.lower()]}")

        # Restore focus to the previously focused window
        if game_hwnd is not focused_hwnd:
            # use pywinauto to get around SetForegroundWindow error/limitation: https://stackoverflow.com/a/30314197
            # first SetForegroundWindow because pywinauto moves the cursor
            win32gui.SetForegroundWindow(focused_hwnd)
            focused_app = Application().connect(handle=focused_hwnd)
            focused_app.top_window().set_focus()

    def _send_keys_in_background(self, keys):
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

        wm_keydown = 0x100
        wm_keyup = 0x101

        hwnd = self.game.get_hwnd()
        for key in keys:
            scancode = KEY_SCANCODES[key.lower()]
            keydown_param = scancode << 16 | 1
            ctypes.windll.user32.SendMessageW(hwnd, wm_keydown, 0, keydown_param)
        for key in reversed(keys):
            scancode = KEY_SCANCODES[key.lower()]
            keyup_param = scancode << 16 | 1 | 0x20000000
            ctypes.windll.user32.SendMessageW(hwnd, wm_keyup, 0, keyup_param)

    def execute(self, input_command):
        """Execute game commands"""
        output_command = self._get_mapped_command(input_command.lower())

        # re-show ui panel if set
        if self.show_ui_panel and "debug_zombie_panel" in self.show_ui_panel:
            output_command += f"; wait; {self.show_ui_panel}"
        else:
            output_command += f"; wait; showpanel {self.show_ui_panel}"

        # write command to file
        command_file = os.path.join(self.game.get_main_dir("dev"), "cfg", "hud_editor_command.cfg")
        with open(command_file, "w", encoding="utf-8") as file_handle:
            file_handle.write(output_command)

        # close ui panel if needed
        if self.previous_ui_panel in ["team", "info"]:
            self._send_keys_in_foreground(["alt", "f4"])

        # execute command
        self._send_keys_in_background(["f11"])
        print(f"Executed command: '{output_command}'")

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
        video_settings_path = os.path.join(os.path.join(self.game.get_main_dir("dev"), "cfg"), "video.txt")

        # retrieve current video settings
        if os.path.exists(video_settings_path):
            video_settings = vdf.load(open(video_settings_path, encoding="utf-8"))

            has_border = video_settings["VideoConfig"]["setting.nowindowborder"]
            is_fullscreen = video_settings["VideoConfig"]["setting.fullscreen"]

            video_settings["VideoConfig"]["setting.fullscreen"] = 0
            vdf.dump(video_settings, open(video_settings_path, "w", encoding="utf-8"), pretty=True)

            width = video_settings["VideoConfig"]["setting.defaultres"]
            height = video_settings["VideoConfig"]["setting.defaultresheight"]
            has_border = video_settings["VideoConfig"]["setting.nowindowborder"]
            is_fullscreen = video_settings["VideoConfig"]["setting.fullscreen"]
            # toggle windowMode to conform to the mat_setvideo command; video.txt file saves windowed mode as 0
            # and fullscreen as 1. so the exact opposite as mat_setvideomode
            if is_fullscreen == 0:
                is_fullscreen = 1
            elif is_fullscreen == 1:
                is_fullscreen = 0
        else:
            # use default video settings
            width = 1920
            height = 1080
            has_border = 1
            is_fullscreen = 1  # 1=windowed

        # resize the game to be really small
        output = f"mat_setvideomode 1 1 {int(is_fullscreen)} {int(has_border)}"

        # restore the specified settings
        output += f";mat_setvideomode {width} {height} {int(is_fullscreen)} {int(has_border)}"

        return output
