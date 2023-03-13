"""Module providing functions related to the game. such as running and installation the dev/user versions"""
import os
import sys
import tkinter as tk
import traceback
import subprocess
import psutil
from include_modules.class_installer import Installer
from include_modules.constants import DEBUG_MODE
from include_modules.functions import get_steam_info
from include_modules.functions import load_data


class Game:
    """Class with functions related to the game. such as running and installation the dev/user versions"""

    def __init__(self, persistent_data):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.installer = Installer(self.persistent_data, self)

        self.game_title = "Left 4 Dead 2"
        self.game_exe = "left4dead2.exe"
        self.game_appid = 550

        # set metadata
        # self.active_exe = os.path.join(self.active_dir, self.game_exe)
        # print(self.active_exe)
        # self.run("user")
        # input('press enter to force close game')
        # self.close()
        # self.run("dev")

    def get_title(self):
        """Retrieve information"""
        return self.game_title

    def get_exe(self):
        """Retrieve information"""
        return self.game_exe

    def get_appid(self):
        """Retrieve information"""
        return self.game_appid

    def get_dir(self, mode):
        """Retrieve information"""
        return self.installer.get_dir(mode)

    def get_main_dir(self, mode):
        """Retrieve information"""
        return self.installer.get_main_dir(mode)

    def activate_mode(self, mode):
        """Switch between user/dev modes"""
        return self.installer.activate_mode(mode)

    def close(self):
        """Close game"""
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] == self.get_exe():
                proc.kill()
        # print('close() game force closed')

    def run(self, mode, wait_on_close=False):
        """Start game"""
        match mode:
            case "user":
                if not self.installer.is_installed(mode):
                    raise AssertionError("User installation not found")
            case "dev":
                if not self.installer.is_installed(mode):
                    if DEBUG_MODE:
                        self.installer.run_installer()
                    else:
                        # if installation failed, show a message box & quit the script
                        try:
                            self.installer.run_installer()
                        except RuntimeError as error_info:
                            # display the error message in a message box
                            tk.messagebox.showerror("Error", str(error_info) + "\n\n" + traceback.format_exc())
                        sys.exit()
            case _:
                raise ValueError("Invalid type parameter")

        game_args = " -novid"  # skip intro videos
        game_args += " -console"  # enable developer console

        if wait_on_close:
            # Run without waiting (opening through steam means code would not connect to left4dead2.exe)
            exe_path = os.path.join(self.get_dir("dev"), self.game_exe)
            subprocess.run('"' + exe_path + '"' + game_args, shell=True, check=False)
        else:
            # run the game through steam to prevent steam issues
            steam_args = f" -applaunch {str(self.get_appid())}"
            steam_exe = self.steam_info.get("steam_exe")
            subprocess.Popen('"' + steam_exe + '"' + steam_args + game_args, shell=True)


def debug_game_class():
    """Debug the class"""
    os.system("cls")  # clear terminal

    saved_data = load_data()
    game_debug_instance = Game(saved_data)
    game_debug_instance = Game(saved_data)
    result = game_debug_instance.get_title()
    print(result)

    input("end of class_game autoexecute")
