"""Module for the editor menu"""
import keyboard

from game.game import Game
from gui.base import BaseGUI
from hud.hud import Hud
from menu.menu import EditorMenuClass
from shared_utils.shared_utils import Singleton
from utils.persistent_data_manager import PersistentDataManager


class GuiEditorMenuPopupContextmenu(BaseGUI, metaclass=Singleton):
    """
    A class representing a toggle window with hotkey functionality and a menu bar.

    Attributes:
        root (tkinter.Tk): The main window of the application.
        is_hidden (bool): A flag indicating whether the window is currently hidden.

    Methods:
        __init__(self): Initializes the ToggleWindow instance and runs the main event loop.
        toggle_visibility(self): Toggles the visibility of the window.
        setup_hotkey(self): Sets up the hotkey for toggling window visibility.
        create_menu(self): Creates the menu bar for the application.
        do_nothing(self): A dummy function that does nothing.
    """

    def __init__(self):
        """
        Initializes a new instance of the ToggleWindow class and runs the main event loop.
        """
        super().__init__(is_modal_dialog=True)
        self.root.title("Editor Context Menu Popup")
        self.set_transparency(0.5)
        self.set_decorations(False)

        self.data_manager = PersistentDataManager()
        self.game = Game()
        self.hud = Hud()
        self.my_editor_menu = EditorMenuClass(self, self.root)
        # self.my_editor_menu.create_and_refresh_menu()

        keyboard.add_hotkey("F4", self.show_menu, suppress=True)  # doesn't work nice - stays open when it loses focus
        keyboard.add_hotkey("F8", self.toggle_visibility, suppress=True)

        # self.show_menu()

    def show_menu(self):
        """Show menu at mouse cursor"""

        # Resize the GUI to the entire screen
        self.root.state("zoomed")

        self.my_editor_menu.create_and_refresh_menu(is_context_menu=True)

        pos_x, pos_y = self.root.winfo_pointerxy()
        self.my_editor_menu.menu_bar.post(pos_x, pos_y)

        self.hide()
