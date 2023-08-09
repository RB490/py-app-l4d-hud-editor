"""Module for the hud browser gui class"""
import tkinter as tk
from tkinter import ttk
import keyboard
import win32gui

from packages.editor_menu.menu import EditorMenuClass
from packages.utils.functions import save_and_exit_script


class GuiHudBrowser:
    """Class for the hud browser gui"""

    def __init__(self, hud_instance, game_instance, persistent_data, start_instance):
        # pylint: disable=c-extension-no-member
        print("GuiHudBrowser")

        # set variables
        self.hud = hud_instance
        self.game = game_instance
        self.persistent_data = persistent_data
        self.root = tk.Tk()
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

        self.search_box = tk.Text(self.search_frame, height=1, wrap=None, width=110)
        self.search_box.pack(side="left", fill="x", expand=True, padx=5, pady=0)

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

        # Bind the search box to the search function
        self.search_box.bind("<KeyRelease>", self.search_treeview)

        # create a treeview with three columns
        self.treeview = ttk.Treeview(self.frame, columns=("file", "description", "custom"), height=15)
        self.treeview.heading("#0", text="")
        self.treeview.heading("file", text="File", anchor="w")
        self.treeview.heading("description", text="Description", anchor="w")
        self.treeview.heading("custom", text="Custom", anchor="w")
        self.treeview.column("#0", width=10, stretch=False)
        self.treeview.column("file", width=260, stretch=False)
        self.treeview.column("description", width=50)
        self.treeview.column("custom", width=50)
        self.treeview.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Create a Scrollbar widget
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")

        # Link the Scrollbar to the Treeview widget
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # editor menu
        self.my_editor_menu = EditorMenuClass(
            self, self.root, persistent_data, game_instance, hud_instance, start_instance, self
        )
        self.my_editor_menu.create_and_refresh_menu()

        # hotkeys
        keyboard.add_hotkey("F5", self.toggle_visibility, suppress=True)

        # set hwnd
        self.hwnd = win32gui.GetParent(self.frame.winfo_id())

        self.treeview_refresh(self.treeview)

        self.root.mainloop()
        # self.hide()

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

    def search_treeview(self, event):
        """Search treeview"""
        # pylint: disable=unused-argument

        # Retrieve the search term from the search box
        search_term = self.search_box.get("1.0", "end-1c")

        # Refresh the Treeview with the search term
        self.treeview_refresh(self.treeview, search_term=search_term if search_term else None)

    def treeview_refresh(self, treeview, search_term=None):
        """Clear treeview & load up-to-date content"""

        print(f"display choice: {self.display_choice.get()}")
        display_choice = self.display_choice.get().lower()
        if display_choice == "all":
            data_dict = self.hud.get_all_files_dict()
        else:
            data_dict = self.hud.get_files_dict()

        # check if there is anything to refresh
        if not data_dict:
            return

        # Clear existing items in the Treeview
        treeview.delete(*treeview.get_children())

        # Add items from the data_dict to the Treeview
        for key, value in data_dict.items():
            if (
                search_term
                and search_term.lower() not in str(key).lower()
                and search_term.lower() not in str(value).lower()
            ):
                # Skip this item if search term is provided and not found in key or value
                continue
            treeview.insert("", "end", values=(key, value))

    def save_window_geometry(self):
        """Save size & position"""
        # Get the current position and size of the window
        geometry = self.root.geometry()
        print(f"geometry: {geometry}")
        self.persistent_data["BrowserGuiGeometry"] = geometry

    def on_close(self):
        """Runs on close"""
        self.save_window_geometry()
        save_and_exit_script(self.persistent_data, self.hud)
