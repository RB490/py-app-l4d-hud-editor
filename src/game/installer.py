# pylint: disable=protected-access, broad-exception-caught, unused-private-member, bare-except
"""Game class installation methods

Notes:
    There is a fair amount of duplicate install/update/repair. Choosing to leave
    as is right now because the added complexity isn't worth it
"""
import os
import shutil
import time

from loguru import logger

from game.constants import DirectoryMode, InstallationError, InstallationState

# pylint: disable=unused-import
from game.installer_prompts import prompt_delete, prompt_start, prompt_verify_game
from gui.progress import ProgressGUI
from shared_utils.shared_utils import copy_directory, show_message
from utils.constants import MODS_DIR
from utils.functions import count_files_and_dirs, get_backup_path, wait_process_close
from utils.vpk import VPKClass


class GameInstaller:
    "Game class installation methods"

    def __init__(self, game_class):
        self.game = game_class

    def uninstall(self):
        "Uninstall"
        logger.debug("Uninstalling..")

        # is dev installed?
        if not self.game.installation_exists(DirectoryMode.DEVELOPER):
            show_message("Not installed!", "info")
            return True

        # prompt user
        if not prompt_delete():
            return False

        self.__perform_uninstall()

        # finished
        show_message("Finished uninstalling!", "info")

    def __perform_uninstall(self):
        # set deletion state
        self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, InstallationState.PENDING_DELETION)

        # close the game
        self.game.window.close()

        # remove directory
        logger.debug("Deleting game directory...")

        # variables
        path = self.game.dir.get(DirectoryMode.DEVELOPER)
        update_interval = 1000  # Update the GUI every 1000 files/dirs processed
        total_files, total_subdirs = count_files_and_dirs(path)
        total_items = total_files + total_subdirs

        rem_gui = ProgressGUI("Uninstalling", 600, 60, total_items // update_interval)  # Adjust total steps
        rem_gui.show()

        files_processed = 0
        for root, dirs, files in os.walk(path, topdown=False):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                files_processed += 1

                if files_processed % update_interval == 0:
                    rem_gui.update_progress(f"Deleted {files_processed}/{total_files} files")

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)

        rem_gui.update_progress(f"Deletion completed: {files_processed}/{total_files} files")
        rem_gui.destroy()

    def update(self):
        "Update"
        return self.common_installation_logic("update", InstallationState.VERIFYING_GAME, "Updating")

    def repair(self):
        "Repair"
        return self.common_installation_logic("repair", InstallationState.EXTRACTING_PAKS, "Repairing")

    def install(self):
        "Install"
        current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)
        return self.common_installation_logic("install", current_state, "Installing")

    def common_installation_logic(self, action, resume_state, action_description):
        "Installation logic for repair/update/install"
        logger.debug(f"{action_description}...")

        # confirm params
        if action not in ["install", "update", "repair"]:
            raise ValueError(f"Invalid action specified: {action}")

        current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)

        # confirm action is possible
        if (action == "repair" or action == "update") and current_state != InstallationState.COMPLETED:
            show_message(f"Can't {action}! Developer mode is not fully installed", "error", action_description)
            return False
        elif action == "install" and current_state == InstallationState.COMPLETED:
            show_message(f"Can't {action}! Developer mode is already installed!", "error", action_description)
            return False

        # get user directory
        if not self.game.installation_exists(DirectoryMode.USER):
            try:
                self.game.dir.id.set_path(DirectoryMode.USER)
            except Exception as err_info:
                show_message(f"{err_info}", "error", "Could not get user directory!")
                return False

        # prompt to select potentially existing dev directory (for example incase broken id file)
        if not self.game.installation_exists(DirectoryMode.DEVELOPER):
            try:
                result = self.game.dir.id.set_path(DirectoryMode.DEVELOPER)
                # if developer directory was located, check if installation is already completed
                if result:
                    current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)
                    if current_state == InstallationState.COMPLETED:
                        logger.debug(f"Successfully selected the developer directory. Finished {action_description}.")
                        return True
            except Exception as err_info:
                logger.debug(f"User did not select developer installation directory! Continuing... ({err_info})")

        # confirm start
        if not prompt_start(action, f"This will {action_description.lower()}"):
            return False

        # close game
        self.game.window.close()

        # install: delete dev folder if needed
        if (
            action == "install"
            and current_state == InstallationState.UNKNOWN
            or current_state == InstallationState.PENDING_DELETION
        ):
            invalid_dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

            if invalid_dev_dir:
                extra_message = "Consider if you want to try to repair the installation instead of deleting it"
                if not prompt_delete(extra_message):
                    return False
                self.__perform_uninstall()

        # activate developer mode
        if self.game.installation_exists(DirectoryMode.DEVELOPER):
            self.game.dir.set(DirectoryMode.DEVELOPER)

        # enable paks
        self.__enable_paks()

        # set resume state
        self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, resume_state)

        # perform installation steps
        try:
            self.__process_installation_steps(resume_state, action_description)
            show_message(f"Finished {action_description.lower()}!", "info")
            return True
        except Exception as err_info:
            show_message(f"{action_description} error: {err_info}", "error")
            return False

    def __process_installation_steps(self, resume_state, action_description):
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

        # show progress gui
        total_steps = len(installation_steps) - last_completed_index
        p_gui = ProgressGUI(action_description, 600, 60, total_steps)  # Create the GUI instance
        p_gui.show()

        try:
            # Perform installation steps starting from the next step after the last completed one
            for _, state in enumerate(installation_steps[last_completed_index:]):
                self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, state)
                p_gui.update_progress(state.name)
                self.__perform_installation_step(state)
                time.sleep(2)  # artifically was some amount of time so very short steps are still visible in gui

            # close progress gui
            p_gui.destroy()

            # Update installation state to completed
            self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, InstallationState.COMPLETED)
            return True
        except Exception as err_info:
            p_gui.destroy()
            raise InstallationError(f"Installation step error: {err_info}") from err_info

    def __perform_installation_step(self, state):
        "perform"
        logger.debug(f"Performing installation step with state: {state}")

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
        logger.debug("Creating developer directory")

        dev_dir = self.game.dir._get_dir_backup_name(DirectoryMode.DEVELOPER)

        os.mkdir(dev_dir)

        # write id file
        id_path = os.path.join(dev_dir, self.game.dir.id._get_filename(DirectoryMode.DEVELOPER))
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
        user_dir = self.game.dir.get(DirectoryMode.USER)
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        copy_directory(
            user_dir,
            dev_dir,
        )
        user_id_file = self.game.dir.id._get_filename(DirectoryMode.USER)
        user_id_file_path = os.path.join(dev_dir, user_id_file)
        if os.path.isfile(user_id_file_path):
            os.remove(user_id_file_path)
            logger.debug(f"Deleted user ID file from dev directory: {user_id_file_path}")
        else:
            raise InstallationError(f"Could not remove user ID file from dev directory: {user_id_file_path}")

    def __prompt_verify_game(self):
        logger.debug("Prompting user to verify game")
        prompt_verify_game()

    def __find_pak01_files(self, game_dir, callback):
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            pak01_path = self.game.dir.get_pak01_vpk_in(subdir_path)

            if pak01_path:
                callback(pak01_path, subdir_path)

    def __extract_paks(self):
        """Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories."""
        logger.debug("Extracting pak01.vpk's")

        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def extract_callback(filepath, output_dir):
            vpk_class = VPKClass()
            vpk_class.extract(filepath, output_dir)

        self.__find_pak01_files(dev_dir, extract_callback)

    def __enable_paks(self):
        logger.debug("Enabling pak01.vpk's")
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        # this check ensures repair() & update() can use this method. and install() ignores it if needed
        if not dev_dir:
            logger.debug("Enable paks: Developer directory not retrieved.")
            return

        def enable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = os.path.join(subdir_path, "pak01_dir.vpk")
            os.rename(source_filepath, target_filepath)
            logger.debug(f"Renaming file {source_filepath} -> {target_filepath}")

        self.__find_pak01_files(dev_dir, enable_callback)

    def __disable_paks(self):
        logger.debug("Disabling pak01.vpk's")
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        def disable_callback(filepath, subdir_path):
            source_filepath = filepath
            target_filepath = get_backup_path(os.path.join(subdir_path, "pak01_dir.vpk"))
            os.rename(source_filepath, target_filepath)

        self.__find_pak01_files(dev_dir, disable_callback)

    def _main_dir_backup(self):
        logger.debug("Copying main directory to create a backup for the sync class")

        resource_dir = self.game.dir._get_main_subdir(DirectoryMode.DEVELOPER, "resource")
        resource_backup_dir = self.game.dir._get_main_subdir_backup(DirectoryMode.DEVELOPER, "resource")
        materials_dir = self.game.dir._get_main_subdir(DirectoryMode.DEVELOPER, "materials")
        materials_backup_dir = self.game.dir._get_main_subdir_backup(DirectoryMode.DEVELOPER, "materials")
        backup_dir = self.game.dir.get_main_dir_backup(DirectoryMode.DEVELOPER)

        # create backup dir from scratch
        if os.path.isdir(backup_dir):
            logger.debug("Removing previous backup directory to keep it 100% clean")
            shutil.rmtree(backup_dir)
        os.makedirs(backup_dir)

        logger.debug(resource_dir)
        logger.debug(resource_backup_dir)
        logger.debug(materials_dir)
        logger.debug(materials_backup_dir)

        copy_directory(
            resource_dir,
            resource_backup_dir,
        )
        copy_directory(
            materials_dir,
            materials_backup_dir,
        )

    def __install_mods(self):
        logger.debug("Installing mods")

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
        logger.debug("Rebuilding audio")

        # variables
        cfg_dir = self.game.dir.get_cfg_dir(DirectoryMode.DEVELOPER)
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        # write .rc file
        with open(valverc_path, "w", encoding="utf-8") as file_handle:
            file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")

        # run game to rebuild audio
        self.game.window.close()
        result = self.game.window.run(DirectoryMode.DEVELOPER, write_config=False)  # don't overwrite valve.rc

        logger.debug("debug: game is fully running!")
        if not result or not wait_process_close(self.game.get_exe(), 300):  # Account for audio rebuilding
            raise InstallationError("Failed to run the game and rebuild audio cache!")

        # write default config so manually running the game doesn't rebuild audiocache -> exit
        self.game.write_config()
