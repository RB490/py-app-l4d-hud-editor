"Game class directory methods"
# pylint: disable=protected-access, broad-exception-caught, broad-exception-raised
import os
import shutil

from game.constants import DirectoryMode
from game.dir_id_handler import GameIDHandler
from hud.syncer import files_differ
from utils.functions import (
    copy_directory,
    generate_random_string,
    get_backup_filename,
    get_backup_path,
    rename_with_timeout,
)
from utils.shared_utils import verify_directory


class GameDir:
    "Game class directory methods"

    def __init__(self, game_class):
        self.game = game_class
        # pylint: disable=invalid-name
        self.id = GameIDHandler(self.game)

    def _get_dir_backup_name(self, dir_mode):
        random_string = generate_random_string()
        output = os.path.join(
            self.game.steam.get_games_dir(), f"_backup_hud_{dir_mode.name}.{self.game.get_title()}_{random_string}"
        )
        return output

    def set(self, dir_mode):
        "Set directory to mode"
        self.game._validate_dir_mode(dir_mode)
        print(f"Setting mode: {dir_mode.name}")

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
            print(f"{target_mode.name} already active!")
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

    def is_custom_file(self, relative_file_path):
        """Search all game directories including the backup folder to find the file"""

        # variables
        game_file_directories = []
        game_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        # retrieve game folders to check
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            is_game_files_dir = self.get_pak01_vpk_in(subdir_path)
            if is_game_files_dir:
                game_file_directories.append(subdir_path)
        # add backup directory last so it's searched last so the code preferably returns file in the main directory
        game_file_directories.append(self.game.dir.get_main_dir_backup(DirectoryMode.DEVELOPER))

        # search game folders for relative file path
        for game_dir in game_file_directories:
            file_path = os.path.join(game_dir, relative_file_path)
            if os.path.isfile(file_path):
                print(f"Not a custom file: '{relative_file_path}'")
                return False

        # could not find file path in game folders. is a custom file
        print(f"Is a custom file: '{relative_file_path}'")
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
        id_filename = self.id._get_filename(dir_mode)
        steam_games_dir = self.game.steam.get_games_dir()

        # Search through folders in the Steam games directory
        for folder_name in os.listdir(steam_games_dir):
            folder_path = os.path.join(steam_games_dir, folder_name)
            if os.path.isdir(folder_path):
                id_path = os.path.join(folder_path, id_filename)
                if os.path.isfile(id_path):
                    print(f"Found installation directory for mode '{dir_mode}': '{folder_path}'")
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

        print(f"Get {dir_mode.name} main dir: {main_dir}")
        return main_dir

    def get_main_dir_backup(self, dir_mode):
        "Get the full path to the main dir backup eg. 'Left 4 Dead 2\\left4dead2.backup'"
        main_dir = self.get_main_dir(dir_mode)
        main_dir_backup = get_backup_path(main_dir)
        print(f"Main directory backup: '{main_dir_backup}'")
        return main_dir_backup

    def _get_main_subdir(self, dir_mode, subdir_name):
        "Get the full path to a subdirectory within the main dir"

        main_dir = self.get_main_dir(dir_mode)
        subdir_path = os.path.join(main_dir, subdir_name)

        if not os.path.exists(subdir_path):
            raise FileNotFoundError(f"{subdir_path} directory not found for {dir_mode.name} mode")

        print(f"Get {dir_mode.name} {subdir_name} dir: {subdir_path}")
        return subdir_path

    def _get_main_subdir_backup(self, dir_mode, subdir_name):
        "Get the full path to a subdirectory within the main dir backup: 'Left 4 Dead 2\\left4dead2.backup\\materials'"

        main_dir_backup = self.get_main_dir_backup(dir_mode)
        subdir_backup_path = os.path.join(main_dir_backup, subdir_name)

        if not os.path.exists(subdir_backup_path):
            raise FileNotFoundError(f"{subdir_backup_path} directory not found for {dir_mode.name} mode")

        print(f"Get {dir_mode.name} {subdir_name} dir: {subdir_backup_path}")
        return subdir_backup_path

    def get_cfg_dir(self, dir_mode):
        "Get the full path to the config dir eg. 'Left 4 Dead 2\\left4dead2\\cfg'"
        return self._get_main_subdir(dir_mode, "cfg")

    def _get_addons_dir(self, dir_mode):
        "Get the full path to the addons dir eg. 'Left 4 Dead 2\\left4dead2\\addons'"
        return self._get_main_subdir(dir_mode, "addons")

    def __get_vanilla_dir(self):
        """Get the vanilla directory path of the game"""
        print("Getting vanilla directory path...")

        # Get the games directory from the steam object of the game
        games_dir = self.game.steam.get_games_dir()
        # Get the title of the game
        title = self.game.get_title()

        # Construct and return the vanilla directory path
        vanilla_dir = os.path.join(games_dir, title)
        print(f"Vanilla directory: {vanilla_dir}")
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

            print("Restored develoer game files!")
            return True
        except Exception as err_info:
            raise Exception(f"Failed to restore game files!\n\n{err_info}") from err_info

    def dev_out_of_date(self):
        "Check if the developer directory is out of date by comparing it agains the user directory"
        print("hi there!")

        # Retrieve all pak01's and compare them between the dev & user directories, possibly even all paks although not needed & i should i have funcs to do this already

        if not self.game.installation_exists(DirectoryMode.DEVELOPER):
            print("Developer mode is not out of date because it's not installed!")
            return False

        # variables
        game_file_directories = []
        game_dir = self.game.dir.get(DirectoryMode.DEVELOPER)

        # retrieve game folders to check
        for subdir_name in os.listdir(game_dir):
            subdir_path = os.path.join(game_dir, subdir_name)
            is_game_files_dir = self.get_pak01_vpk_in(subdir_path)

            print(is_game_files_dir)

            if is_game_files_dir:
                game_file_directories.append(subdir_path)

        # return files_differ(file1, file2)
