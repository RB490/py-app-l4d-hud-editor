"""Module containing editor menu methods for GuiEditorMenu to keep things organized"""


class EditorMenuHandler:
    """Class containing editor menu methods for GuiEditorMenu to keep things organized"""

    def __init__(self, parent, persistent_data, game_instance, hud_instance):
        # super().__init__()

        self.parent = parent
        self.persistent_data = persistent_data
        self.game = game_instance
        self.hud = hud_instance

        # Define any menu items and their associated commands here
        # self.add_command(label="File", command=self.file_command)

        print("MenuHandler")
