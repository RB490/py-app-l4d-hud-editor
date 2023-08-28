"""Module for the hud select gui class"""
# pylint: disable=broad-exception-caught, import-outside-toplevel, arguments-differ, broad-exception-raised
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

import keyboard
import send2trash
from PIL import Image, ImageTk

from game.game import Game
from gui.base import BaseGUI
from gui.browser import GuiHudBrowser
from hud.hud import Hud
from shared_utils.shared_utils import Singleton, show_message
from shared_utils.show_custom_prompt import show_custom_prompt
from utils.constants import APP_ICON, IMAGES_DIR_128, ImageConstants
from utils.functions import copy_directory
from utils.persistent_data_manager import PersistentDataManager
from utils.vpk import VPKClass


class GuiHudStart(BaseGUI, metaclass=Singleton):
    """Class for the hud select gui"""

    def __init__(self):
        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
        super().__init__()
        self.img = ImageConstants()
        self.data_manager = PersistentDataManager()
        self.game = Game()
        self.hud = Hud()
        self.root.title("Select")
        self.root.iconbitmap(APP_ICON)
        self.root.minsize(865, 500)
        self.set_window_geometry(self.data_manager.get("HudSelectGuiGeometry"))
        self.browser = GuiHudBrowser(self.root)

        self.__create_widgets()
        self.__create_context_menu()

        self.change_addon_image(os.path.join(IMAGES_DIR_128, "cross.png"))

        # Bind the right-click event to show the context menu
        self.treeview.bind("<Button-3>", self.show_tree_context_menu)

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_set_selected_item)

        from menu.menu import EditorMenuClass

        self.my_editor_menu = EditorMenuClass(self, self.root)
        # self.my_editor_menu.create_and_refresh_menu_developer_installer() # add to the menubar
        self.dev_context_menu = self.my_editor_menu.get_developer_installer_menu(self.root)  # add as context menu

        # Configure the root window with the menubar
        self.update_treeview()

        # Debug hotkeys
        keyboard.add_hotkey("F9", self.start_debug_method, suppress=True)  # TODO disable debug hotkey

    def start_debug_method(self):
        print("start_debug_method")
        # get_browser_gui()

    def __create_widgets(self):
        # gui variables
        self.pad_x = 10
        self.pad_y = 10
        self.right_panel_width = 204

        # initialize variables
        self.picture_canvas_photo = None
        self.selected_hud_name = ""
        self.selected_hud_dir = ""

        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", anchor="nw", expand=True)

        self.__create_treeview()
        self.__create_right_panel()

    def __create_treeview(self):
        # pylint: disable=attribute-defined-outside-init
        # create a treeview with three columns
        self.treeview = ttk.Treeview(self.frame, columns=("name", "directory"), height=10)
        self.treeview.heading("#0", text="")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("directory", text="Directory")
        self.treeview.column("#0", width=10, stretch=False)
        self.treeview.column("name", width=125, stretch=False)
        self.treeview.column("directory", width=400)
        self.treeview.pack(side="left", expand=True, fill="both", padx=self.pad_x, pady=(self.pad_y, self.pad_y))

    def __create_right_panel(self):
        # pylint: disable=attribute-defined-outside-init
        # create a frame for the right panel
        self.right_panel = tk.Frame(self.frame, bd=0, relief="solid")
        self.right_panel.pack(padx=(0, self.pad_x), pady=(self.pad_y, self.pad_y), fill="both", expand=True)

        # treeview button frame
        self.tree_btn_frame = tk.Frame(self.right_panel)
        self.tree_btn_frame.pack(fill="both", expand=True)

        self.__create_new_or_add_frame()
        self.__create_bottom_frame()

    def __create_new_or_add_frame(self):
        # pylint: disable=attribute-defined-outside-init
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
        self.add_button.config(image=self.img.addition_sign, compound="left", padx=10)
        self.add_button.config(width=(self.right_panel_width / 2) - 5, height=25)
        self.add_button.pack(padx=(0, 0), pady=(0, self.pad_y), side="right")

        # create a button above the picture frame
        self.new_button = tk.Button(self.new_or_add_frame, text="New", height=25, command=self.prompt_new_hud)
        self.new_button.config(image=self.img.star_black_fivepointed_shape_symbol, compound="left", padx=10)
        self.new_button.config(width=(self.right_panel_width / 2), height=25)
        self.new_button.pack(padx=(0, 5), pady=(0, self.pad_y), side="left")

    def __create_bottom_frame(self):
        # pylint: disable=attribute-defined-outside-init
        # create a frame for the edit controls
        self.bottom_frame = tk.Frame(self.tree_btn_frame)
        self.bottom_frame.pack(side="bottom", fill="both", anchor="se", expand=False)
        self.__create_rem_op_ex_frame()
        self.__create_picture_frame()
        self.__create_dev_and_edit_frame()

    def __create_rem_op_ex_frame(self):
        # pylint: disable=attribute-defined-outside-init
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
        self.rem_op_ex_label.pack(fill="both", pady=self.pad_y)

        # remove, open & export buttons frame
        self.rem_op_ex_frame = tk.Frame(self.bottom_frame, bd=0, relief="solid")
        self.rem_op_ex_frame.pack()

        # export vpk
        self.export_vpk_button = tk.Button(
            self.rem_op_ex_frame,
            text="Export",
            justify="center",
            command=self.selected_hud_export_vpk_or_folder,
            state="disabled",  # Disable the remove button
        )
        self.export_vpk_button.config(
            image=self.img.save_black_diskette_interface_symbol, compound="left", padx=self.pad_x
        )
        self.export_vpk_button.config(width=55, height=25)
        self.export_vpk_button.pack(padx=0, pady=0, side="left")

        # open dir
        self.open_dir_button = tk.Button(
            self.rem_op_ex_frame,
            text="Open",
            justify="center",
            command=self.selected_hud_open_dir,
            state="disabled",  # Disable the remove button
        )
        self.open_dir_button.config(image=self.img.folder_black_interface_symbol, compound="left", padx=self.pad_x)
        self.open_dir_button.config(width=55, height=25)  # Adjust the width as needed
        self.open_dir_button.pack(padx=(5, 5), pady=0, side="left")

        # Remove
        self.remove_button = tk.Button(
            self.rem_op_ex_frame,
            text="Remove",
            justify="center",
            command=self.selected_hud_remove_or_delete,
            state="disabled",  # Disable the remove button
        )
        self.remove_button.config(image=self.img.trash_can_black_symbol, compound="left", padx=self.pad_x)
        self.remove_button.config(width=55, height=25)
        self.remove_button.pack(padx=0, pady=0, side="left")

    def __create_picture_frame(self):
        # pylint: disable=attribute-defined-outside-init
        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.bottom_frame, bd=0, relief="solid")  # bg="black"
        self.picture_frame.pack(fill=tk.X, padx=0, pady=(self.pad_y, self.pad_y))

        # Add the image viewport, display it in the picture frame and set the initial image
        self.picture_canvas = tk.Canvas(self.picture_frame, relief="groove", bd=3)
        # width + 16 because otherwise black bars around the canvas. possibly caused by the relief/border options
        self.picture_canvas.config(width=self.right_panel_width + 45, height=self.right_panel_width + 45)
        self.picture_canvas.pack()

    def __create_dev_and_edit_frame(self):
        # pylint: disable=attribute-defined-outside-init

        # remove, open & export buttons frame
        self.dev_and_edit_frame = tk.Frame(self.bottom_frame, bd=0, relief="solid")
        self.dev_and_edit_frame.pack(fill=tk.X, expand=True)

        # Developer menu
        developer_menu_button = tk.Button(self.dev_and_edit_frame, text="Developer", justify="center")
        developer_menu_button.config(width=85, height=25)
        developer_menu_button.config(image=self.img.wrench_black_silhouette, compound="left", padx=self.pad_x)
        developer_menu_button.pack(padx=(0, 5), pady=0, side="left")
        developer_menu_button.bind("<ButtonRelease-1>", self.show_developer_menu)

        # create a button above the picture frame
        self.edit_button = tk.Button(
            self.dev_and_edit_frame,
            text="Edit",
            height=25,
            command=self.edit_selected_hud,
            state="disabled",  # Disable the remove button
        )
        self.edit_button.config(image=self.img.paintbrush_design_tool_interface_symbol, compound="left", padx=10)
        self.edit_button.pack(fill=tk.X, padx=0, pady=0)

    def __create_context_menu(self):
        # Create a context menu for the treeview
        self.context_menu = tk.Menu(self.treeview, tearoff=0)
        self.context_menu.add_command(
            label="Edit",
            command=self.selected_hud_start_editing,
            image=self.img.paintbrush_design_tool_interface_symbol,
            compound="left",
        )
        self.context_menu.add_separator()
        self.context_menu.add_command(
            label="Open directory",
            command=self.selected_hud_open_dir,
            image=self.img.folder_black_interface_symbol,
            compound="left",
        )
        self.context_menu.add_command(
            label="Export as VPK",
            command=self.selected_hud_export_vpk,
            image=self.img.save_black_diskette_interface_symbol,
            compound="left",
        )
        self.context_menu.add_command(
            label="Export as Folder",
            command=self.selected_hud_export_directory,
            image=self.img.save_black_diskette_interface_symbol,
            compound="left",
        )
        self.context_menu.add_separator()
        self.context_menu.add_command(
            label="Remove",
            command=self.selected_hud_remove_or_delete,
            image=self.img.trash_can_black_symbol,
            compound="left",
        )

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        self.data_manager.set("HudSelectGuiGeometry", self.get_window_geometry())

    def enable_buttons(self):
        """Enable the following buttons: edit, export, open, remove"""

        # Enable the export button
        self.export_vpk_button.config(state="normal")
        # Enable the open button
        self.open_dir_button.config(state="normal")
        # Enable the remove button
        self.remove_button.config(state="normal")
        # Enable the edit button
        self.edit_button.config(state="normal")

    def show_developer_menu(self, event):
        """Open the developer context menu"""
        self.dev_context_menu.post(event.x_root, event.y_root)

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

    def selected_hud_export_vpk_or_folder(self):
        """Export the selected hud as a vpk file or directory"""
        options = ["VPK", "Folder"]
        result = show_custom_prompt(options)
        if not result:
            print("User did not select an export method!")
            return
        if result == "VPK":
            self.selected_hud_export_vpk()
        if result == "Folder":
            self.selected_hud_export_directory()

    def selected_hud_export_directory(self):
        """Export hud as folder"""
        print("selected_hud_export_directory")

        if not self.selected_hud_dir:
            print("No HUD selected!")
            return

        target_dir = filedialog.askdirectory(title="Select a target folder to copy contents into")
        if target_dir:
            copy_directory(self.selected_hud_dir, target_dir)

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
        # pylint: disable=attribute-defined-outside-init
        print("Remove tree item")

        # set variables
        hud_name = self.selected_hud_name
        hud_dir_json_format = self.selected_hud_dir.replace("\\", "/")  # convert path to json

        # prompt remove
        result = show_message(f"Remove {hud_name} from the list?", "yesno")
        if not result:
            return

        # remove from data
        self.data_manager.remove_item_from_list("stored_huds", hud_dir_json_format)
        self.selected_hud_dir = ""
        self.selected_hud_name = ""
        self.update_treeview()

        # prompt move to trash
        result = show_message(f"Also move {hud_name} directory into the trash?", "yesno")
        if result:
            send2trash.send2trash(self.selected_hud_dir)

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
        # pylint: disable=attribute-defined-outside-init
        image = Image.open(path)
        self.picture_canvas_photo = ImageTk.PhotoImage(image)

        # Calculate the center coordinates based on the canvas size
        center_x = self.picture_canvas.winfo_reqwidth() // 2
        center_y = self.picture_canvas.winfo_reqheight() // 2

        # Configure the canvas to display the image
        self.picture_canvas.create_image(center_x, center_y, anchor="center", image=self.picture_canvas_photo)

    # pylint: disable=unused-argument
    def tree_set_selected_item(self, event):
        """Get select item from treeview"""
        # pylint: disable=attribute-defined-outside-init
        selected_item = self.treeview.selection()
        for item in selected_item:
            item_values = self.treeview.item(item)["values"]
            self.selected_hud_name = self.treeview.item(item)["values"][0]
            self.selected_hud_dir = os.path.normpath(self.treeview.item(item)["values"][1])
            image = os.path.join(self.selected_hud_dir, "addonimage.jpg")

            self.change_addon_image(image)
            self.enable_buttons()

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

        # edit hud
        self.hud.edit.start_editing(self.selected_hud_dir)
