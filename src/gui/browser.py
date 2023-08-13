"""Module for the hud browser gui class"""
import os
import tkinter as tk
from tkinter import ttk

import keyboard
import win32gui

from editor_menu.menu import EditorMenuClass
from game.game import Game
from utils.constants import HOTKEY_TOGGLE_BROWSER
from utils.functions import save_and_exit_script
from utils.shared_utils import Singleton


class GuiHudBrowser(metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self, persistent_data):
        # pylint: disable=c-extension-no-member
        print("GuiHudBrowser")

        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
        from hud.hud import Hud

        # set variables
        self.hud = Hud(persistent_data)
        self.game = Game(persistent_data)
        self.root = tk.Tk()
        self.persistent_data = persistent_data
        self.root.title("Browser")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.minsize(300, 100)
        # self.root.wm_attributes("-topmost", 1)  # python can't focus windows so always on top it is
        self.is_hidden = False

        # load saved geometry
        try:
            geometry = self.persistent_data["BrowserGuiGeometry"]
            self.root.geometry(geometry)
        except KeyError:
            self.root.geometry("1000x1000+100+100")

        # draw controls
        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", anchor="nw", expand=True)

        # create a frame for search controls
        self.search_frame = tk.Frame(self.frame)
        self.search_frame.pack(side="top", fill="x", padx=5, pady=5)

        self.search_label = tk.Label(self.search_frame, text="Search")
        self.search_label.pack(side="left", padx=5, pady=5)

        self.search_box = tk.Text(self.search_frame, height=1, wrap=None, width=10)
        self.search_box.pack(side="left", fill="x", expand=True, padx=5, pady=0)
        self.search_box.bind("<KeyRelease>", self.treeview_search)

        # create Radiobuttons
        self.display_choice = tk.StringVar(value="Added")

        self.radio_1 = tk.Radiobutton(
            self.search_frame,
            text="Added",
            variable=self.display_choice,
            value="Added",
            command=self.handle_radio_click,
        )
        self.radio_1.pack(side="right", padx=5)

        self.radio_2 = tk.Radiobutton(
            self.search_frame, text="All", variable=self.display_choice, value="All", command=self.handle_radio_click
        )
        self.radio_2.pack(side="right", padx=5)

        # create a treeview with three columns
        self.treeview = ttk.Treeview(self.frame, columns=("file", "description", "custom", "path"), height=15)
        self.treeview.heading("#0", text="")
        self.treeview.heading("file", text="File", anchor="w")
        self.treeview.heading("description", text="Description", anchor="w")
        self.treeview.heading("custom", text="Custom", anchor="w")
        self.treeview.heading("path", text="Path", anchor="w")
        self.treeview.column("#0", width=10, stretch=False)
        self.treeview.column("file", width=260, stretch=False)
        self.treeview.column("description", width=50)
        self.treeview.column("custom", width=1)
        self.treeview.column("path", width=50)
        self.treeview.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        # self.treeview.bind("<<TreeviewSelect>>", self.treeview_on_click)
        self.treeview.bind("<Double-1>", self.treeview_on_double_click)

        # Create a Scrollbar widget
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")
        # Link the Scrollbar to the Treeview widget
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Create a context menu
        self.context_menu = tk.Menu(self.treeview, tearoff=False)

        # Add options to the context menu
        self.context_menu.add_command(label="Open File", command=self.dummy_handler)
        self.context_menu.add_command(label="Open Default File", command=self.dummy_handler)
        self.context_menu.add_command(label="Open Folder", command=self.dummy_handler)
        self.context_menu.add_command(label="Open Game Folder", command=self.dummy_handler)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Description", command=self.dummy_handler)
        self.context_menu.add_command(label="Integers", command=self.dummy_handler)
        self.context_menu.add_command(label="Describe", command=self.dummy_handler)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Recycle", command=self.dummy_handler)

        # Bind the context menu to the right-click event on the treeview
        self.treeview.bind("<Button-3>", self.treeview_show_context_menu)

        # editor menu
        self.my_editor_menu = EditorMenuClass(self, self.root, persistent_data)
        self.my_editor_menu.create_and_refresh_menu()

        # set hwnd
        self.hwnd = win32gui.GetParent(self.frame.winfo_id())

        self.treeview_refresh(self.treeview)

        self.hide()

    def run(self):
        "Show & start main loop"
        # hotkeys
        keyboard.add_hotkey(HOTKEY_TOGGLE_BROWSER, self.toggle_visibility, suppress=True)

        self.show()
        self.root.mainloop()

    def dummy_handler(self):
        "Dummy method"
        print("dummy")

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

        Because python can't focus windows (win32 has a function but it doesn't work, wow.) set it to always on top
        """
        if self.is_hidden:
            self.show()
        else:
            self.hide()

    def handle_radio_click(self):
        """Handle clicks on radio buttons."""
        display_choice = self.display_choice.get()
        # Do something with the selected choice, such as refreshing the UI
        print(f"Radio button clicked: {display_choice}")
        self.treeview_refresh(self.treeview)

    def treeview_search(self, event):
        """Search treeview"""
        # pylint: disable=unused-argument

        # Retrieve the search term from the search box
        search_term = self.search_box.get("1.0", "end-1c")

        # Refresh the Treeview with the search term
        self.treeview_refresh(self.treeview, search_term=search_term if search_term else None)

    def treeview_show_context_menu(self, event):
        """Treeview context menu"""

        # Identify the item clicked using event's coordinates
        item = self.treeview.identify_row(event.y)

        # Select the item (optional, but it visually indicates the clicked item)
        if item:
            self.treeview.selection_set(item)

        # Show the context menu at the event's coordinates
        self.context_menu.post(event.x_root, event.y_root)

    def treeview_get_selected_values(self):
        """Get a list of the values of the selected treeview row"""

        selection = self.treeview.selection()
        if not selection:
            return "No item selected"

        item = self.treeview.selection()[0]
        values = self.treeview.item(item)["values"]

        return values

    def treeview_get_selected_full_path(self):
        """Retrieve selected treeview row path"""
        relative_path = self.treeview_get_selected_values()[3]
        full_path = os.path.join(self.hud.get_dir(), relative_path)
        return full_path if full_path else "No item selected"

    def treeview_on_double_click(self, event):
        """Handle user clicks"""
        # pylint: disable=unused-argument

        file_path = self.treeview_get_selected_full_path()
        os.startfile(file_path)

    def treeview_refresh(self, treeview, search_term=None):
        """Clear treeview & load up-to-date content"""

        print(f"Treeview: Refreshing directory: '{self.hud.get_dir()}'")

        print(f"display choice: '{self.display_choice.get()}'")
        display_choice = self.display_choice.get().lower()
        if display_choice == "all":
            data_dict = self.hud.get_all_files_dict()
        else:
            data_dict = self.hud.get_files_dict()

        # check if there is anything to refresh
        if not data_dict:
            print("Treeview: No data to display")
            return

        # Clear existing items in the Treeview
        treeview.delete(*treeview.get_children())

        # Add items from the data_dict to the Treeview
        for file_name, desc_relpath_tuple in data_dict.items():
            file_desc = desc_relpath_tuple[0]
            file_relative_path = desc_relpath_tuple[1]
            if (
                search_term
                and search_term.lower() not in str(file_name).lower()
                and search_term.lower() not in str(file_desc).lower()
                and search_term.lower() not in str(file_relative_path).lower()
            ):
                # Skip this item if search term is provided and not found in key or value
                continue
            treeview.insert("", "end", values=(file_name, file_desc, "", file_relative_path))

        print("Treeview: Refreshed")

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        if self.root and self.root.winfo_viewable():
            # Get the current position and size of the window
            geometry = self.root.geometry()
            print(f"geometry: {geometry}")
            self.persistent_data["BrowserGuiGeometry"] = geometry
        else:
            print("GUI is not loaded or visible. Skipping window geometry save.")

    def destroy_gui(self):
        "Close & stop main loop"
        keyboard.remove_hotkey(HOTKEY_TOGGLE_BROWSER)
        self.save_window_geometry()
        self.root.destroy()

    def on_close(self):
        """Runs on close"""
        self.save_window_geometry()
        save_and_exit_script(self.persistent_data)


def get_debug_gui_browser_instance(persistent_data):
    "debug_gui_browser"
    print("debug_browser")
    return GuiHudBrowser(persistent_data)
