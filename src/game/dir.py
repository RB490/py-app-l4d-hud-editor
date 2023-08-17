"Game class directory methods"
# pylint: disable=protected-access, broad-exception-caught
import os

from game.constants import DirectoryMode
from game.dir_id_handler import GameIDHandler
from utils.functions import generate_random_string, rename_with_timeout


class GameDir:
    "Game class directory methods"

    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data
        # pylint: disable=invalid-name
        self.id = GameIDHandler(self.game)

        print(self.__class__.__name__)

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
        rename_timeout = 3
        # variables - source
        source_mode = DirectoryMode.USER if dir_mode == DirectoryMode.DEVELOPER else DirectoryMode.DEVELOPER
        source_dir = self.get(source_mode)
        source_dir_backup = self._get_dir_backup_name(source_mode)
        # variables - target
        target_mode = dir_mode
        target_dir = self.get(target_mode)
        vanilla_dir = self.__get_vanilla()

        # do we need to swap?
        if os.path.exists(vanilla_dir) and os.path.samefile(target_dir, vanilla_dir):
            print(f"{target_mode.name} already active!")
            return True

        # close game
        self.game.close()

        # backup source mode
        print(f"Renaming {source_dir} -> {source_dir_backup}")
        if not rename_with_timeout(source_dir, source_dir_backup, rename_timeout):
            print(f"Failed to rename {source_dir} -> {source_dir_backup}")
            return False

        # activate target mode
        print(f"Renaming {target_dir} -> {vanilla_dir}")
        if not rename_with_timeout(target_dir, vanilla_dir, rename_timeout):
            print(f"Failed to rename {target_dir} -> {vanilla_dir}")
            return False

        print(f"Set mode: {dir_mode.name} successfully!")
        return True

    def get(self, dir_mode):
        "Get directory"
        # set variables
        self.game._validate_dir_mode(dir_mode)
        id_filename = self.id._get_id_filename(dir_mode)
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
        vanilla_dir = self.__get_vanilla()

        if dev_dir == vanilla_dir:
            print(f"Active mode: {DirectoryMode.DEVELOPER.name}")
            return DirectoryMode.DEVELOPER
        elif user_dir == vanilla_dir:
            print(f"Active mode: {DirectoryMode.USER.name}")
            return DirectoryMode.USER
        else:
            print("No active mode found")
            return None

    def get_main_dir(self, dir_mode):
        "Get the full path to the main dir eg. 'Left 4 Dead 2\\left4dead2'"

        root_dir = self.get(dir_mode)
        main_dir_name = self.game.get_title().replace(" ", "")
        main_dir_name = main_dir_name.lower()  # python is case sensitive; convert to Left4Dead2 -> left4dead2
        main_dir = os.path.join(root_dir, main_dir_name)

        print(f"Get {dir_mode.name} main dir: {main_dir}")
        return main_dir

    def get_main_dir_backup(self, dir_mode):
        "Get the full path to the main dir backup eg. 'Left 4 Dead 2\\_backup_left4dead2_'"
        main_dir = self.get_main_dir(dir_mode)
        main_dir_name = os.path.basename(os.path.dirname(main_dir))
        main_dir_backup_name = f"_backup_{main_dir_name}_"
        main_dir_backup = os.path.join(main_dir, main_dir_backup_name)
        print(f"Main directory backup: '{main_dir_backup}'")
        return main_dir_backup

    def get_main_dir_backup_resource(self, dir_mode):
        "Get the full path to the main dir backup eg. 'Left 4 Dead 2\\_backup_left4dead2_\\resource'"
        resource_backup_dir = os.path.join(self.get_main_dir_backup(dir_mode), "resource")
        print(f"Resource backup directory: '{resource_backup_dir}'")
        return resource_backup_dir

    def get_main_dir_backup_materials(self, dir_mode):
        "Get the full path to the main dir backup eg. 'Left 4 Dead 2\\_backup_left4dead2_\\materials'"
        materials_backup_dir = os.path.join(self.get_main_dir_backup(dir_mode), "materials")
        print(f"Materials backup directory: '{materials_backup_dir}'")
        return materials_backup_dir

    def __get_main_sub_dir(self, dir_mode, subdirectory):
        "Get the full path to the specified subdirectory (cfg or addons)"

        main_dir = self.get_main_dir(dir_mode)
        dir_path = os.path.join(main_dir, subdirectory)

        if not os.path.exists(dir_path):
            raise FileNotFoundError(f"{subdirectory} directory not found for {dir_mode.name} mode")

        print(f"Get {dir_mode.name} {subdirectory} dir: {dir_path}")
        return dir_path

    def get_cfg_dir(self, dir_mode):
        "Get the full path to the config dir eg. 'Left 4 Dead 2\\cfg'"
        return self.__get_main_sub_dir(dir_mode, "cfg")

    def _get_addons_dir(self, dir_mode):
        "Get the full path to the addons dir eg. 'Left 4 Dead 2\\addons'"
        return self.__get_main_sub_dir(dir_mode, "addons")

    def __get_vanilla(self):
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
