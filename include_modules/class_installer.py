"""This module is a sub class of the game class.
functions related to the game folder such as switching between user/dev modes"""
import os
import shutil
import sys
from tkinter import Tk
from tkinter import filedialog
import easygui
from include_modules.class_vpk import VPK
from include_modules.constants import DEBUG_MODE, MODS_DIR, SCRIPT_NAME
from include_modules.functions import copy_directory_contents, get_dir_size_in_gb, get_steam_info, load_data


class Installer:
    """Sub class of the game class. functions related to the game folder such as switching between user/dev modes"""

    def __init__(self, persistent_data, game_class):
        self.persistent_data = persistent_data
        self.steam_info = get_steam_info(self.persistent_data)
        self.game = game_class

        self.user_dir_id_file = "user_folder.DoNotDelete"
        self.dev_dir_id_file = "hud_dev_folder.DoNotDelete"

    def get_cfg_dir(self, mode):
        """Get the full path to the 'cfg' dir"""
        main_dir = self.get_main_dir(mode)
        return os.path.join(main_dir, "cfg")

    def get_main_dir(self, mode):
        """Get the full path to the main dir eg. 'Left 4 Dead 2\\left4dead2"""
        root_dir = self.get_dir(mode)
        main_dir_name = self.game.get_title().replace(" ", "")
        main_dir_name = main_dir_name.lower()  # python is case sensitive; convert to Left4Dead2 -> left4dead2
        return os.path.join(root_dir, main_dir_name)

    def get_dir(self, mode):
        """Get the full path to the specified mode's directory. If not found prompts to manually select"""
        match mode:
            case "user":
                installation_id_file = self.user_dir_id_file
            case "dev":
                installation_id_file = self.dev_dir_id_file
            case _:
                raise ValueError("Invalid mode parameter")

        steam_games_dir = self.steam_info["game_dir"]
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                installation_id_file_path = os.path.join(folder_path, installation_id_file)
                if os.path.isfile(installation_id_file_path):
                    return folder_path

        # could not find the id file for specified mode - prompt to manually select
        message = (
            f"Could not find id file for the {mode} installation directory.\n\n\n\n"
            "Manually select it? If so - Be sure to select the correct directory!"
        )
        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=SCRIPT_NAME, choices=choices)
        if response == "No":
            return False
        folder_path = filedialog.askdirectory(
            mustexist=True, title=f"Select the {mode} directory", initialdir=self.steam_info.get("game_dir")
        )
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(
                f"Could not find game installation directory for specified installation mode ({mode})"
            )
        id_file_path = os.path.join(folder_path, installation_id_file)
        with open(id_file_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(id_file_path)
        return folder_path

    def activate_mode(self, mode):
        """Activate user/dev mode by switching folder names eg. Left 4 Dead 2 & Left 4 Dead 2 User"""
        assert self.is_installed("dev"), "Called activate_mode to activate dev mode without it being installed"

        try:
            if mode == "user":
                os.rename(
                    self.get_dir("dev"),
                    os.path.join(self.steam_info.get("game_dir"), "backup_hud_dev." + self.game.get_title()),
                )
                os.rename(self.get_dir("user"), os.path.join(self.steam_info.get("game_dir"), self.game.get_title()))
            elif mode == "dev":
                os.rename(
                    self.get_dir("user"),
                    os.path.join(self.steam_info.get("game_dir"), self.game.get_title() + " User"),
                )
                os.rename(self.get_dir("dev"), os.path.join(self.steam_info.get("game_dir"), self.game.get_title()))
            else:
                raise ValueError("Invalid mode parameter")
        except RuntimeError as err_info:
            print(f"An error occurred during directory renaming: {err_info}")

    def is_installed(self, mode):
        """Check if mode is installed"""
        assert mode in ["user", "dev"], "Invalid mode parameter"

        # confirm mode is installed by retrieving its dir
        install_dir = self.get_dir(mode)
        if not os.path.isdir(install_dir):
            return False

        # confirm this is the correct directory by checking the game's executable
        if os.path.isfile(os.path.join(install_dir, self.game.get_exe())):
            return True
        else:
            # raise RuntimeError(f"Game executable not found in game directory: '{install_dir}'")
            return False

    def run_installer(self):
        """Runs the installer and throws errors on failure"""
        if DEBUG_MODE:
            if not self._perform_installation():
                raise RuntimeError("Installation cancelled!")
        else:
            try:
                self._perform_installation()
            except RuntimeError as err_info:
                Tk.messagebox.showerror(
                    "Error", str(err_info) + "\n\nInstallation cancelled! Currently unhandled. Closing."
                )
                sys.exit()

    def _perform_installation(self):
        # verify the user installation is available
        if not self.is_installed("user"):
            raise AssertionError("User installation not found. Unable to install")

        # delete the dev folder for debugging purposes only
        # if DEBUG_MODE and os.path.isdir(self.get_dir("dev")):
        #     self.activate_mode("user")
        #     shutil.rmtree(self.get_dir("dev"))
        #     print('debug mode: successfully deleted the dev folder')

        # close the game
        self.game.close()

        # confirm install start
        # if not self._prompt_install_start():
        #     return False

        # 1. create dev folder template (folder & .exe) for detection incase of cancellation for cleanup
        # self._create_dev_dir()

        # 2. copy the game files into and activate the dev folder
        # self._copy_game_files()
        # print('finished copying files')
        # self.activate_mode("dev")

        # 3. steam verify = prompt to verify game install through steam to update and restore all game files
        # self._prompt_game_verified()

        # 4. extract paks
        # self._extract_paks()
        # self._disable_paks()

        # 5. install mods
        # self._install_mods()

        # 6. rebuild audio cache
        self._rebuild_audio()

        # finish installation
        input("press enter to successfully finish installation")
        return True

    def _prompt_install_start(self):
        title = f"Enable hud editing for {self.game.get_title()}?"
        disk_space = get_dir_size_in_gb(self.get_dir("user"))
        message = (
            f"Enable hud editing for {self.game.get_title()}?\n\n"
            "- This can take up to ~30 minutes depending on drive and processor speed\n"
            f"- This will use around {disk_space} of disk space (copy of the game folder)\n"
            "- Keep any L4D games closed during this process\n\n"
            "It is possible to cancel the setup at any time by closing the progress window"
        )

        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            return True
        elif response == "No":
            return False
        else:
            return False

    def _create_dev_dir(self):
        game_user_dir = self.get_dir("user")
        game_dev_dir = os.path.join(self.steam_info.get("game_dir"), "backup_hud_dev." + self.game.get_title())
        game_exe_path = os.path.join(game_user_dir, self.game.get_exe())
        dev_id_file_path = os.path.join(game_dev_dir, self.dev_dir_id_file)

        os.mkdir(game_dev_dir)
        shutil.copy(game_exe_path, game_dev_dir)
        with open(dev_id_file_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(dev_id_file_path)

    def _copy_game_files(self):
        copy_directory_contents(self.get_dir("user"), self.get_dir("dev"), self.user_dir_id_file)

    def _prompt_game_verified(self):
        title = f"Verify integrity of games files for {self.game.get_title()} in steam"
        message = (
            f"Verify integrity of games files for {self.game.get_title()} in steam\n\n"
            f"Right-Click {self.game.get_title()} -> Properties -> Local Files -> 'Verify integrity of games files'\n"
            "This will not affect your game installation. Only the copy that was just made\n\n"
            "Are you sure Steam has finished verifying AND downloaded any missing files?"
        )

        choices = ["Yes", "No"]
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            pass
        elif response == "No":
            return False
        else:
            return False

        # ask a second time - are you really sure?
        message = (
            f"Are you REALLY sure Steam has finished verifying AND"
            f"downloaded any missing files for {self.game.get_title()}?"
        )
        response = easygui.buttonbox(message, title=title, choices=choices)
        if response == "Yes":
            return True
        return False

    def _find_pak_files(self, dev_dir, callback):
        for subdir_name in os.listdir(dev_dir):
            subdir_path = os.path.join(dev_dir, subdir_name)
            if os.path.isdir(subdir_path):
                for filename in os.listdir(subdir_path):
                    if filename == "pak01_dir.vpk":
                        filepath = os.path.join(subdir_path, filename)
                        callback(filepath, subdir_path)

    def _extract_paks(self):
        """Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories."""
        print("extract paks")
        dev_dir = self.get_dir("dev")

        def extract_callback(filepath, output_dir):
            vpk_class = VPK(filepath)
            vpk_class.extract(output_dir)

        self._find_pak_files(dev_dir, extract_callback)

    def _disable_paks(self):
        dev_dir = self.get_dir("dev")

        def disable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk.disabled")
            os.rename(source_filepath, target_filepath)

        self._find_pak_files(dev_dir, disable_callback)

    def _enable_paks(self):
        dev_dir = self.get_dir("dev")

        def enable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk")
            os.rename(source_filepath, target_filepath)

        self._find_pak_files(dev_dir, enable_callback)

    def _install_mods(self):
        mods_dev_map_dir = os.path.join(MODS_DIR, self.game.get_title(), "export")
        mods_addons_dir = os.path.join(MODS_DIR, "Addons", "Export")
        mods_sourcemod_dir = os.path.join(MODS_DIR, "SourceMod", "Export")
        main_dir = self.get_main_dir("dev")

        copy_directory_contents(mods_dev_map_dir, main_dir)
        copy_directory_contents(mods_addons_dir, main_dir)
        copy_directory_contents(mods_sourcemod_dir, main_dir)

    def _rebuild_audio(self):
        print("rebuild audio")

        cfg_dir = self.get_cfg_dir("dev")
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        with open(valverc_path, "w", encoding="utf-8") as file_handle:
            file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")

        self.game.close()
        self.game.run("dev", "wait on close")
        print("finished rebuilding audio")
        # Run, % STEAM_INFO.exePath A_Space "-applaunch " this.game.obj.appid " -novid -w 1 -h 1 -x 0 -y 0 -windowed"


def debug_installer_class(game_instance):
    """Debug installer class"""
    os.system("cls")  # clear terminal

    saved_data = load_data()
    inst = Installer(saved_data, game_instance)
    inst.run_installer()
    # inst.toggle_dev_mode(True)

    input("end of class_installer autoexecute")
