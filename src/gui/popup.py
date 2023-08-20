"""Module for the editor menu"""

import tkinter as tk

from game.game import Game
from hud.hud import Hud
from menu.menu import EditorMenuClass


class GuiEditorMenuPopupContextmenu:
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

    def __init__(self, persistent_data):
        """
        Initializes a new instance of the ToggleWindow class and runs the main event loop.
        """
        self.is_hidden = None
        self.root = tk.Tk()
        self.hide()
        # self.root.geometry("300x200")
        self.root.title("Hud Editor")
        # self.root.withdraw()
        self.persistent_data = persistent_data
        self.game = Game(persistent_data)
        self.hud = Hud(persistent_data)
        self.my_editor_menu = EditorMenuClass(self, self.root, persistent_data)
        self.my_editor_menu.create_and_refresh_menu()
        # keyboard.add_hotkey("F4", self.show_menu, suppress=True) # doesn't work nice - stays open when it loses focus
        # keyboard.add_hotkey("F5", self.toggle_visibility, suppress=True)

        # self.show_menu()

    def run(self):
        "Show & start main loop"

        self.show()
        self.root.mainloop()

    def show(self):
        """Show gui"""
        self.root.deiconify()
        self.is_hidden = False

    def hide(self):
        """Hide gui"""
        self.root.withdraw()
        self.is_hidden = True

    def toggle_visibility(self):
        """
        Toggles the visibility of the window between visible and hidden.

        If the window is not currently activated and focused, it will get focused before toggling visibility.
        Otherwise, if the window is currently hidden, it will be shown. If it is visible, it will be hidden.
        """
        print("toggle_visibility")

        # if not self.root.focus_get():
        # self.root.attributes("-topmost", True)
        # self.root.attributes("-topmost", False)
        # self.root.focus_force()
        # self.my_editor_menu.root.focus_force()
        # self.root.lift()  # bring the window to the front

        # window_title = self.root.title()
        # win = gw.getWindowsWithTitle(window_title)[0]
        # win.activate()

        # window_id = self.root.winfo_id()
        # hwnd = win32gui.GetParent(window_id)
        # print(hwnd)
        # bring_window_to_front(hwnd)
        # print("Focused Editor Gui")
        if self.is_hidden:
            self.root.deiconify()
            self.is_hidden = False
        else:
            self.root.withdraw()
            self.is_hidden = True

    def show_menu(self):
        """Show menu at mouse cursor"""
        pos_x, pos_y = self.root.winfo_pointerxy()
        self.my_editor_menu.menu_bar.post(pos_x, pos_y)


def debug_gui_editor_menu(persistent_data):
    """Debug gui class"""
    # pylint: disable=unused-variable
    app = GuiEditorMenuPopupContextmenu(persistent_data)
