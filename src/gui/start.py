"""Module for the hud select gui class"""
# pylint: disable=broad-exception-caught, import-outside-toplevel
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
        right_panel_width = 204

        # initialize variables
        self.picture_canvas_photo = None
        self.selected_hud_name = ""
        self.selected_hud_dir = ""

        # Create image buttons
        self.edit_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "medium", "paintbrush.png")).subsample(2, 2)
        self.open_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "medium", "arrow_redo.png")).subsample(2, 2)
        self.saveas_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "medium", "save_as.png")).subsample(2, 2)
        self.delete_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "medium", "trash.png")).subsample(2, 2)
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
        self.treeview.pack(side="left", expand=True, fill="both", padx=pad_x, pady=(pad_y, pad_y))

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_get_selected_item)

        # create a frame for the right panel
        self.right_panel = tk.Frame(self.frame, bd=0, relief="solid")
        self.right_panel.pack(padx=(0, pad_x), pady=(pad_y, pad_y), fill="both", expand=True)

        # treeview button frame
        self.tree_btn_frame = tk.Frame(self.right_panel)
        self.tree_btn_frame.pack(fill="both", expand=True)

        # new or add label
        self.new_or_add_label = tk.Label(
            self.tree_btn_frame,
            text="Management",
            font=("Helvetica", 18),
            wraplength=99999999,
            padx=0,
            pady=0,  # Use a single value for padding at the top
            # relief="solid",
            # bd=1,
        )
        self.new_or_add_label.pack(fill="both")

        # treeview button frame
        self.new_or_add_frame = tk.Frame(self.tree_btn_frame, bd=0, relief="solid")
        self.new_or_add_frame.pack(pady=(5, 0))

        # create a button above the picture frame
        self.add_button = tk.Button(self.new_or_add_frame, text="Add", height=25, command=self.prompt_add_hud)
        self.add_button.config(image=self.add_image, compound="left", padx=10)
        self.add_button.config(width=(right_panel_width / 2) - 5, height=25)
        self.add_button.pack(padx=(0, 0), pady=(0, pad_y), side="right")

        # create a button above the picture frame
        self.new_button = tk.Button(self.new_or_add_frame, text="New", height=25, command=self.prompt_new_hud)
        self.new_button.config(image=self.new_image, compound="left", padx=10)
        self.new_button.config(width=(right_panel_width / 2), height=25)
        self.new_button.pack(padx=(0, 5), pady=(0, pad_y), side="left")

        # create a frame for the edit controls
        self.bottom_frame = tk.Frame(self.tree_btn_frame)
        self.bottom_frame.pack(side="bottom", fill="both", anchor="se", expand=False)

        # new or add label
        self.rem_op_ex_label = tk.Label(
            self.bottom_frame,
            text="Actions",
            font=("Helvetica", 18),
            wraplength=99999999,
            padx=0,
            pady=0,  # Use a single value for padding at the top
            # relief="solid",
            # bd=1,
        )
        self.rem_op_ex_label.pack(fill="both", pady=pad_y)

        # remove, open & export buttons frame
        self.rem_op_ex_frame = tk.Frame(self.bottom_frame, bd=0, relief="solid")
        self.rem_op_ex_frame.pack()

        # export vpk
        export_vpk_button = tk.Button(
            self.rem_op_ex_frame, text="Export", justify="center", command=self.selected_hud_export_vpk
        )
        export_vpk_button.config(image=self.saveas_image, compound="left", padx=pad_x)
        export_vpk_button.config(width=55, height=25)
        export_vpk_button.pack(padx=0, pady=0, side="left")

        # open dir
        open_dir_button = tk.Button(
            self.rem_op_ex_frame, text="Open", justify="center", command=self.selected_hud_open_dir
        )
        open_dir_button.config(image=self.open_image, compound="left", padx=pad_x)
        open_dir_button.config(width=55, height=25)  # Adjust the width as needed
        open_dir_button.pack(padx=(5, 5), pady=0, side="left")

        # Remove
        remove_button = tk.Button(
            self.rem_op_ex_frame, text="Remove", justify="center", command=self.selected_hud_remove_or_delete
        )
        remove_button.config(image=self.delete_image, compound="left", padx=pad_x)
        remove_button.config(width=55, height=25)
        remove_button.pack(padx=0, pady=0, side="left")

        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.bottom_frame, bd=0, relief="solid")  # bg="black"
        self.picture_frame.pack(fill=tk.X, padx=0, pady=(pad_y, pad_y))

        # Add the image viewport, display it in the picture frame and set the initial image
        self.picture_canvas = tk.Canvas(self.picture_frame, relief="groove", bd=3)
        # width + 16 because otherwise black bars around the canvas. possibly caused by the relief/border options
        self.picture_canvas.config(width=right_panel_width + 45, height=right_panel_width + 45)
        self.picture_canvas.pack()

        self.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))

        # Developer menu
        developer_menu_button = tk.Button(self.bottom_frame, text="Developer", justify="center")
        developer_menu_button.config(width=85, height=25)
        developer_menu_button.config(image=self.settings_image, compound="left", padx=pad_x)
        developer_menu_button.pack(padx=(0, 5), pady=0, side="left")
        developer_menu_button.bind("<ButtonRelease-1>", self.show_developer_menu)

        # create a button above the picture frame
        self.edit_button = tk.Button(self.bottom_frame, text="Edit", height=25, command=self.edit_selected_hud)
        self.edit_button.config(image=self.edit_image, compound="left", padx=10)
        self.edit_button.pack(fill=tk.X, padx=0, pady=0)

        # Create a context menu for the treeview
        self.context_menu = tk.Menu(self.treeview, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.selected_hud_start_editing)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Open dir", command=self.selected_hud_open_dir)
        self.context_menu.add_command(label="Export VPK", command=self.selected_hud_export_vpk)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Remove", command=self.selected_hud_remove_or_delete)

        # Bind the right-click event to show the context menu
        self.treeview.bind("<Button-3>", self.show_tree_context_menu)
        from menu.menu import EditorMenuClass

        self.my_editor_menu = EditorMenuClass(self, self.root)
        # self.my_editor_menu.create_and_refresh_menu_developer_installer() # add to the menubar
        self.dev_context_menu = self.my_editor_menu.get_developer_installer_menu(self.root)  # add as context menu

        # Configure the root window with the menubar
        self.update_treeview()

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
        """Open the developer context menu"""
        self.dev_context_menu.post(event.x_root, event.y_root)
        print("Opened the developer context menu!")

    def show_tree_context_menu(self, event):
        """Show the context menu for the treeview item at the position of the mouse cursor."""

        # select row under mouse
        iid = self.treeview.identify_row(event.y)
        if iid:
            # mouse pointer over item
            self.treeview.selection_set(iid)

        self.context_menu.post(event.x_root, event.y_root)

    def selected_hud_start_editing(self):
        """Edit the selected hud."""
        self.edit_selected_hud()

    def selected_hud_open_dir(self):
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

    def selected_hud_export_vpk(self):
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

    def selected_hud_remove_or_delete(self):
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

    def prompt_add_hud(self):
        """Prompt user for hud folder to add"""
        if self.hud.manager.prompt_add_existing_hud():
            self.update_treeview()

    def prompt_new_hud(self):
        """Prompt user for hud folder to create a new hud in"""
        if self.hud.manager.prompt_create_new_hud():
            self.update_treeview()

    def edit_selected_hud(self):
        """Start hud editing for selected hud"""

        # hide gui
        self.hide()
        self.save_window_geometry()

        # edit hud
        self.hud.edit.start_editing(self.selected_hud_dir)


def show_start_gui():
    "There can only be one main Tkinter GUI using root.mainloop() at oncee"
    from gui.browser import GuiHudBrowser

    # destroy other main gui
    browser_gui = GuiHudBrowser()
    browser_gui.destroy()

    start_gui = GuiHudStart()
    start_gui.show()

    print("Opened the Start GUI!")
    return start_gui
