from game_v2.game_v2 import ID_FILE_NAMES


class GameV2Dir:
    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data
        print(self.__class__.__name__)
        # TODO write class

    def set(self, dir_mode):
        # TODO set directory to mode aka activate_mode / swap_mode_folders
        # TODO is dir_mode installed
        # TODO is dir_mode already activated?
        # TODO is dir_mode already activated?
        pass

    def get(self, dir_mode):
        # TODO get directory for mode AKA get_dir
        self.game.validate_dir_mode(dir_mode)

        id_filename = ID_FILE_NAMES[dir_mode]
        print(f"File name for {dir_mode.name}: {id_filename}")
