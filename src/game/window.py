# pylint: disable=broad-exception-caught, c-extension-no-member
"Game class window methods"
# pylint: disable=protected-access, broad-exception-raised
import subprocess

import win32gui

from utils.constants import GAME_POSITIONS
from utils.functions import (
    get_hwnd_for_exe,
    is_process_running,
    is_valid_window,
    wait_for_process_with_ram_threshold,
)
from utils.shared_utils import move_hwnd_to_position


class GameWindow:
    "Game class window methods"

    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data

        self.hwnd = None
        self.exe = "left4dead2.exe"

    def get_exe(self):
        """Retrieve information"""
        return self.exe

    def get_hwnd(self):
        """Retrieve information"""

        if self.hwnd is None or not is_valid_window(self.hwnd):
            self.__set_hwnd()

        if not self.hwnd:
            print("No window handle to get!")
        else:
            print(f"Get {self.get_exe()} hwnd '{self.hwnd}'")
            return self.hwnd

    def restore_saved_position(self):
        "Restore saved position"
        self.set_position(self.persistent_data["game_pos"])

    def save_position(self):
        "Save custom position"
        # pylint: disable=unused-variable
        # Save custom location
        game_hwnd = self.game.window.get_hwnd()
        if game_hwnd:
            left, top, right, bottom = win32gui.GetWindowRect(game_hwnd)
            x_coordinate = left
            y_coordinate = top
            custom_position_tuple = (x_coordinate, y_coordinate)

            # Store the custom coordinate tuple in the persistent data dictionary
            self.persistent_data["game_pos"] = "Custom (Save)"
            self.persistent_data["game_pos_custom_coord"] = custom_position_tuple

            print("Stored Custom Position Tuple:", custom_position_tuple)
            return custom_position_tuple
        else:
            return None

    def set_position(self, position):
        """Move window to position"""
        # pylint: disable=c-extension-no-member
        if position not in GAME_POSITIONS:
            raise Exception("Invalid position")

        # save position
        self.persistent_data["game_pos"] = position

        if "custom" in position.lower():
            # Use custom location
            print("Restoring position:", position)

            # restore
            custom_position_tuple = self.persistent_data.get("game_pos_custom_coord")
            if (  # verify tuple legitimacy
                isinstance(custom_position_tuple, tuple)
                and len(custom_position_tuple) == 2
                and all(isinstance(i, int) and i >= 0 for i in custom_position_tuple)
            ):
                position = custom_position_tuple

        # move game
        move_hwnd_to_position(self.game.window.get_hwnd(), position)

    def __set_hwnd(self, timeout_seconds=0):
        """Retrieve game hwnd"""

        # exception because we need the window handle
        try:
            # wait until game is running
            wait_for_process_with_ram_threshold(self.get_exe(), timeout_seconds)

            # retrieve hwnd
            self.hwnd = get_hwnd_for_exe(self.get_exe())
            if not self.hwnd:
                raise Exception("Could not set window handle!")
            else:
                print(f"Set {self.get_exe()} hwnd '{self.hwnd}'")
                return self.hwnd
        except Exception as err_info:
            print(f"An error occurred retrieving window handle: {err_info}")
            return False

    def run(self, dir_mode, write_config=True):
        """Start game

        write_config is used by installation when rebuilding audio so valve.rc doesnt get overwritten"""

        self.game._validate_dir_mode(dir_mode)

        print(f"directory mode: {dir_mode.name}")

        # activate selected dir_mode
        result = self.game.dir.set(dir_mode)
        if not result:
            return False

        # run game
        if self.is_running():
            self.__set_hwnd()
            self.restore_saved_position()
            return True

        # setup
        self.game._disable_addons()
        if write_config:
            self.game._write_config()

        # build game argument params
        game_args = ["-novid", "-console"]  # novid=Skip intro videos  # consoleEnable developer console

        # run the game through steam to prevent steam issues
        steam_args = f"-applaunch {str(self.game.get_app_id())}"
        steam_exe = self.game.steam.get_exe_path()
        steam_command = f'"{steam_exe}" {steam_args} {" ".join(game_args)}'
        subprocess.Popen(steam_command, shell=False)

        # set hwnd
        self.__set_hwnd(20)

        # set position
        self.restore_saved_position()

        return True

    def is_running(self):
        """Checks if the game is running"""
        return is_process_running(self.get_exe())
