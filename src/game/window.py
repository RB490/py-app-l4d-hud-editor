# pylint: disable=broad-exception-caught, c-extension-no-member
"Game class window methods"
# pylint: disable=protected-access, broad-exception-raised
import subprocess

import win32gui

from game.constants import InstallationState
from shared_utils.hwnd_window_manager import HwndWindowUtils
from shared_utils.shared_utils import show_message
from utils.constants import GAME_POSITIONS
from utils.persistent_data_manager import PersistentDataManager


class GameWindow:
    "Game class window methods"

    def __init__(self, game_class):
        self.game = game_class
        self.data_manager = PersistentDataManager()
        self.hwnd_utils = HwndWindowUtils()

        self.hwnd = None
        self.exe = "left4dead2.exe"

    def get_exe(self):
        """Retrieve information"""
        return self.exe

    def get_hwnd(self):
        """Retrieve information"""

        if self.hwnd is None or not self.hwnd_utils.running(self.hwnd):
            self.__set_hwnd()

        if not self.hwnd:
            print("No window handle to get!")
        else:
            # print(f"Get {self.get_exe()} hwnd '{self.hwnd}'")
            return self.hwnd

    def __set_hwnd(self, hwnd=None):
        """Retrieve game hwnd"""
        if hwnd is not None:
            self.hwnd = hwnd
            print(f"Set hwnd to '{self.hwnd}'")
            return self.hwnd
        try:
            # retrieve hwnd
            self.hwnd = self.hwnd_utils.get_hwnd_from_executable(self.get_exe())
            if not self.hwnd:
                raise Exception("Could not set window handle!")
            else:
                print(f"Set {self.get_exe()} hwnd '{self.hwnd}'")
                return self.hwnd
        except Exception as err_info:
            print(f"An error occurred retrieving window handle: {err_info}")
            return False

    def restore_saved_position(self):
        "Restore saved position"
        self.set_position(self.data_manager.get("game_pos"))

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
            self.data_manager.set("game_pos", "Custom (Save)")
            self.data_manager.set("game_pos_custom_coord", custom_position_tuple)

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
        self.data_manager.set("game_pos", position)

        if "custom" in position.lower():
            # restore
            custom_position_tuple = self.data_manager.get("game_pos_custom_coord")
            custom_position_tuple = tuple(custom_position_tuple)  # load it back into a tuple to work with the coords
            if (  # verify tuple legitimacy
                isinstance(custom_position_tuple, tuple)
                and len(custom_position_tuple) == 2
                and all(isinstance(i, int) and i >= 0 for i in custom_position_tuple)
            ):
                position = custom_position_tuple
            else:
                raise ValueError(f"Invalid custom_position_tuple: {custom_position_tuple}")

        # move game
        self.hwnd_utils.move(self.game.window.get_hwnd(), position)

    def run(self, dir_mode, write_config=True):
        """Start the game
        'write_config' param is used by installation when rebuilding audio so valve.rc doesnt get overwritten"""

        self.game._validate_dir_mode(dir_mode)

        print(f"directory mode: {dir_mode.name}")

        # confirm dir mode isn't being deleted
        if self.game.dir.id.get_installation_state(dir_mode) == InstallationState.PENDING_DELETION:
            show_message(f"{dir_mode} is partially deleted!\n\nRe-install before running", "error")
            return False

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

        result = subprocess.Popen(
            steam_command,
            shell=True,
            creationflags=subprocess.DETACHED_PROCESS,
            start_new_session=True,  # Required for some platforms
        )
        if not result:
            print("Unable to run game!")
            return False

        # wait for game to fully open
        hwnd = self.hwnd_utils.wait_for_process_with_ram_threshold_and_timeout_to_get_hwnd(
            self.get_exe(), 100, 80
        )  # account for steam starting up

        # set hwnd
        if hwnd:
            self.__set_hwnd(hwnd)
            self.restore_saved_position()
            return True
        else:
            return False

    def is_running(self):
        """Checks if the game is running"""
        return self.hwnd_utils.running(self.get_hwnd())
