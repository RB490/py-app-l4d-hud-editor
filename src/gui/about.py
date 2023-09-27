"""Class for the hud browser gui"""
import tkinter as tk
import webbrowser

from shared_gui.base import BaseGUI
from shared_utils.functions import Singleton

from src.utils.constants import APP_ICON, APP_NAME, APP_URL, DATA_MANAGER, VERSION_NO, VERSION_NO_GITHUB


class GuiAbout(BaseGUI, metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self, parent_root):
        # set variables
        self.settings_geometry_key = "GuiGeometryAbout"
        self.project_url = APP_URL
        self.data_manager = DATA_MANAGER

        # create gui
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.set_title("About")
        self.set_resizable(False)
        self.set_icon(APP_ICON)
        self.set_window_geometry(self.data_manager.get(self.settings_geometry_key))
        self.__create_widgets()

    def __create_widgets(self):
        # Create a label to display project information
        project_info_header = tk.Label(
            self.root,
            text=f"{APP_NAME} (Version {VERSION_NO})",
            padx=10,
            pady=10,
            font=("Helvetica", 11),
        )
        project_info_header.pack()

        project_info_latest_version_label = tk.Label(
            self.root,
            text=f"Github Version: {VERSION_NO_GITHUB}",
            padx=10,
            pady=10,
        )
        project_info_latest_version_label.pack()

        # Create and configure the synchronization hotkey button
        self.open_project_url_btn = tk.Button(
            self.root,
            text="Github Page",
            justify="center",
            command=self.open_main_page,
            state="normal",
            image=self.img.get("link.png", 2),
            compound="left",
            padx=10,
            width=125,
            height=25,
        )
        self.open_project_url_btn.pack(padx=10, pady=10)

    def open_main_page(self):
        """Open main page"""
        main_page_url = self.project_url
        webbrowser.open(main_page_url)


def main():
    root = tk.Tk()
    root.withdraw()
    gui = GuiAbout(root)
    gui.show()
    input("Press enter to exit program...")


if __name__ == "__main__":
    main()
