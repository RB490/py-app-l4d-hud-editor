class EditorMenuBase:
    """Base class for game map menu and game res menu"""

    def __init__(self, editor_menu_instance):
        instance_param_name = type(editor_menu_instance).__name__
        if instance_param_name is not "EditorMenuClass":
            raise ValueError("Specified param is not an instance of the editor menu class!")

        self.editor_menu_instance = editor_menu_instance
        self.data_manager = self.editor_menu_instance.data_manager
        self.parent_gui = self.editor_menu_instance.parent_gui
        self.handler = self.editor_menu_instance.handler
        self.img = self.editor_menu_instance.img
        self.game = self.editor_menu_instance.game

        from src.hud.hud import Hud

        self.hud = Hud()
