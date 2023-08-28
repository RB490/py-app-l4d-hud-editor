"Game class directory methods"
# pylint: disable=protected-access, broad-exception-caught, broad-exception-raised, logging-fstring-interpolation
import logging
import os
import shutil

from game.constants import DirectoryMode, SyncState
from game.dir_id_handler import GameIDHandler
from hud.syncer import files_differ
from shared_utils.logging_manager import LoggerManager
from shared_utils.shared_utils import verify_directory
from utils.functions import (
    copy_directory,
    generate_random_string,
    get_backup_filename,
    get_backup_path,
    rename_with_timeout,
)
from utils.steam_info_retriever import SteamInfoRetriever

logger_manager = LoggerManager(__name__, level=logging.WARNING)  # Pass the desired logging level
# logger_manager = LoggerManager(__name__, level=logging.CRITICAL + 1)  # turns off
logger = logger_manager.get_logger()  # Get the logger instance


class GameDir:
    "Game class directory methods"

    def __init__(self, game_class):
        self.game = game_class
        # pylint: disable=invalid-name
        self.id = GameIDHandler(self.game)
        self.steam = SteamInfoRetriever()

    def _get_dir_backup_name(self, dir_mode):
        random_string = generate_random_string()
        output = os.path.join(
            self.game.steam.get_games_dir(), f"_backup_hud_{dir_mode.name}.{self.game.get_title()}_{random_string}"
        )
        return output

    def set(self, dir_mode):
        "Set directory to mode"
        self.game._validate_dir_mode(dir_mode)

        logger.debug(f"Setting mode: {dir_mode.name}")

        # retrieving source & target dir with self.get also already checks whether they are installed
        rename_timeout = 6
        # variables - source
        source_mode = DirectoryMode.USER if dir_mode == DirectoryMode.DEVELOPER else DirectoryMode.DEVELOPER
        source_dir = self.get(source_mode)
        source_dir_backup = self._get_dir_backup_name(source_mode)
        # variables - target
        target_mode = dir_mode
        target_dir = self.get(target_mode)
        vanilla_dir = self.__get_vanilla_dir()

        if not verify_directory(source_dir, "Could not retrieve source directory!"):
            return False
        if not verify_directory(target_dir, "Could not retrieve target directory!"):
            return False
        # not checking vanilla_dir because it might very well not exist if both of the modes are custom renamed

        # do we need to swap?
        if os.path.exists(vanilla_dir) and os.path.samefile(target_dir, vanilla_dir):
            logger.debug(f"{target_mode.name} already active!")
            return True

        # close game
        self.game.close()

        # backup source mode
        if not rename_with_timeout(source_dir, source_dir_backup, rename_timeout):
            return False

        # activate target mode
        if not rename_with_timeout(target_dir, vanilla_dir, rename_timeout):
            return False

        print(f"Set mode: {dir_mode.name} successfully!")
        return True

    def get_vanilla_file(self, relative_file_path):
        """Search all game directories including the backup folder to find the file"""

        is_synced = False
        if self.game.dir.id.get_sync_state(DirectoryMode.DEVELOPER) == SyncState.FULLY_SYNCED:
            is_synced = True

        # variables
        # retrieve game folders to check
        game_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        game_file_directories = self.__get_pak01_vpk_subdirs(DirectoryMode.DEVELOPER)
        # add backup directory last so it's searched last so the code preferably returns file in the main directory
        game_file_directories.append(self.game.dir.get_main_dir_backup(DirectoryMode.DEVELOPER))

        # search game folders for relative file path
        for game_dir in game_file_directories:
            file_path = os.path.join(game_dir, relative_file_path)
            if is_synced:
                file_path = get_backup_path(file_path)

            if os.path.isfile(file_path):
                print(f"Get vanilla file: '{relative_file_path}'")
                return file_path

        # could not find file path in game folders. is a custom file
        print(f"No vanilla file available, custom file: '{relative_file_path}'")
        return True

    def is_custom_file(self, relative_file_path):
        """Search all game directories including the backup folder to find the file

        Note: use description's get_custom_file_status for cached result. Should be a lot faster"""

        vanilla_file = self.get_vanilla_file(relative_file_path)
        if vanilla_file:
            print(f"Vanilla file is available. Not a custom file: '{relative_file_path}'")
            return True
        else:
            print(f"Vanilla file is not available. Ccustom file: '{relative_file_path}'")
            return False

    def get_pak01_vpk_in(self, directory):
        "Verify if this is a game files directory by checking if it contains a pak01_dir.vpk file"
        pak01_filename = "pak01_dir.vpk"
        backup_pak01_filename = get_backup_filename(pak01_filename)
        required_files = [pak01_filename, backup_pak01_filename]

        for file in required_files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                return file_path

        return False

    def get(self, dir_mode):
        "Get directory"
        # set variables
        self.game._validate_dir_mode(dir_mode)
        id_filename = self.id._get_filename(dir_mode)
        steam_games_dir = self.game.steam.get_games_dir()

        # Search through folders in the Steam games directory
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                id_path = os.path.join(folder_path, id_filename)
                if os.path.isfile(id_path):
                    logger.debug(f"Found installation directory for mode '{dir_mode}': '{folder_path}'")
                    return folder_path

        print(f"No installation directory found for mode '{dir_mode}'.")
        return None

    def _get_active_mode(self):
        dev_dir = self.get(DirectoryMode.DEVELOPER)
        user_dir = self.get(DirectoryMode.USER)
        vanilla_dir = self.__get_vanilla_dir()

        if dev_dir == vanilla_dir:
            print(f"Active mode: {DirectoryMode.DEVELOPER.name}")
            return DirectoryMode.DEVELOPER
        elif user_dir == vanilla_dir:
            print(f"Active mode: {DirectoryMode.USER.name}")
            return DirectoryMode.USER
        else:
            print("No active mode found")
            return None

    def get_main_dir_name(self):
        "Retrieve main directory name. eg: 'left4dead2'"
        main_dir_name = self.game.get_title().replace(" ", "")
        main_dir_name = main_dir_name.lower()
        return main_dir_name

    def get_main_dir(self, dir_mode):
        "Get the full path to the main dir eg. 'Left 4 Dead 2\\left4dead2'"

        root_dir = self.get(dir_mode)
        if not os.path.isdir(root_dir):
            print(f"Unable to get {dir_mode.name} main directory. Directory unavailable")
            return None

        main_dir_name = self.get_main_dir_name()
        main_dir = os.path.join(root_dir, main_dir_name)

        # print(f"Get {dir_mode.name} main dir: {main_dir}")
        return main_dir

    def get_main_dir_backup(self, dir_mode):
        "Get the full path to the main dir backup eg. 'Left 4 Dead 2\\left4dead2.backup'"
        main_dir = self.get_main_dir(dir_mode)
        main_dir_backup = get_backup_path(main_dir)
        # print(f"Main directory backup: '{main_dir_backup}'")
        return main_dir_backup

    def _get_main_subdir(self, dir_mode, subdir_name):
        "Get the full path to a subdirectory within the main dir"

        main_dir = self.get_main_dir(dir_mode)
        subdir_path = os.path.join(main_dir, subdir_name)

        if not os.path.exists(subdir_path):
            raise FileNotFoundError(f"{subdir_path} directory not found for {dir_mode.name} mode")

        # print(f"Get {dir_mode.name} {subdir_name} dir: {subdir_path}")
        return subdir_path

    def _get_main_subdir_backup(self, dir_mode, subdir_name):
        """Get the full path to a subdirectory within the main dir backup:'Left 4 Dead 2\\left4dead2.backup\\materials'
        Not throwing an expection because installer uses this to create the backup folder"""

        main_dir_backup = self.get_main_dir_backup(dir_mode)
        subdir_backup_path = os.path.join(main_dir_backup, subdir_name)

        # print(f"Get {dir_mode.name} {subdir_name} dir: {subdir_backup_path}")
        return subdir_backup_path

    def get_cfg_dir(self, dir_mode):
        "Get the full path to the config dir eg. 'Left 4 Dead 2\\left4dead2\\cfg'"
        return self._get_main_subdir(dir_mode, "cfg")

    def _get_addons_dir(self, dir_mode):
        "Get the full path to the addons dir eg. 'Left 4 Dead 2\\left4dead2\\addons'"
        return self._get_main_subdir(dir_mode, "addons")

    def __get_vanilla_dir(self):
        """Get the vanilla directory path of the game"""
        
        # Get the games directory from the steam object of the game
        games_dir = self.game.steam.get_games_dir()
        # Get the title of the game
        title = self.game.get_title()

        # Construct and return the vanilla directory path
        vanilla_dir = os.path.join(games_dir, title)
        # print(f"Vanilla directory: {vanilla_dir}")
        return vanilla_dir

    def restore_developer_directory(self):
        "Restore developer game files using backup"
        print("Restoring developer game files")

        try:
            # receive variables
            main_dir_backup = self.game.dir.get_main_dir_backup(DirectoryMode.DEVELOPER)
            main_dir = self.game.dir.get_main_dir(DirectoryMode.DEVELOPER)

            main_dir_resource = self.game.dir._get_main_subdir(DirectoryMode.DEVELOPER, "resource")
            main_dir_materials = self.game.dir._get_main_subdir(DirectoryMode.DEVELOPER, "materials")

            # delete potentially beschmirched game directories
            shutil.rmtree(main_dir_resource)
            shutil.rmtree(main_dir_materials)

            # copy files
            copy_directory(main_dir_backup, main_dir)

            # update sync status
            self.id.set_sync_state(DirectoryMode.DEVELOPER, SyncState.NOT_SYNCED)

            print("Restored developer game files!")
            return True
        except Exception as err_info:
            raise Exception(f"Failed to restore game files!\n\n{err_info}") from err_info

    def check_for_invalid_id_file_structure(self):
        """
        Check for invalid ID file structures in the Steam game directory.

        This method searches for ID files (user and developer) within subdirectories of
        the Steam game directory and performs checks for invalid file structures.

        Raises:
            Exception: If two ID files are found in the same folder.
            Exception: If more than one of the same ID file is found in different folders.
        """
        steam_game_dir = self.steam.get_games_dir()

        user_id_file_name = self.game.dir.id._get_filename(DirectoryMode.USER)
        dev_id_file_name = self.game.dir.id._get_filename(DirectoryMode.DEVELOPER)

        id_files_in_folders = {}  # Dictionary to store ID files in each folder

        for game_dir in os.listdir(steam_game_dir):
            game_dir_path = os.path.join(steam_game_dir, game_dir)

            if os.path.isdir(game_dir_path):
                id_files_in_game_dir = []

                # Search for user and dev ID files in the current game directory
                for subdir_item in os.listdir(game_dir_path):
                    subdir_item_path = os.path.join(game_dir_path, subdir_item)

                    if os.path.isfile(subdir_item_path):
                        if subdir_item == user_id_file_name or subdir_item == dev_id_file_name:
                            id_files_in_game_dir.append(subdir_item)

                if id_files_in_game_dir:
                    id_files_in_folders[game_dir] = id_files_in_game_dir

        # Check for two ID files in the same folder
        for folder, id_files in id_files_in_folders.items():
            if len(id_files) > 1:
                raise Exception(f"Multiple ID files found in folder '{folder}': {', '.join(id_files)}")

        # Check for more than one of the same ID file in any folder
        id_counts = {}
        for id_files in id_files_in_folders.values():
            for id_file in id_files:
                if id_file not in id_counts:
                    id_counts[id_file] = 1
                else:
                    id_counts[id_file] += 1
                    if id_counts[id_file] > 1:
                        raise Exception(f"More than one '{id_file}' file found in different folders")

        print("Verified ID file structure!")

    def dev_out_of_date(self):
        "Check if the developer directory is out of date by comparing it agains the user directory"
        print("Checking if developer directory is outdated...")

        if not self.game.installation_exists(DirectoryMode.DEVELOPER):
            print("Unable to check outdated state: Developer mode is not installed!")
            return False

        user_pak01_subdirs = self.__get_pak01_vpk_subdirs(DirectoryMode.USER)
        dev_pak01_subdirs = self.__get_pak01_vpk_subdirs(DirectoryMode.DEVELOPER)

        for user_subdir, dev_subdir in zip(user_pak01_subdirs, dev_pak01_subdirs):
            user_pak01 = self.get_pak01_vpk_in(user_subdir)
            dev_pak01 = self.get_pak01_vpk_in(dev_subdir)

            if files_differ(user_pak01, dev_pak01):
                print("Developer directory is outdated!")
                return True
        print("Developer directory is up-to-date!")
        return False

    def __get_pak01_vpk_subdirs(self, dir_mode):
        "Retrieve subdirs with pak01's in them. Eg: left4dead2, left4dead2_dlc1, update"

        # variables
        pak01_subdirs = []
        game_dir = self.game.dir.get(dir_mode)

        # retrieve game folders to check
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            is_game_files_dir = self.get_pak01_vpk_in(subdir_path)

            if is_game_files_dir:
                pak01_subdirs.append(subdir_path)

        return pak01_subdirs
