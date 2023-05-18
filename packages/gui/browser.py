"""Module for the hud browser gui class"""
import tkinter as tk
from tkinter import ttk

from packages.editor_menu.menu import EditorMenuClass


class GuiHudBrowser:
    """Class for the hud browser gui"""

    def __init__(self, hud_instance, game_instance, persistent_data):
        print("GuiHudBrowser")

        # set variables
        self.hud = hud_instance
        self.game = game_instance
        self.persistent_data = persistent_data
        self.root = tk.Tk()
        self.root.title("Browser")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.minsize(300, 100)

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
        self.my_editor_menu = EditorMenuClass(self, self.root, persistent_data, game_instance, hud_instance)
        self.my_editor_menu.create_and_refresh_menu()

        # draw controls
        # self.Add("Text", "section", "Search")
        # self._fileFilterRadio = self.Add("radio", f"xs+{self.width - 90} ys", "All", self.Radio_Handler.Bind(self))
        # self._fileFilterRadio = self.Add("radio", "x+5 Checked", "Added", self.Radio_Handler.Bind(self))
        # self._searchEdit = self.Add("edit", f"xs w{self.width}", "", self.Lv_Refresh.Bind(self))
        # self.Lv = self.ListView(
        #     self, f"w{self.width} r20 AltSubmit -LV0x10", "File|Description|Path", self.Lv_Handler.Bind(self)
        # )

        self.treeview_refresh(self.treeview)

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
        if not data_dict or not len(data_dict):
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

    def on_close(self):
        """Runs on close"""
        print("on_close")
