import tkinter as tk
import traceback
import subprocess
import psutil
import os
# if __name__ == '__main__':
#     from Constants import *
#     from Functions import *
#     from Class_Installer import *
# else:
#     from .Constants import *
#     from .Functions import *
#     from .Class_Installer import *
from Constants import *
from Functions import *
from Class_Installer import *

class Game:
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
        return self.game_title

    def get_exe(self):
        return self.game_exe

    def get_appid(self):
        return self.game_appid

    def close(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == self.get_exe():
                proc.kill()
        # print('close() game force closed')
    
    def run(self, type):
        match type:
            case "user":
                if not self.installer.is_installed(type):
                    raise Exception("User installation not found")
            case "dev":
                if not self.installer.is_installed(type):
                    if DEBUG_MODE:
                        self.installer.run()
                    else:
                        # if installation failed, show a message box & quit the script
                        try:
                            self.installer.run()
                        except Exception as e:
                            # display the error message in a message box
                            tk.messagebox.showerror("Error", str(e) + "\n\n" + traceback.format_exc())
                        quit()
            case _:
                ValueError("Invalid type parameter")

        # run the game through steam to prevent steam issues
        game_args = f"-applaunch {str(self.get_appid())}"
        game_args += " -novid" # skip intro videos
        game_args += " -console" # enable developer console

        steam_exe = self.steam_info.get("steam_exe") 

        # Run the command without waiting for it to finish
        subprocess.Popen('"' + steam_exe + '" ' + game_args, shell=True)


if __name__ == '__main__':
    os.system("cls")  # clear terminal
    
    
    PERSISTENT_DATA = load_data()
    game_debug_instance = Game(PERSISTENT_DATA)
    # result = game_debug_instance._get_install_dir("dev")
    # result = game_debug_instance._get_active_dir()
    
