"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
import os
import ctypes
import vdf

# import pydirectinput
from modules.utils.functions import get_steam_info


class GameCommands:
    """Sub class of the game class

    Everything related to sending the game commands such as
    - Sending direct console commands
    - Taking 'custom' input such as 'reloadFonts' or 'giveAllItems' and executing the correlating cmds"""

    def __init__(self, persistent_data, game_class):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.game = game_class

    def execute(self, input_command):
        """Execute game commands"""
        output_command = self._get_mapped_command(input_command.lower())

        # write command to file
        command_file = os.path.join(self.game.get_main_dir("dev"), "cfg", "hud_editor_command.cfg")
        with open(command_file, "w", encoding="utf-8") as file_handle:
            file_handle.write(output_command)

        self._send_f11_in_background()

        print(f"Executed command '{input_command}'")

    def _send_f11_in_background(self):
        """
        Sends an F11 key press to the game window using the Windows API.

        Key scancodes: https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
        Keyup scancode: https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-keyup
        Keydown scancode: https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-keydown
        """
        key_scancode = 0x57
        wm_keydown = 0x100
        wm_keyup = 0x101
        wm_keydown_param = key_scancode << 16 | 1
        wm_keyup_param = key_scancode << 16 | 1 | 0x20000000

        hwnd = self.game.get_hwnd()
        ctypes.windll.user32.SendMessageW(hwnd, wm_keydown, 0, wm_keydown_param)
        ctypes.windll.user32.SendMessageW(hwnd, wm_keyup, 0, wm_keyup_param)

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
            video_settings["VideoConfig"]["setting.fullscreen"] = 0
            vdf.dump(video_settings, open(video_settings_path, "w", encoding="utf-8"), pretty=True)

            width = video_settings["VideoConfig"]["setting.defaultres"]
            height = video_settings["VideoConfig"]["setting.defaultresheight"]
            has_border = video_settings["VideoConfig"]["setting.nowindowborder"]
            is_fullscreen = video_settings["VideoConfig"]["setting.fullscreen"]
            # toggle windowMode to conform to the mat_setvideo command; video.txt file saves windowed mode as 0
            # and fullscreen as 1. so the exact opposite as mat_setvideomode
            is_fullscreen = not is_fullscreen
        else:
            # use default video settings
            width = 1920
            height = 1080
            has_border = 1
            is_fullscreen = 1  # 1=windowed

        # resize the game
        output = f"mat_setvideomode 1 1 {int(is_fullscreen)} {int(has_border)}"

        # restore the original settings
        output += f";mat_setvideomode {width} {height} {int(is_fullscreen)} {int(has_border)}"

        return output
