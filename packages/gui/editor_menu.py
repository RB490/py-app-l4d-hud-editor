"""Module for the editor menu"""

import tkinter as tk

import keyboard


from packages.editor_menu.menu import EditorMenuClass


class GuiEditorMenu:
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

    def __init__(self, persistent_data, game_instance, hud_instance):
        """
        Initializes a new instance of the ToggleWindow class and runs the main event loop.
        """
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Hud Editor")
        # self.root.withdraw()
        self.is_hidden = False
        self.persistent_data = persistent_data
        self.game = game_instance
        self.hud = hud_instance
        self.my_editor_menu = EditorMenuClass(self, self.root, persistent_data, game_instance, hud_instance)
        self.my_editor_menu.create_and_refresh_menu()
        # keyboard.add_hotkey("F4", self.show_menu, suppress=True)
        keyboard.add_hotkey("F5", self.toggle_visibility, suppress=True)

        self.root.mainloop()

    def toggle_visibility(self):
        """
        Toggles the visibility of the window between visible and hidden.
        """
        print("toggle_visibility")
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


def debug_gui_editor_menu(persistent_data, game_instance, hud_instance):
    """Debug gui class"""
    # pylint: disable=unused-variable
    app = GuiEditorMenu(persistent_data, game_instance, hud_instance)
