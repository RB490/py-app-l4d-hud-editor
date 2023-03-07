import shutil
import easygui
# if __name__ == '__main__':
#     from Constants import *
#     from Functions import *
#     from Class_Game import *
# else:
#     from .Constants import *
#     from .Functions import *
#     from .Class_Game import *
from Constants import *
from Functions import *
from Class_Game import *
from Class_VPK import *


class Installer:
    def __init__(self, persistent_data, game_class):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.game = game_class

        self.user_dir_id_file = "user_folder.DoNotDelete"
        self.dev_dir_id_file = "hud_dev_folder.DoNotDelete"

    def get_active_dir(self):
        # find active game directory        
        steam_games_dir = self.steam_info["game_dir"]
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if folder_name == GAME_TITLE:
                break
            else:
                folder_path = None

        # confirm active directory was found
        if folder_path == None:
            raise Exception(f"Could not find any game installation directory")

        return folder_path

    def get_dir(self, mode):
        match mode:
            case "user":
                installation_id_file = self.user_dir_id_file
            case "dev":
                installation_id_file = self.dev_dir_id_file
            case _:
                ValueError("Invalid mode parameter")

        steam_games_dir = self.steam_info["game_dir"]
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                installation_id_file_path = os.path.join(folder_path, installation_id_file)
                if os.path.isfile(installation_id_file_path):
                    return folder_path

        # raise Exception(f"Could not find game installation directory for specified installation mode ({mode})")
        return False

    def activate_mode(self, mode):
        # ensure dev mode is installed
        if not self.is_installed("dev"):
            raise Exception(f"Called activate_mode to activate dev mode without it being installed")
            
        try:
            if mode == "user":
                os.rename(self.get_dir("dev"), os.path.join(self.steam_info.get("game_dir"), "backup_hud_dev." + GAME_TITLE))
                os.rename(self.get_dir("user"), os.path.join(self.steam_info.get("game_dir"), GAME_TITLE))
            elif mode == "dev":
                os.rename(self.get_dir("user"), os.path.join(self.steam_info.get("game_dir"), GAME_TITLE + " User"))
                os.rename(self.get_dir("dev"), os.path.join(self.steam_info.get("game_dir"), GAME_TITLE))
            else:
                raise ValueError("Invalid mode parameter")
        except Exception as e:
            print(f"An error occurred during directory renaming: {e}")

    def is_installed(self, mode):
        # verify mode param
        modes = ['user', 'dev']
        if mode not in modes:
            ValueError("Invalid mode parameter")
        
        # confirm mode is installed by retrieving its dir
        install_dir = self.get_dir(mode)
        if not os.path.isdir(install_dir):
            return False
        
        # confirm this is the correct directory by checking the game's executable
        if os.path.isfile(os.path.join(install_dir, GAME_EXE)):
            return True
        else:
            # raise Exception(f"Game executable not found in game directory: '{install_dir}'")
            return False


    def run_installer(self):
        if DEBUG_MODE:
            if not self._perform_installation():
                raise Exception("Installation cancelled!")
            self.Install(self)
        else:
            try:
                self.Install(self)
            except Exception as e:
                tk.messagebox.showerror("Error", str(e) + "\n\nInstallation cancelled! Currently unhandled. Closing.")
                quit()

    def _perform_installation(self):
        # verify the user installation is available
        if not self.parent.is_installed("user"):
            raise Exception("User installation not found. Unable to install")

        # delete the dev folder for debugging purposes only
        # if DEBUG_MODE and os.path.isdir(self.parent.get_dir("dev")):
        #     self.parent.activate_mode("user")
        #     shutil.rmtree(self.parent.get_dir("dev"))
        #     print('debug mode: successfully deleted the dev folder')

        # close the game
        self.parent.game.close()

        # confirm install start
        # if not self._prompt_install_start():
        #     return False

        # 1. create dev folder template (folder & .exe) for detection incase of cancellation for cleanup
        # self._create_dev_dir()

        # 2. copy the game files into and activate the dev folder
        # self._copy_game_files()
        # print('finished copying files')
        # self.parent.activate_mode("dev")

        # 3. steam verify = prompt to verify game install through steam to update and restore all game files
        # self._prompt_game_verified()

        # 4. extract paks
        # self._extract_paks()
        # self._disable_paks()

        # 5. install mods
        self._install_mods()

        # finish installation
        input('press enter to successfully finish installation')
        return True


    def _prompt_install_start(self):
        title = f"Enable hud editing for {GAME_TITLE}?"
        disk_space = get_dir_size_in_gb(self.parent.get_dir("user"))
        message =   f"Enable hud editing for {GAME_TITLE}?\n\n" \
                    "- This can take up to ~30 minutes depending on drive and processor speed\n" \
                    f"- This will use around {disk_space} of disk space (copy of the game folder)\n" \
                    "- Keep any L4D games closed during this process\n\n" \
                    "It is possible to cancel the setup at any time by closing the progress window"

        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            return True
        elif response == "No":
            return False
        else:
            return False

    def _create_dev_dir(self):
        game_user_dir = self.parent.get_dir("user")
        game_dev_dir = os.path.join(self.parent.steam_info.get("game_dir"), "backup_hud_dev." + GAME_TITLE)
        game_exe_path = os.path.join(game_user_dir, GAME_EXE)
        dev_id_file_path = os.path.join(game_dev_dir, self.parent.dev_dir_id_file)

        os.mkdir(game_dev_dir)
        shutil.copy(game_exe_path, game_dev_dir)
        with open(dev_id_file_path, 'w') as f:
            pass

    def ignore_files(self, dir, files):
        return [name for name in files if name == self.parent.user_dir_id_file]

    def _copy_game_files(self):
        copy_directory_contents(self.parent.get_dir("user"), self.parent.get_dir("dev"), self.parent.user_dir_id_file)

    def _prompt_game_verified(self):
        title = f"Verify integrity of games files for {GAME_TITLE} in steam"
        disk_space = get_dir_size_in_gb(self.parent.get_dir("user"))
        message =   f"Verify integrity of games files for {GAME_TITLE} in steam\n\n" \
                    f"Right-Click {GAME_TITLE} -> Properties -> Local Files -> 'Verify integrity of games files'\n" \
                    "This will not affect your game installation. Only the copy that was just made\n\n" \
                    "Are you sure Steam has finished verifying AND downloaded any missing files?"

        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            pass
        elif response == "No":
            return False
        else:
            return False

        # ask a second time - are you really sure?
        message = f"Are you REALLY sure Steam has finished verifying AND downloaded any missing files for {GAME_TITLE}?"
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            return True
        elif response == "No":
            return False
        else:
            return False

    def _extract_paks(self):
        print('extract paks')
        """
        Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories.
        """
        dev_dir = self.parent.get_dir("dev")
        for filename in os.listdir(dev_dir):
            subdir_path = os.path.join(dev_dir, filename)
            if os.path.isdir(subdir_path):
                for subfilename in os.listdir(subdir_path):
                    if subfilename == "pak01_dir.vpk":
                        filepath = os.path.join(subdir_path, subfilename)
                        # output_dir = os.path.join(subdir_path, "pak01_dir")
                        output_dir = subdir_path
                        vpk_class = VPK(filepath)
                        vpk_class.extract(output_dir)

    def _disable_paks(self):
        dev_dir = self.parent.get_dir("dev")
        for filename in os.listdir(dev_dir):
            subdir_path = os.path.join(dev_dir, filename)
            if os.path.isdir(subdir_path):
                for subfilename in os.listdir(subdir_path):
                    if subfilename == "pak01_dir.vpk":
                        source_filepath = os.path.join(subdir_path, subfilename)
                        target_filepath = os.path.join(subdir_path, subfilename + ".disabled")
                        os.rename(source_filepath, target_filepath)

    def _enable_paks(self):
        dev_dir = self.parent.get_dir("dev")
        for filename in os.listdir(dev_dir):
            subdir_path = os.path.join(dev_dir, filename)
            if os.path.isdir(subdir_path):
                for subfilename in os.listdir(subdir_path):
                    if subfilename == "pak01_dir.vpk.disabled":
                        source_filepath = os.path.join(subdir_path, subfilename)
                        target_filepath = os.path.join(subdir_path, "pak01_dir.vpk")
                        os.rename(source_filepath, target_filepath)

    def _install_mods(self):
        pass


if __name__ == '__main__':
    os.system("cls")  # clear terminal

    PERSISTENT_DATA = load_data()
    game_instance = Game(PERSISTENT_DATA)
    inst = Installer(PERSISTENT_DATA, game_instance)
    inst.run_installer()
    # inst.toggle_dev_mode(True)
