import os
import tkinter as tk
import json

from modules.utils.constants import MISC_DIR


class MenuGUI(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.title("Show panel")
        self.data = data
        self.game_version = "L4D2"
        # Create command function using create_lambda_command
        self.lambda_cmd_func = self.create_lambda_command(self.editor_menu_show_panel)

        # Create menu items
        self.menu = tk.Menu(self, tearoff=0)

        # Create general menu and add common options
        show_panel_menu = tk.Menu(self.menu, tearoff=0)
        for key, value in self.data["general"].items():
            show_panel_menu.add_command(
                label=key, command=self.create_lambda_command(self.editor_menu_show_panel, value)
            )

        # Check GAME_VERSION to determine which L4D-specific options to add
        if self.game_version == "L4D1":
            show_panel_game_version_data = self.data.get("L4D1", {})
        elif self.game_version == "L4D2":
            show_panel_game_version_data = self.data.get("L4D2", {})
        else:
            show_panel_game_version_data = {}

        # Add L4D-specific options to general menu
        for key, value in show_panel_game_version_data.items():
            show_panel_menu.add_command(
                label=key, command=self.create_lambda_command(self.editor_menu_show_panel, value)
            )

        # Add all menus under a single "General" option
        self.menu.add_cascade(label="Show panel", menu=show_panel_menu)

        self.config(menu=self.menu)

    def create_lambda_command(self, func, *args):
        return lambda: func(*args)

    def editor_menu_show_panel(self, panel):
        # Do something with the panel value (e.g. print it)
        print(panel)


if __name__ == "__main__":
    # Open and read file
    with open(os.path.join(MISC_DIR, "gui_editor_menu_show_panels.json"), "r") as f:
        in_data = json.load(f)

    # Use 'data' variable in your code
    menu_gui = MenuGUI(in_data)
    menu_gui.mainloop()
