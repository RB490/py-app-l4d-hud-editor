# pylint: disable=protected-access, broad-exception-caught, unused-private-member
"Game class installation methods"
import filecmp
import os

from game_v2.game_v2 import DirectoryMode, InstallationState

# pylint: disable=unused-import
from game_v2.installer_prompts import (
    prompt_delete_unknown,
    prompt_start,
    prompt_verify_game,
)
from utils.constants import MODS_DIR
from utils.functions import copy_directory, wait_for_process, wait_process_close
from utils.vpk import VPKClass


class GameV2Installer:
    "Game class installation methods"

    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data
        print(self.__class__.__name__)
        # TODO Installer: Finish all functionality
        # TODO Installer: Restore checks & prompts when finished

    def _install(self):
        print("Running installer..")

        # variables
        current_state = self.game.dir._get_installation_state(DirectoryMode.DEVELOPER)
        installation_steps = [
            InstallationState.CREATE_DEV_DIR,
            InstallationState.COPYING_FILES,
            InstallationState.VERIFYING_GAME,
            InstallationState.EXTRACTING_PAKS,
            InstallationState.INSTALLING_MODS,
            InstallationState.REBUILDING_AUDIO,
        ]

        # already installed?
        # if current_state is InstallationState.COMPLETED:
        #     print("Already installed")
        #     return True

        # confirm start
        # if not prompt_start(self.game, "install"):
        #     return False

        # close game
        self.game.close()

        # delete dev folder if needed
        # if current_state == InstallationState.UNKNOWN:
        #     invalid_dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        #     if invalid_dev_dir:
        #         if not prompt_delete_unknown(self.game):
        #             return False
        #         shutil.rmtree(invalid_dev_dir)

        # invalid_dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        # if invalid_dev_dir:
        #     shutil.rmtree(invalid_dev_dir)
        current_state = InstallationState.REBUILDING_AUDIO

        # # perform installation
        try:
            # Find the index of the last completed step or -1 if not found
            last_completed_index = (
                0 if current_state is InstallationState.UNKNOWN else installation_steps.index(current_state)
            )

            # Perform installation steps starting from the next step after the last completed one
            for _, state in enumerate(installation_steps[last_completed_index:]):
                input(f"press enter to: {state}")
                self.game.dir._set_id_content(DirectoryMode.DEVELOPER, state)
                self.__perform_installation_step(state)
        except Exception as err_info:
            print(f"An error occurred during installation initialization: {err_info}")
            return False

        # finished
        self.game.dir._set_id_content(DirectoryMode.DEVELOPER, InstallationState.COMPLETED)

        print("Finished installing!")
        return True

    def __perform_installation_step(self, state):
        "perform"
        print(f"Performing installation step with state: {state}")

        if state == InstallationState.CREATE_DEV_DIR:
            self.__create_dev_dir()
        elif state == InstallationState.COPYING_FILES:
            self.__copy_game_files()
        elif state == InstallationState.VERIFYING_GAME:
            self.__prompt_verify_game()
        elif state == InstallationState.EXTRACTING_PAKS:
            self.__extract_paks()
            self.__disable_paks()
        elif state == InstallationState.INSTALLING_MODS:
            self.__install_mods()
        elif state == InstallationState.REBUILDING_AUDIO:
            self.__rebuild_audio()

    def __create_dev_dir(self):
        print("Creating developer directory")

        dev_dir = self.game.dir._get_dir_backup_name(DirectoryMode.DEVELOPER)

        os.mkdir(dev_dir)

        # write id file
        id_path = os.path.join(dev_dir, self.game.dir.get_id_filename(DirectoryMode.DEVELOPER))
        with open(id_path, "w", encoding="utf-8"):
            pass

        # activate directory
        self.game.dir.set(DirectoryMode.DEVELOPER)
        return

    def __copy_game_files(self):
        print("Copying game files into developer directory")

        copy_directory(
            self.game.dir.get(DirectoryMode.USER),
            self.game.dir.get(DirectoryMode.DEVELOPER),
            self.game.dir.get_id_filename(DirectoryMode.USER),
        )

    def __prompt_verify_game(self):
        print("Prompting user to verify game")
        prompt_verify_game(self.game)

    def __find_pak_files(self, game_dir, callback):
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            if os.path.isdir(subdir_path):
                for filename in os.listdir(subdir_path):
                    if filename == "pak01_dir.vpk" or filename == "pak01_dir.vpk.disabled":
                        filepath = os.path.join(subdir_path, filename)
                        callback(filepath, subdir_path)

    def __extract_paks(self):
        """Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories."""
        print("Extracting pak01.vpk's")

        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def extract_callback(filepath, output_dir):
            vpk_class = VPKClass()
            vpk_class.extract(filepath, output_dir)

        self.__find_pak_files(dev_dir, extract_callback)

    def __extract_outdated_paks(self):
        """1. Confirm which pak01_dir.vpk files are outdated by checking for differences between the user & dev modes
        2. Extract all files from the outdated pak01_dir.vpk files to their respective root directories"""
        print("Extracting outdated pak01.vpk's")

        # retrieve pak files for user & dev modes
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        user_dir = self.game.dir.get(DirectoryMode.USER)

        user_paks = []
        dev_paks = []

        def get_user_paks_callback(filepath, output_dir):
            # vpk_class.extract(filepath, output_dir)
            print(f"filepath={filepath}\noutput_dir={output_dir}")
            pak_tuple = (filepath, output_dir)
            user_paks.append(pak_tuple)

        def get_dev_paks_callback(filepath, output_dir):
            # vpk_class.extract(filepath, output_dir)
            print(f"filepath={filepath}\noutput_dir={output_dir}")
            pak_tuple = (filepath, output_dir)
            dev_paks.append(pak_tuple)

        self.__find_pak_files(user_dir, get_user_paks_callback)
        self.__find_pak_files(dev_dir, get_dev_paks_callback)

        # extract any paks that are not identical between the user & dev folders
        i = 0
        for dev_pak in dev_paks:
            user_pak = user_paks[i]

            print(f'comparing "{dev_pak[0]}" to "{user_pak[0]}"')
            if not filecmp.cmp(dev_pak[0], user_pak[0]):
                print(f'pak out of date! extracting "{dev_pak[0]}"')
                vpk_class = VPKClass()
                vpk_class.extract(dev_pak[0], dev_pak[1])

            i += 1

    def __enable_paks(self):
        print("Enabling pak01.vpk's")
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def enable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk")
            os.rename(source_filepath, target_filepath)
            print("Renaming file from", source_filepath, "to", target_filepath)

        self.__find_pak_files(dev_dir, enable_callback)

    def __disable_paks(self):
        print("Disabling pak01.vpk's")
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def disable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk.disabled")
            os.rename(source_filepath, target_filepath)

        self.__find_pak_files(dev_dir, disable_callback)

    def __install_mods(self):
        print("Installing mods")

        # variables
        mods_dev_map_dir = os.path.join(MODS_DIR, "Dev Map", self.game.get_title(), "export")
        mods_addons_dir = os.path.join(MODS_DIR, "Addons", "Export")
        mods_sourcemod_dir = os.path.join(MODS_DIR, "SourceMod", "Export")
        main_dir = self.game.dir._get_main_dir(DirectoryMode.DEVELOPER)

        # exceptions - we absolutely need these
        if not os.path.exists(mods_dev_map_dir):
            raise FileNotFoundError(f"Directory not found: {mods_dev_map_dir}")

        if not os.path.exists(mods_addons_dir):
            raise FileNotFoundError(f"Directory not found: {mods_addons_dir}")

        if not os.path.exists(mods_sourcemod_dir):
            raise FileNotFoundError(f"Directory not found: {mods_sourcemod_dir}")

        # copy files
        copy_directory(mods_dev_map_dir, main_dir)
        copy_directory(mods_addons_dir, main_dir)
        copy_directory(mods_sourcemod_dir, main_dir)

    def __rebuild_audio(self):
        print("Rebuilding audio")

        # variables
        cfg_dir = self.game.dir._get_cfg_dir(DirectoryMode.DEVELOPER)
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        # write .rc file
        with open(valverc_path, "w", encoding="utf-8") as file_handle:
            file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")

        # run game to rebuild audio
        self.game.close()
        self.game.window.run(DirectoryMode.DEVELOPER)

        if not wait_for_process(self.game.get_exe(), 60):  # account for steam starting up
            return False
        if not wait_process_close(self.game.get_exe(), 300):  # account audio rebuilding
            return False
