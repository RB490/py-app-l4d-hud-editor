# pylint: disable=protected-access, broad-exception-caught, unused-private-member, bare-except
"""Game class installation methods

Notes:
    There is a fair amount of duplicate install/update/repair. Choosing to leave
    as is right now because the added complexity isn't worth it
"""
import os
import shutil
import threading
import time

from loguru import logger
from shared_gui.progress import ProgressGUI
from shared_managers.valve_vpk_manager import VPKManager  # type: ignore
from shared_utils.functions import copy_directory, show_message

from src.game.constants import DirectoryMode, InstallationError, InstallationState

# pylint: disable=unused-import
from src.game.installer.prompts import prompt_delete, prompt_start, prompt_verify_game
from src.utils.constants import MODS_DIR
from src.utils.functions import count_files_and_dirs, get_backup_path, wait_process_close


class GameInstaller:
    "Game class installation methods"

    def __init__(self, game_class):
        self.game = game_class

    def uninstall(self):
        "Uninstall"
        logger.debug("Uninstalling..")

        # is dev installed?
        if not self.game.is_installed(DirectoryMode.DEVELOPER):
            show_message("Not installed!", "info")
            return True

        # prompt user
        if not prompt_delete():
            return False

        self._perform_uninstall()

        # finished
        show_message("Finished uninstalling!", "info")

    def _perform_uninstall(self):
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

        # remove empty folder
        os.rmdir(path)

        rem_gui.update_progress(f"Deletion completed: {files_processed}/{total_files} files")
        time.sleep(4)  # show the deletion completed message for a little while before closing
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
        if (action == "repair" or action == "update") and current_state != InstallationState.INSTALLED:
            show_message(f"Can't {action}! Developer mode is not (fully) installed", "error", action_description)
            return False
        elif action == "install" and current_state == InstallationState.INSTALLED:
            show_message(f"Can't {action}! Developer mode is already installed!", "error", action_description)
            return False

        # get user directory
        if not self.game.is_installed(DirectoryMode.USER):
            try:
                self.game.dir.id.set_path(DirectoryMode.USER)
            except Exception as err_info:
                show_message(f"{err_info}", "error", "Could not get user directory!")
                return False

        # prompt to select potentially existing dev directory (for example incase broken id file)
        if not self.game.dir.get(DirectoryMode.DEVELOPER):
            try:
                result = self.game.dir.id.set_path(DirectoryMode.DEVELOPER)
                # if developer directory was located, check if installation is already completed
                if result:
                    current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)
                    if current_state == InstallationState.INSTALLED:
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
                self._perform_uninstall()

        # activate developer mode
        if self.game.dir.get(DirectoryMode.DEVELOPER):
            try:
                self.game.dir.set(DirectoryMode.DEVELOPER)
            except Exception as e:
                raise InstallationError("Could not activate developer directory: {e}")

        # enable paks
        self._enable_paks()

        # set resume state
        self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, resume_state)

        # perform installation steps
        try:
            self._process_installation_steps(resume_state, action_description)
            show_message(f"Finished {action_description.lower()}!", "info")
            return True
        except Exception as err_info:
            show_message(f"{action_description} error: {err_info}", "error")
            return False

    def _process_installation_steps(self, resume_state, action_description):
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
                self._perform_installation_step(state)
                time.sleep(2)  # artifically wait small amount of time so very short steps are still visible in gui

            # close progress gui
            p_gui.destroy()

            # Update installation state to completed
            self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, InstallationState.INSTALLED)
            return True
        except Exception as err_info:
            p_gui.destroy()
            raise InstallationError(f"Installation step error: {err_info}") from err_info

    def _perform_installation_step(self, state):
        "perform"
        logger.debug(f"Performing installation step with state: {state}")

        if state == InstallationState.CREATE_DEV_DIR:
            self._create_dev_dir()
        elif state == InstallationState.COPYING_FILES:
            self._copy_game_files()
        elif state == InstallationState.VERIFYING_GAME:
            self._prompt_verify_game()
        elif state == InstallationState.EXTRACTING_PAKS:
            self._extract_paks()
            self._disable_paks()
        elif state == InstallationState.MAIN_DIR_BACKUP:
            self._main_dir_backup()
        elif state == InstallationState.INSTALLING_MODS:
            self._install_mods()
        elif state == InstallationState.REBUILDING_AUDIO:
            self._rebuild_audio()

    def _create_dev_dir(self):
        logger.debug("Creating developer directory")

        dev_dir = self.game.dir._get_random_dir_name_for(DirectoryMode.DEVELOPER)

        os.mkdir(dev_dir)

        # write id file
        id_path = os.path.join(dev_dir, self.game.dir.id.get_file_name(DirectoryMode.DEVELOPER))
        self.game.dir.id._create_file(id_path)

        # copy executable
        game_exe = self.game.get_exe()
        source_exe_path = os.path.join(self.game.dir.get(DirectoryMode.USER), game_exe)
        target_exe_path = os.path.join(dev_dir, game_exe)
        shutil.copy2(source_exe_path, target_exe_path)

        # activate directory
        try:
            self.game.dir.set(DirectoryMode.DEVELOPER)
        except Exception as e:
            raise InstallationError("Could not activate developer directory: {e}")
        return

    def _copy_game_files(self):
        user_dir = self.game.dir.get(DirectoryMode.USER)
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        user_id_file_name = self.game.dir.id.get_file_name(DirectoryMode.USER)

        # Copy all files from the root folder to the developer folder (except user ID file)
        for item in os.listdir(user_dir):
            src_item = os.path.join(user_dir, item)
            dest_item = os.path.join(dev_dir, item)

            if os.path.isfile(src_item) and os.path.basename(src_item) != user_id_file_name:
                shutil.copy2(src_item, dest_item)

        # Loop through subfolders and call copy_directory
        for dir_name in os.listdir(user_dir):
            src_subfolder = os.path.join(user_dir, dir_name)
            dest_subfolder = os.path.join(dev_dir, dir_name)
            if os.path.isdir(src_subfolder):
                copy_directory(src_subfolder, dest_subfolder)

    def _prompt_verify_game(self):
        logger.debug("Prompting user to verify game")
        prompt_verify_game()

    def _extract_paks(self):
        """Extract all files from the pak01_dir.vpk files located in the specified game directory
        to their respective root directories."""
        logger.debug("Extracting pak01.vpk's")

        vpk_class = VPKManager()

        pak01_data = self.game.dir._get_pak01_dirs_with_files(DirectoryMode.DEVELOPER)

        def extract_pak_thread(pak_dir, pak_path):
            vpk_class.extract(pak_path, pak_dir)

        # Create a list to hold thread objects
        threads = []

        for pak01_dir, pak01_path in pak01_data:
            # Create a thread for each extraction task
            thread = threading.Thread(target=extract_pak_thread, args=(pak01_dir, pak01_path))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    def _enable_paks(self):
        logger.debug("Enabling pak01.vpk's")
        dev_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        # this check ensures repair() & update() can use this method. and install() ignores it if needed
        if not dev_dir:
            logger.debug("Enable paks: Developer directory not retrieved.")
            return

        pak01_data = self.game.dir._get_pak01_dirs_with_files(DirectoryMode.DEVELOPER)
        for pak01_dir, pak01_path in pak01_data:
            source_filepath = pak01_path
            target_filepath = os.path.join(pak01_dir, "pak01_dir.vpk")
            os.rename(source_filepath, target_filepath)
            logger.debug(f"Renaming file {source_filepath} -> {target_filepath}")

    def _disable_paks(self):
        logger.debug("Disabling pak01.vpk's")

        pak01_data = self.game.dir._get_pak01_dirs_with_files(DirectoryMode.DEVELOPER)
        for pak01_dir, pak01_path in pak01_data:
            source_filepath = pak01_path
            target_filepath = get_backup_path(os.path.join(pak01_dir, "pak01_dir.vpk"))
            os.rename(source_filepath, target_filepath)

    def _main_dir_backup(self):
        logger.debug("Copying main directory to create a backup for the sync class")

        pak01_data = self.game.dir._get_pak01_dirs_with_files(DirectoryMode.DEVELOPER)
        for pak01_dir, _ in pak01_data:
            # variables
            backup_dir = get_backup_path(pak01_dir)

            resource_dir = self.game.dir.get_subdir(pak01_dir, "resource")
            materials_dir = self.game.dir.get_subdir(pak01_dir, "materials")
            scripts_dir = self.game.dir.get_subdir(pak01_dir, "scripts")

            resource_backup_dir = os.path.join(get_backup_path(pak01_dir), "resource")
            materials_backup_dir = os.path.join(get_backup_path(pak01_dir), "materials")
            scripts_backup_dir = os.path.join(get_backup_path(pak01_dir), "scripts")

            # remove old backup dir
            if os.path.isdir(backup_dir):
                logger.debug("Removing previous backup directory to keep it 100% clean: '{backup_dir}'")
                shutil.rmtree(backup_dir)

            # create backup dir
            copy_directory(
                resource_dir,
                resource_backup_dir,
            )
            copy_directory(
                materials_dir,
                materials_backup_dir,
            )
            copy_directory(
                scripts_dir,
                scripts_backup_dir,
            )

    def _install_mods(self):
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

    def _rebuild_audio(self):
        logger.debug("Rebuilding audio")

        # variables
        cfg_dir = self.game.dir.get_main_subdir(DirectoryMode.DEVELOPER, "cfg")
        valverc_path = os.path.join(cfg_dir, "valve.rc")

        # write .rc file
        try:
            with open(valverc_path, "w", encoding="utf-8") as file_handle:
                file_handle.write("mat_setvideomode 800 600 1 0; snd_rebuildaudiocache; exit")
        except IOError as e:
            logger.error("Failed to write valve.rc file: %s", e)
            raise InstallationError("Failed to write valve.rc file")

        # run game to rebuild audio
        try:
            self.game.window.close()
            result = self.game.window.run(DirectoryMode.DEVELOPER, write_config=False, restore_pos=False)
        except Exception as e:
            logger.error("Failed to run the game: %s", e)
            raise InstallationError("Failed to run the game and rebuild audio cache: {e}")

        logger.debug("Debug: game is fully running!")
        if not result or not wait_process_close(self.game.get_exe(), 300):
            raise InstallationError("Timed out waiting for game to close after rebuilding audio cache: {e}")

        # write default config so manually running the game doesn't rebuild audiocache -> exit
        self.game.write_config()


def main():
    """main"""
    from src.game.game import Game

    game = Game()
    installer = GameInstaller(game)
    # installer.install()
    installer._prompt_verify_game()
    logger.info("this is a test!")


if __name__ == "__main__":
    main()
