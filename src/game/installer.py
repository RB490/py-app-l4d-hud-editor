# pylint: disable=protected-access, broad-exception-caught, unused-private-member
"""Game class installation methods

Notes:
    There is a fair amount of duplicate install/update/repair. Choosing to leave 
    as is right now because the added complexity isn't worth it
"""
import filecmp
import os
import shutil

from game.constants import DirectoryMode, InstallationState

# pylint: disable=unused-import
from game.installer_prompts import prompt_delete, prompt_start, prompt_verify_game
from utils.constants import MODS_DIR
from utils.functions import (
    copy_directory,
    get_backup_filename,
    get_backup_path,
    wait_process_close,
)
from utils.shared_utils import show_message
from utils.vpk import VPKClass


class GameInstaller:
    "Game class installation methods"

    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data

    def uninstall(self):
        "Uninstall"
        print("Uninstalling..")

        # is dev installed?
        if not self.game.installed(DirectoryMode.DEVELOPER):
            print("Not installed!")
            return True

        # prompt user
        if not prompt_delete(self.game):
            return False

        # close the game
        self.game.close()

        # remove directory
        print("Deleting game directory...")
        shutil.rmtree(self.game.dir.get(DirectoryMode.DEVELOPER))

        # finished
        print("Uninstalled!")

    def update(self):
        "Update"
        print("Updating...")

        current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)

        # is installed?
        if current_state is not InstallationState.COMPLETED:
            print("Not installed!")
            return False

        # get user directory
        if not self.game.installed(DirectoryMode.USER):
            try:
                self.game.dir.id.set_id_path(DirectoryMode.USER)
            except Exception as err_info:
                show_message(f"{err_info}", "error", "Could not get user directory!")
                return False

        # confirm start
        if not prompt_start(self.game, "repair", "This will re-extract every pak01_dir in the dev folder"):
            return False

        # close game
        self.game.close()

        # acativate developer mode
        self.game.dir.set(DirectoryMode.DEVELOPER)

        # enable paks
        self.__enable_paks()

        # set resume state
        self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, InstallationState.VERIFYING_GAME)

        # perform installation steps
        try:
            self.__process_installation_steps(current_state)
            print("Finished updating!")
            return True
        except Exception as err_info:
            print(f"Update error: {err_info}")
            # since installation state is saved, don't do anything here
            return False

    def repair(self):
        "Repair"
        print("Repairing...")

        current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)

        # is installed?
        if current_state is not InstallationState.COMPLETED:
            print("Not installed!")
            return False

        # get user directory
        if not self.game.installed(DirectoryMode.USER):
            try:
                self.game.dir.id.set_id_path(DirectoryMode.USER)
            except Exception as err_info:
                show_message(f"{err_info}", "error", "Could not get user directory!")
                return False

        # confirm start
        if not prompt_start(self.game, "repair", "This will re-extract every pak01_dir in the dev folder"):
            return False

        # close game
        self.game.close()

        # acativate developer mode
        self.game.dir.set(DirectoryMode.DEVELOPER)

        # enable paks
        self.__enable_paks()

        # set resume state
        self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, InstallationState.EXTRACTING_PAKS)

        # perform installation steps
        try:
            self.__process_installation_steps(current_state)
            # finished
            print("Finished reparing!")
            return True
        except Exception as err_info:
            print(f"Repair error: {err_info}")
            # since installation state is saved, don't do anything here
            return False

    def install(self):
        "Install"
        print("Installing..")

        current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)

        # already installed?
        if current_state is InstallationState.COMPLETED:
            print("Already installed!")
            return True

        # get user directory
        if not self.game.installed(DirectoryMode.USER):
            try:
                self.game.dir.id.set_id_path(DirectoryMode.USER)
            except Exception as err_info:
                show_message(f"{err_info}", "error", "Could not get user directory!")
                return False

        # get dev directory
        try:
            result = self.game.dir.id.set_id_path(DirectoryMode.DEVELOPER)
            if result:
                print("Successfully selected the developer directory. Finished installation.")
                return True
        except Exception as err_info:
            print(f"Could not retrieve developer directory: {err_info}")

        # confirm start
        if not prompt_start(self.game, "install"):
            return False

        # close game
        self.game.close()

        # delete dev folder if needed
        if current_state == InstallationState.UNKNOWN:
            invalid_dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

            if invalid_dev_dir:
                extra_message = "Consider if you want to try to repair the installation instead of deleting it"
                if not prompt_delete(self.game, extra_message):
                    return False
                shutil.rmtree(invalid_dev_dir)

        # install
        try:
            self.__process_installation_steps(current_state)
            # finished
            print("Finished installing!")
            return True
        except Exception as err_info:
            print(f"Installation error: {err_info}")
            # since installation state is saved, don't do anything here
            return False

    def __process_installation_steps(self, resume_state):
        installation_steps = [
            InstallationState.CREATE_DEV_DIR,
            InstallationState.COPYING_FILES,
            InstallationState.VERIFYING_GAME,
            InstallationState.EXTRACTING_PAKS,
            InstallationState.MAIN_DIR_BACKUP,
            InstallationState.INSTALLING_MODS,
            InstallationState.REBUILDING_AUDIO,
        ]

        # Find the index of the last completed step or set to 0 if resume_state is not in installation_steps
        if resume_state not in installation_steps:
            last_completed_index = 0
        else:
            last_completed_index = installation_steps.index(resume_state)

        # Perform installation steps starting from the next step after the last completed one
        for _, state in enumerate(installation_steps[last_completed_index:]):
            self.__perform_installation_step(state)
            self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, state)
        # except Exception as err_info:
        #     print(f"step process error: {err_info}")
        #     return False

        # Update installation state to completed or repaired based on process type
        self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, InstallationState.COMPLETED)
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
        elif state == InstallationState.MAIN_DIR_BACKUP:
            self._main_dir_backup()
        elif state == InstallationState.INSTALLING_MODS:
            self.__install_mods()
        elif state == InstallationState.REBUILDING_AUDIO:
            self.__rebuild_audio()

    def __create_dev_dir(self):
        print("Creating developer directory")

        dev_dir = self.game.dir._get_dir_backup_name(DirectoryMode.DEVELOPER)

        os.mkdir(dev_dir)

        # write id file
        id_path = os.path.join(dev_dir, self.game.dir.id._get_id_filename(DirectoryMode.DEVELOPER))
        with open(id_path, "w", encoding="utf-8"):
            pass

        # copy executable
        game_exe = self.game.get_exe()
        source_exe_path = os.path.join(self.game.dir.get(DirectoryMode.USER), game_exe)
        target_exe_path = os.path.join(dev_dir, game_exe)
        shutil.copy2(source_exe_path, target_exe_path)

        # activate directory
        self.game.dir.set(DirectoryMode.DEVELOPER)
        return

    def __copy_game_files(self):
        copy_directory(
            self.game.dir.get(DirectoryMode.USER),
            self.game.dir.get(DirectoryMode.DEVELOPER),
            self.game.dir.id._get_id_filename(DirectoryMode.USER),
        )

    def __prompt_verify_game(self):
        print("Prompting user to verify game")
        prompt_verify_game(self.game)

    def __find_pak01_files(self, game_dir, callback):
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            pak01_path = self.game.dir.get_pak01_vpk_in(subdir_path)

            if pak01_path:
                callback(pak01_path, subdir_path)

    def __extract_paks(self):
        """Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories."""
        print("Extracting pak01.vpk's")

        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def extract_callback(filepath, output_dir):
            vpk_class = VPKClass()
            vpk_class.extract(filepath, output_dir)

        self.__find_pak01_files(dev_dir, extract_callback)

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

        self.__find_pak01_files(user_dir, get_user_paks_callback)
        self.__find_pak01_files(dev_dir, get_dev_paks_callback)

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

        self.__find_pak01_files(dev_dir, enable_callback)

    def __disable_paks(self):
        print("Disabling pak01.vpk's")
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def disable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = get_backup_path(os.path.join(subdir_path, "pak01_dir.vpk"))
            os.rename(source_filepath, target_filepath)

        self.__find_pak01_files(dev_dir, disable_callback)

    def _main_dir_backup(self):
        print("Copying main directory to create a backup for the sync class")

        resource_dir = os.path.join(self.game.dir.get_main_dir(DirectoryMode.DEVELOPER), "resource")
        resource_backup_dir = self.game.dir.get_main_dir_backup_resource(DirectoryMode.DEVELOPER)
        materials_dir = os.path.join(self.game.dir.get_main_dir(DirectoryMode.DEVELOPER), "materials")
        materials_backup_dir = self.game.dir.get_main_dir_backup_materials(DirectoryMode.DEVELOPER)
        backup_dir = self.game.dir.get_main_dir_backup(DirectoryMode.DEVELOPER)

        # create backup dir from scratch
        if os.path.isdir(backup_dir):
            print("Removing previous backup directory to keep it 100% clean")
            shutil.rmtree(backup_dir)
        os.makedirs(backup_dir)

        print(resource_dir)
        print(resource_backup_dir)
        print(materials_dir)
        print(materials_backup_dir)

        copy_directory(
            resource_dir,
            resource_backup_dir,
        )
        copy_directory(
            materials_dir,
            materials_backup_dir,
        )

    def __install_mods(self):
        print("Installing mods")

        # variables
        mods_dev_map_dir = os.path.join(MODS_DIR, "Dev Map", self.game.get_title(), "export")
        mods_addons_dir = os.path.join(MODS_DIR, "Addons", "Export")
        mods_sourcemod_dir = os.path.join(MODS_DIR, "SourceMod", "Export")
        main_dir = self.game.dir.get_main_dir(DirectoryMode.DEVELOPER)

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
        cfg_dir = self.game.dir.get_cfg_dir(DirectoryMode.DEVELOPER)
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        # write .rc file
        with open(valverc_path, "w", encoding="utf-8") as file_handle:
            file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")

        # run game to rebuild audio
        self.game.close()
        self.game.window.run(DirectoryMode.DEVELOPER, write_config=False)  # don't overwrite valve.rc

        if not wait_process_close(self.game.get_exe(), 300):  # account audio rebuilding
            return False
