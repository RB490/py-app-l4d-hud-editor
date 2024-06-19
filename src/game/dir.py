"Game class directory methods"
# pylint: disable=protected-access, broad-exception-caught, broad-exception-raised, logging-fstring-interpolation
import functools
import os
import shutil

from loguru import logger
from shared_gui.splash_gui import SplashGUI
from shared_utils.functions import copy_directory, generate_random_string, is_valid_file_path_format, verify_directory

from src.game.constants import DirectoryMode, SyncState
from src.game.dir_id_handler import GameIDHandler
from src.hud.syncer import files_differ
from src.utils.functions import get_backup_filename, get_backup_path, get_start_gui, rename_with_timeout
from src.utils.steam_path_handler import SteamPathHandler


def raise_exception_if_invalid_path_format(func):
    "Check if hwnd is running"

    @functools.wraps(func)
    def wrapper(self, relative_file_path, *args, **kwargs):
        if not is_valid_file_path_format(relative_file_path):
            raise ValueError(f"Invalid path: {relative_file_path}")
        return func(self, relative_file_path, *args, **kwargs)

    return wrapper


class GameDir:
    "Game class directory methods"

    def __init__(self, game_class):
        self.game = game_class

        self.id = GameIDHandler(self.game)
        self.steam = SteamPathHandler()

    def _get_random_dir_name_for(self, dir_mode):
        random_string = generate_random_string()
        output = os.path.join(
            self.game.steam.get_games_dir(), f"_backup_hud_{dir_mode.name}.{self.game.get_title()}_{random_string}"
        )
        return output

    def set(self, dir_mode):
        """
        Set the directory to the specified mode.

        Args:
            dir_mode (DirectoryMode): The target directory mode to set.
        Returns:
            bool: True if the directory was successfully set; False otherwise.
        """
        self.game._validate_dir_mode(dir_mode)
        logger.debug(f"Setting mode: {dir_mode.name}")

        # Get source and target directories
        source_mode = DirectoryMode.USER if dir_mode == DirectoryMode.DEVELOPER else DirectoryMode.DEVELOPER
        source_dir = self.get(source_mode)
        target_dir = self.get(dir_mode)
        vanilla_dir = self.__get_vanilla_dir()

        # Set the rename timeout to 6
        rename_timeout = 6

        # Verify target directory
        if not verify_directory(target_dir, "Could not retrieve target directory!"):
            return False

        # Check if the target directory is already active
        if vanilla_dir and os.path.exists(vanilla_dir) and os.path.samefile(target_dir, vanilla_dir):
            logger.debug(f"{dir_mode.name} already active!")
            return True

        # Close the game
        self.game.window.close()

        # Rename vanilla folder if needed
        if vanilla_dir and os.path.isdir(vanilla_dir) and vanilla_dir != source_dir and vanilla_dir != target_dir:
            random_string = generate_random_string()
            vanilla_dir_renamed = vanilla_dir + random_string
            if not rename_with_timeout(vanilla_dir, vanilla_dir_renamed, rename_timeout):
                return False

        # Verify and rename source directory if source_dir == vanilla_dir
        if source_dir == vanilla_dir:
            if vanilla_dir and not verify_directory(vanilla_dir, "Could not retrieve vanilla directory!"):
                return False
            source_dir_backup = self._get_random_dir_name_for(source_mode)
            if not rename_with_timeout(source_dir, source_dir_backup, rename_timeout):
                return False

        # Activate the target mode
        if not rename_with_timeout(target_dir, vanilla_dir, rename_timeout):
            return False

        return True

    @raise_exception_if_invalid_path_format
    def get_vanilla_file(self, relative_file_path):
        """Search all game directories including the backup folder to find the file"""

        is_synced = False
        if self.game.dir.id.get_sync_state(DirectoryMode.DEVELOPER) == SyncState.SYNCED:
            is_synced = True

        # variables
        # retrieve game folders to check
        game_dir = self.game.dir.get(DirectoryMode.DEVELOPER)
        game_file_directories = self._get_pak01_vpk_subdirs(DirectoryMode.DEVELOPER)
        # add backup directory last so it's searched last so the code preferably returns file in the main directory
        game_file_directories.append(get_backup_path(self.get_main_dir(DirectoryMode.DEVELOPER)))

        # verify variables
        if not game_dir or not os.path.exists(game_dir):
            raise FileNotFoundError(f"Game dir '{game_dir}' is None or does not exist")

        if len(game_file_directories) < 1:
            raise ValueError(f"The list game_file_directories must contain at least one item: {game_file_directories}")

        # search game folders for relative file path
        for game_dir in game_file_directories:
            file_path = os.path.join(game_dir, relative_file_path)
            if is_synced:
                backup_file_path = get_backup_path(file_path)
                if os.path.isfile(backup_file_path):
                    file_path = backup_file_path

            if os.path.isfile(file_path):
                logger.debug(f"Get vanilla file: '{relative_file_path}'")
                return file_path

        # could not find file path in game folders. is a custom file
        logger.debug(f"No vanilla file available, custom file: '{relative_file_path}'")
        return False

    @raise_exception_if_invalid_path_format
    def is_custom_file(self, relative_file_path):
        """Search all game directories including the backup folder to find the file

        Note: use description's get_custom_file_status for cached result. Should be a lot faster"""
        vanilla_file = self.get_vanilla_file(relative_file_path)
        if vanilla_file:
            logger.debug(f"Vanilla file is available. Not a custom file: '{relative_file_path}'")
            return False
        else:
            logger.debug(f"Vanilla file is not available. Custom file: '{relative_file_path}'")
            return True

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
        id_filename = self.id.get_file_name(dir_mode)
        steam_games_dir = self.game.steam.get_games_dir()

        # Search through folders in the Steam games directory
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                id_path = os.path.join(folder_path, id_filename)
                if os.path.isfile(id_path):
                    logger.debug(f"Found installation directory for mode '{dir_mode}': '{folder_path}'")
                    return folder_path

        logger.debug(f"No installation directory found for mode '{dir_mode}'.")
        return None

    def get_active_mode(self):
        """User or developer mode is active"""
        dev_dir = self.get(DirectoryMode.DEVELOPER)
        user_dir = self.get(DirectoryMode.USER)
        vanilla_dir = self.__get_vanilla_dir()

        if dev_dir == vanilla_dir:
            logger.debug(f"Active mode: {DirectoryMode.DEVELOPER.name}")
            return DirectoryMode.DEVELOPER
        elif user_dir == vanilla_dir:
            logger.debug(f"Active mode: {DirectoryMode.USER.name}")
            return DirectoryMode.USER
        else:
            logger.debug("No active mode found")
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
            logger.debug(f"Unable to get {dir_mode.name} main directory. Directory unavailable")
            return None

        main_dir_name = self.get_main_dir_name()
        main_dir = os.path.join(root_dir, main_dir_name)

        logger.debug(f"Get {dir_mode.name} main dir: {main_dir}")
        return main_dir

    def get_subdir(self, subdir, subdir_name):
        "Get the full path to a subdirectory within the main dir"

        subdir_path = os.path.join(subdir, subdir_name)

        if not os.path.exists(subdir_path):
            raise FileNotFoundError(f"{subdir_name} subdir not found in {subdir}")

        logger.debug(f"Get {subdir_name} in dir: {subdir}")
        return subdir_path

    def get_main_subdir(self, dir_mode, subdir_name):
        "Get the full path to a subdirectory within the main dir"

        main_dir = self.get_main_dir(dir_mode)
        subdir_path = os.path.join(main_dir, subdir_name)

        if not os.path.exists(subdir_path):
            raise FileNotFoundError(f"{subdir_path} directory not found for {dir_mode.name} mode")

        logger.debug(f"Get {dir_mode.name} {subdir_name} dir: {subdir_path}")
        return subdir_path

    def __get_vanilla_dir(self):
        """Get the vanilla directory path of the game"""

        # Get the games directory from the steam object of the game
        games_dir = self.game.steam.get_games_dir()
        # Get the title of the game
        title = self.game.get_title()

        # Construct and return the vanilla directory path
        vanilla_dir = os.path.join(games_dir, title)
        logger.debug(f"Vanilla directory: {vanilla_dir}")
        return vanilla_dir

    def restore_developer_directory(self):
        "Restore developer game files using backup"

        logger.debug("Restoring developer game files")

        try:
            splash = SplashGUI(get_start_gui().root)
            splash.splash("Restoring...", "Restoring game files..")

            dev_pak01_subdirs = self._get_pak01_vpk_subdirs(DirectoryMode.DEVELOPER)

            for pak01_dir in dev_pak01_subdirs:
                # variables
                backup_dir = get_backup_path(pak01_dir)

                resource_dir = self.game.dir.get_subdir(pak01_dir, "resource")
                materials_dir = self.game.dir.get_subdir(pak01_dir, "materials")

                # delete potentially beschmirched game directories
                shutil.rmtree(resource_dir)
                shutil.rmtree(materials_dir)

                # restore backup
                copy_directory(backup_dir, pak01_dir)

            # update sync status
            self.id.set_sync_state(DirectoryMode.DEVELOPER, SyncState.NOT_SYNCED)

            # finish up
            splash.destroy()
            logger.warning("Restored developer game files!")
            return True
        except Exception as err_info:
            splash.destroy()
            raise Exception(f"Failed to restore game files!\n\n{err_info}") from err_info

    def disable_any_enabled_pak01s(self):
        """Check if developer directory has any pak01's enabled"""
        logger.debug("Disabling all pak01_dir.vpk's...")

        if not self.game.is_installed(DirectoryMode.DEVELOPER):
            logger.warning("Unable to disable pak01_dir.vpk's: Developer mode is not installed!")
            return None

        dev_pak01_subdirs = self._get_pak01_vpk_subdirs(DirectoryMode.DEVELOPER)

        for dev_subdir in dev_pak01_subdirs:
            file_path = self.get_pak01_vpk_in(dev_subdir)
            file_name = os.path.basename(file_path)

            disabled_file_path = os.path.join(os.path.dirname(file_path), "pak01_dir.vpk")
            disabled_file_path = get_backup_path(disabled_file_path)

            if file_name == "pak01_dir.vpk":
                # Rename the file
                os.rename(file_path, disabled_file_path)
                logger.info(f"Disabled pak01_dir.vpk! '{file_path}' -> '{disabled_file_path}'")

        logger.debug("All developer directory pak01_dir.vpk's are disabled!")
        return False

    def check_for_invalid_id_file_structure(self):
        """
        Check for invalid ID file structures in the Steam game directory.

        This method searches for ID files (user and developer) within subdirectories of
        the Steam game directory and performs checks for invalid file structures.

        Raises:
            Exception: If two ID files are found in the same folder.
            Exception: If more than one of the same ID file is found in different folders.
        """
        if not self.game.is_installed(DirectoryMode.DEVELOPER):
            logger.warning("Developer mode is not fully installed! (Unable to check if any pak01s are enabled)")
            return None
        if not self.game.is_installed(DirectoryMode.USER):
            logger.warning("User mode is not fully installed! (Unable to check if any pak01s are enabled)")
            return None
        steam_game_dir = self.steam.get_games_dir()

        user_id_file_name = self.game.dir.id.get_file_name(DirectoryMode.USER)
        dev_id_file_name = self.game.dir.id.get_file_name(DirectoryMode.DEVELOPER)

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

        logger.debug("Verified ID file structure!")

    def dev_out_of_date(self):
        "Check if the developer directory is out of date by comparing it agains the user directory"
        logger.debug("Checking if developer directory is outdated...")

        if not self.game.is_installed(DirectoryMode.DEVELOPER):
            logger.debug("Unable to check outdated state: Developer mode is not fully installed!")
            return None

        user_pak01_subdirs = self._get_pak01_vpk_subdirs(DirectoryMode.USER)
        dev_pak01_subdirs = self._get_pak01_vpk_subdirs(DirectoryMode.DEVELOPER)

        for user_subdir, dev_subdir in zip(user_pak01_subdirs, dev_pak01_subdirs):
            user_pak01 = self.get_pak01_vpk_in(user_subdir)
            dev_pak01 = self.get_pak01_vpk_in(dev_subdir)

            if files_differ(user_pak01, dev_pak01):
                logger.debug("Developer directory is outdated!")
                return True
        logger.debug("Developer directory is up-to-date!")
        return False

    def _get_pak01_vpk_subdirs(self, dir_mode):
        "Retrieve subdirs with pak01's in them. Eg: left4dead2, left4dead2_dlc1, update"

        result = self._get_pak01_dirs_with_files(dir_mode)

        # Extract the directory paths from the list of tuples
        directories = [item[0] for item in result]

        return directories

    def _get_pak01_dirs_with_files(self, dir_mode):
        "Retrieve subdirs with pak01's in them along with the corresponding pak01 file."

        # variables
        game_dir = self.game.dir.get(dir_mode)

        # create a list to store tuples of subdir paths and their corresponding pak01 file paths
        subdir_file_mapping = []

        # retrieve game folders to check
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            pak01_file_path = self.get_pak01_vpk_in(subdir_path)

            if pak01_file_path:
                subdir_file_mapping.append((subdir_path, pak01_file_path))

        return subdir_file_mapping

    def _find_resource_recursive(self, current_dir, target_file, root_dir):
        for root, _, files in os.walk(current_dir):
            logger.debug(f"Searching in directory: {root}")
            if target_file in files:
                resource_path = os.path.relpath(os.path.join(root, target_file), root_dir)
                logger.info(f"Found '{target_file}' at: {resource_path}")
                return resource_path
        return None
