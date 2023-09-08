"""Module for the hud select gui class"""
# pylint: disable=broad-exception-caught, import-outside-toplevel, arguments-differ, broad-exception-raised
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

import send2trash
from loguru import logger
from PIL import Image, ImageTk
from shared_gui.base import BaseGUI

from game.game import Game
from gui.browser import GuiHudBrowser
from hud.hud import Hud
from shared_utils.shared_utils import Singleton, copy_directory, show_message
from utils.constants import (APP_ICON, GUI_BROWSER_TITLE, IMAGES_DIR_128,
                             PROGRAM_NAME, VERSION_NO_PRETTY, ImageConstants)
from utils.functions import save_and_exit_script
from utils.persistent_data_manager import PersistentDataManager
from utils.vpk import VPKClass


class GuiHudStart(BaseGUI, metaclass=Singleton):
    """Class for the hud select gui"""

    def __init__(self):
        # variables
        self.settings_geometry_key = "GuiGeometryStart"
        self.data_manager = PersistentDataManager()
        self.game = Game()
        self.hud = Hud()
        self.selected_hud_name = ""
        self.selected_hud_dir = ""

        # gui
        super().__init__("main")
        self.browser = GuiHudBrowser(self.root, self)
        self.img = ImageConstants()
        self.root.title("Start")
        self.root.iconbitmap(APP_ICON)
        self.root.minsize(865, 500)
        self.set_window_geometry(self.data_manager.get(self.settings_geometry_key))
        self.__create_widgets()
        self.__create_context_menu()
        self.change_addon_image(os.path.join(IMAGES_DIR_128, "cross.png"))

        # Bind the right-click event to show the context menu
        self.treeview.bind("<Button-3>", self.show_tree_context_menu)

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_set_selected_item)

        from menu.menu import EditorMenuClass

        self.editor_menu = EditorMenuClass(self, self.root)

        self.gui_refresh()

    def debug_show_browser_gui(self):
        """Used for debugging to automatically open the browser gui after starting mainloop"""
        self.browser.show()
        self.browser.set_title(f"{self.hud.edit.get_name()} {GUI_BROWSER_TITLE}")

    def __create_widgets(self):
        # gui variables
        self.pad_x = 10
        self.pad_y = 10
        self.right_panel_width = 204

        # initialize variables
        self.picture_canvas_photo = None

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
        developer_menu_button = tk.Button(
            self.dev_and_edit_frame,
            text="Developer",
            justify="center",
            width=85,
            height=25,
            image=self.img.wrench_black_silhouette,
            compound="left",
            padx=self.pad_x,
            command=lambda: self.show_menu_on_button(developer_menu_button, self.editor_menu.get_context_menu_dev()),
        )
        developer_menu_button.pack(padx=(0, 5), pady=0, side="left")

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

        self.context_menu.add_separator()
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
        self.data_manager.set(self.settings_geometry_key, self.get_window_geometry())

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
        hud_dir = self.selected_hud_dir

        # Check if the source directory exists
        if os.path.exists(hud_dir):
            # Open the source directory in the file explorer
            subprocess.Popen(["explorer", hud_dir])
        else:
            logger.debug(f"Directory '{hud_dir}' does not exist.")

    def selected_hud_export_vpk_or_folder(self):
        """Export the selected hud as a vpk file or directory"""

        # Create the menu
        vpk_export_menu = tk.Menu(self.root, tearoff=0)

        # vpk_export_menu.add_command(label="Export", state=tk.DISABLED, command=lambda: None)
        # vpk_export_menu.add_separator()

        vpk_export_menu.add_command(
            label="VPK",
            image=self.img.file_black_rounded_symbol_1,
            compound=tk.LEFT,
            command=self.selected_hud_export_vpk,
        )

        vpk_export_menu.add_command(
            label="Folder",
            image=self.img.folder_black_interface_symbol,
            compound=tk.LEFT,
            command=self.selected_hud_export_directory,
        )

        self.show_menu_on_button(self.export_vpk_button, vpk_export_menu)

    def selected_hud_export_directory(self):
        """Export hud as folder"""

        if not self.selected_hud_dir:
            logger.debug("No HUD selected!")
            return

        target_dir = filedialog.askdirectory(title="Export HUD as folder")
        if target_dir:
            copy_directory(self.selected_hud_dir, target_dir)

    def selected_hud_export_vpk(self):
        """Export the selected hud as a vpk file."""

        export_path = filedialog.asksaveasfilename(
            initialdir="/", title="Export HUD as VPK", filetypes=(("package files", "*.vpk"), ("all files", "*.*"))
        )

        if export_path:
            logger.debug(export_path)
            vpk_class = VPKClass()
            vpk_class.create(self.selected_hud_dir, os.path.dirname(export_path), os.path.basename(export_path))
            # vpk_class.create(self, input_dir, output_dir, output_file_name):

    def selected_hud_remove_or_delete(self):
        """Remove the selected hud."""
        # pylint: disable=attribute-defined-outside-init

        # set variables
        hud_name = self.selected_hud_name
        hud_dir_json_format = self.selected_hud_dir.replace("\\", "/")  # convert path to json

        # prompt remove
        result = show_message(f"Remove {hud_name} from the list?", "yesno")
        if not result:
            return

        # remove from data
        self.data_manager.remove_item_from_list("stored_huds", hud_dir_json_format)
        self.clear_selection()
        self.treeview_refresh()

        # prompt move to trash
        result = show_message(f"Also move {hud_name} directory into the trash?", "yesno")
        if result:
            send2trash.send2trash(self.selected_hud_dir)

    def update_buttons(self):
        """Enable the following buttons: edit, export, open, remove"""

        # Toggle buttons
        if self.selected_hud_dir:
            self.export_vpk_button.config(state="normal")
            self.open_dir_button.config(state="normal")
            self.remove_button.config(state="normal")
            self.edit_button.config(state="normal")
        else:
            self.export_vpk_button.config(state="disabled")
            self.open_dir_button.config(state="disabled")
            self.remove_button.config(state="disabled")
            self.edit_button.config(state="disabled")

        # Rename edit button
        if self.selected_hud_dir_is_being_edited():
            self.edit_button.config(text="Stop Editing")
        else:
            self.edit_button.config(text="Edit")

    def clear_selection(self):
        """Clear selected variables. Called by hud editing class so the gui can properly disable buttons"""
        self.selected_hud_dir = ""
        self.selected_hud_name = ""

    def gui_refresh(self, called_by_browser=False):
        "Update treeview, browser treeview, buttons"

        # set title
        name_of_hud_thats_being_edited = self.hud.edit.get_name()
        gui_title = f"{PROGRAM_NAME} {VERSION_NO_PRETTY}"
        if name_of_hud_thats_being_edited:
            if self.hud.edit.is_synced_and_being_edited():
                gui_title = f"{gui_title} - Editing: {name_of_hud_thats_being_edited}"
            else:
                gui_title = f"{gui_title} - Opened: {name_of_hud_thats_being_edited}"
        self.root.title(gui_title)

        # update buttons
        self.update_buttons()

        # refresh treeview
        self.treeview_refresh()

        # refresh browser gui
        if not called_by_browser and self.browser.has_been_run() and self.browser.is_visible():
            self.browser.gui_refresh()

        logger.debug("Refreshed Start GUI!")

    def treeview_refresh(self):
        """Clear treeview & load up-to-date content + update browser menu"""

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
            self.selected_hud_name = item_values[0]
            self.selected_hud_dir = os.path.normpath(item_values[1])
            image = os.path.join(self.selected_hud_dir, "addonimage.jpg")

            self.change_addon_image(image)
            self.update_buttons()

    def prompt_add_hud(self):
        """Prompt user for hud folder to add"""
        if self.hud.manager.prompt_add_existing_hud():
            self.treeview_refresh()

    def prompt_new_hud(self):
        """Prompt user for hud folder to create a new hud in"""
        if self.hud.manager.prompt_create_new_hud():
            self.treeview_refresh()

    def edit_selected_hud(self):
        """Start hud editing for selected hud"""

        if self.selected_hud_dir_is_being_edited():
            self.hud.edit.start_editing(self.selected_hud_dir, called_by_start_gui=True)
            self.hide()
        else:
            self.hud.edit.finish_editing()

    def selected_hud_dir_is_being_edited(self):
        """Check if selected hud dir is being edited"""
        selected_dir = self.selected_hud_dir
        edited_dir = self.hud.edit.get_dir()

        if selected_dir and edited_dir:
            return selected_dir.lower() == edited_dir.lower()

        return False

    def on_close(self):
        """On close callback"""

        if self.browser.is_visible():
            self.hide()
        else:
            if self.hud.edit.is_synced_and_being_edited():
                self.hide()
            else:
                save_and_exit_script()
