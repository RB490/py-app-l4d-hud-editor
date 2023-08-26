"""Module for the hud select gui class"""
# pylint: disable=broad-exception-caught
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

from PIL import Image, ImageTk

from game.game import Game
from gui.base import BaseGUI
from hud.hud import Hud
from utils.constants import APP_ICON, IMAGES_DIR
from utils.persistent_data_manager import PersistentDataManager
from utils.shared_utils import Singleton
from utils.vpk import VPKClass


class GuiHudStart(BaseGUI, metaclass=Singleton):
    """Class for the hud select gui"""

    def __init__(self):
        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
        super().__init__()
        self.data_manager = PersistentDataManager()
        self.game = Game()
        self.hud = Hud()
        self.root.title("Select")
        self.root.iconbitmap(APP_ICON)
        self.root.minsize(865, 375)
        self.set_window_geometry(self.data_manager.get("HudSelectGuiGeometry"))

        # gui variables
        pad_x = 10
        pad_y = 10

        # initialize variables
        self.picture_canvas_photo = None
        self.selected_hud_name = ""
        self.selected_hud_dir = ""

        # Create image buttons
        self.add_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "medium", "plus.png")).subsample(2, 2)
        self.new_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "medium", "star.png")).subsample(2, 2)
        self.settings_image = tk.PhotoImage(
            file=os.path.join(IMAGES_DIR, "medium", "settings_hamburger.png")
        ).subsample(2, 2)

        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", anchor="nw", expand=True)

        # create a treeview with three columns
        self.treeview = ttk.Treeview(self.frame, columns=("name", "directory"), height=10)
        self.treeview.heading("#0", text="")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("directory", text="Directory")
        self.treeview.column("#0", width=10, stretch=False)
        self.treeview.column("name", width=125, stretch=False)
        self.treeview.column("directory", width=400)
        self.treeview.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_get_selected_item)

        # create a frame for the right panel
        self.right_panel = tk.Frame(self.frame)
        self.right_panel.pack(fill="both", anchor="nw", expand=True)

        # Developer menu
        developer_menu_button = tk.Button(self.right_panel, text="Developer", justify="center")
        developer_menu_button.config(width=70, height=25)
        developer_menu_button.config(image=self.settings_image, compound="left", padx=pad_x)
        developer_menu_button.pack(padx=pad_x, pady=(pad_y, pad_y))
        developer_menu_button.bind("<ButtonRelease-1>", self.show_developer_menu)

        # create a button above the picture frame
        self.add_button = tk.Button(self.right_panel, text="Add", height=25, command=self.prompt_add_hud_btn)
        self.add_button.pack(fill=tk.X, pady=5, padx=5)
        self.add_button.config(image=self.add_image, compound="left", padx=10)

        # create a button above the picture frame
        self.new_button = tk.Button(self.right_panel, text="New", height=25, command=self.prompt_new_hud_btn)
        self.new_button.pack(fill=tk.X, pady=5, padx=5)
        self.new_button.config(image=self.new_image, compound="left", padx=10)

        # create a frame for the edit controls
        self.edit_panel = tk.Frame(self.right_panel)
        self.edit_panel.pack(side="bottom", fill="both", anchor="se", expand=False)

        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.edit_panel, bg="black")
        self.picture_frame.pack(fill=tk.X, pady=5, padx=5)

        # Add the image viewport, display it in the picture frame and set the initial image
        self.picture_canvas = tk.Canvas(self.picture_frame, relief="groove", bd=3)
        self.picture_canvas.pack()
        self.picture_canvas.config(width=250, height=200)
        # setting the image isn't possible before calling mainloop()
        # self.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))

        # create a button above the picture frame
        self.edit_button = tk.Button(self.edit_panel, text="Edit", height=25, command=self.edit_selected_hud)
        self.edit_button.pack(fill=tk.X, pady=5, padx=5)
        self.edit_button.config(image=self.add_image, compound="left", padx=10)

        # Create a context menu for the treeview
        self.context_menu = tk.Menu(self.treeview, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.tree_edit_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Open dir", command=self.tree_open_dir)
        self.context_menu.add_command(label="Export VPK", command=self.tree_export_vpk)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Remove", command=self.tree_remove_item)

        # Bind the right-click event to show the context menu
        self.treeview.bind("<Button-3>", self.show_tree_context_menu)

        from menu.menu import EditorMenuClass

        self.my_editor_menu = EditorMenuClass(self, self.root)
        # self.my_editor_menu.create_and_refresh_menu_developer_installer() # add to the menubar
        self.dev_context_menu = self.my_editor_menu.get_developer_installer_menu(self.root)  # add as context menu

        # Configure the root window with the menubar
        self.update_treeview()

        self.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))

    def show(self):
        # destroy other main gui to prevent tkinter issues
        # from gui.browser import GuiHudBrowser
        # browser_gui = GuiHudBrowser()
        # browser_gui.destroy()

        self.root.deiconify()
        self.is_hidden = False
        self.root.mainloop()

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        self.data_manager.set("HudSelectGuiGeometry", self.get_window_geometry())

    def show_developer_menu(self, event):
        print("dev context menu!")
        self.dev_context_menu.post(event.x_root, event.y_root)

    def show_tree_context_menu(self, event):
        """Show the context menu for the treeview item at the position of the mouse cursor."""

        # select row under mouse
        iid = self.treeview.identify_row(event.y)
        if iid:
            # mouse pointer over item
            self.treeview.selection_set(iid)

        self.context_menu.post(event.x_root, event.y_root)

    def tree_edit_item(self):
        """Edit the selected hud."""
        self.edit_selected_hud()

    def tree_open_dir(self):
        """Open the directory of the selected hud."""
        print("Opening selected tree item directory")

        hud_dir = self.selected_hud_dir

        # Check if the source directory exists
        if os.path.exists(hud_dir):
            # Open the source directory in the file explorer
            subprocess.Popen(["explorer", hud_dir])
            print(f"Opened directory '{hud_dir}'")
        else:
            print(f"Directory '{hud_dir}' does not exist.")

    def tree_export_vpk(self):
        """Export the selected hud as a vpk file."""
        print("Exporting selected tree item as vpk")

        export_path = filedialog.asksaveasfilename(
            initialdir="/", title="Export HUD as VPK", filetypes=(("package files", "*.vpk"), ("all files", "*.*"))
        )

        if export_path:
            print(export_path)
            vpk_class = VPKClass()
            vpk_class.create(self.selected_hud_dir, os.path.dirname(export_path), os.path.basename(export_path))
            # vpk_class.create(self, input_dir, output_dir, output_file_name):

    def tree_remove_item(self):
        """Remove the selected hud."""
        print("Remove tree item")

        self.data_manager.get("stored_huds").remove(self.selected_hud_dir.replace("\\", "/"))  # convert path to json
        self.selected_hud_dir = ""
        self.selected_hud_name = ""

        self.update_treeview()

    def update_treeview(self):
        """Clear treeview & load up-to-date content"""

        # Clear the existing items in the Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Insert the new items from the list into the Treeview
        for stored_hud_dir in self.data_manager.get("stored_huds"):
            # retrieve hud name (from addoninfo.txt if available)
            hud_name = self.hud.manager.retrieve_hud_name_for_dir(stored_hud_dir)

            self.treeview.insert("", "end", values=(hud_name, os.path.normpath(stored_hud_dir)))

    def change_addon_image(self, path):
        """Load specified image into the image control"""
        image = Image.open(path)
        self.picture_canvas_photo = ImageTk.PhotoImage(image)

        # Calculate the center coordinates based on the canvas size
        center_x = self.picture_canvas.winfo_reqwidth() // 2
        center_y = self.picture_canvas.winfo_reqheight() // 2

        # Configure the canvas to display the image
        self.picture_canvas.create_image(center_x, center_y, anchor="center", image=self.picture_canvas_photo)

    # pylint: disable=unused-argument
    def tree_get_selected_item(self, event):
        """Get select item from treeview"""
        selected_item = self.treeview.selection()
        for item in selected_item:
            item_values = self.treeview.item(item)["values"]
            print(item_values)
            self.selected_hud_name = self.treeview.item(item)["values"][0]
            self.selected_hud_dir = os.path.normpath(self.treeview.item(item)["values"][1])
            image = os.path.join(self.selected_hud_dir, "addonimage.jpg")
            print(self.selected_hud_dir)
            print(self.selected_hud_name)

            self.change_addon_image(image)

    def prompt_add_hud_btn(self):
        """Prompt user for hud folder to add"""
        if self.hud.manager.prompt_add_existing_hud():
            self.update_treeview()

    def prompt_new_hud_btn(self):
        """Prompt user for hud folder to create a new hud in"""
        if self.hud.manager.prompt_create_new_hud():
            self.update_treeview()

    def edit_selected_hud(self):
        """Start hud editing for selected hud"""

        # hide gui
        self.hide()
        self.save_window_geometry()
        # self.destroy_gui()

        # edit hud
        self.hud.edit.start_editing(self.selected_hud_dir)


def debug_start_gui():
    "Show start gui"
    start_instance = GuiHudStart()
    start_instance.show()
