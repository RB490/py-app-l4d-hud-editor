class GameV2Installer:
    def __init__(self, game_class):
        self.game = game_class
        self.persistent_data = self.game.persistent_data
        print(self.__class__.__name__)
        # TODO write class
