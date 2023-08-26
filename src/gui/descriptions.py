"""Module for the hud file descriptions gui"""
import os
import tkinter as tk
from tkinter import simpledialog

from game.game import Game
from gui.base import BaseGUI
from hud.hud import Hud
from shared_utils.shared_utils import Singleton, show_message
from utils.constants import APP_ICON, IMAGES_DIR


class GuiHudDescriptions(BaseGUI, metaclass=Singleton):
    """Class for the hud file descriptions gui"""

    def __init__(self):
        super().__init__(is_modal_dialog=True)
        self.root.title("File")
        self.root.iconbitmap(APP_ICON)

        self.game = Game()
        self.hud = Hud()

        self.relative_path = None
        self.unsaved_changes = False
        self.prev_file_desc_content = None
        self.prev_ctrl_desc_content = None

        # self.root.minsize(450, 400)

        # Create image buttons
        self.add_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "plus.png"))
        self.delete_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "delete.png"))
        self.save_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "saveas.png"))

        # define constants for padding and sizing
        pad_x = 10
        pad_y = 10
        ctrl_w = 40

        file_desc_frame = tk.Frame(self.root)
        file_desc_frame.pack(fill="both", expand=True, padx=pad_x, pady=(0, 0))

        file_desc_label = tk.Label(file_desc_frame, text="File description")
        file_desc_label.pack(side="top", anchor="w", padx=pad_x, pady=pad_y)

        file_desc_scrollbar = tk.Scrollbar(file_desc_frame)
        file_desc_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_desc_text = tk.Text(file_desc_frame, height=6, width=ctrl_w, yscrollcommand=file_desc_scrollbar.set)
        self.file_desc_text.pack(side="top", fill="both", expand=True, padx=pad_x, pady=0)
        self.file_desc_text.bind("<KeyPress>", self.on_file_desc_modified)

        file_desc_scrollbar.config(command=self.file_desc_text.yview)

        ctrl_label_frame = tk.LabelFrame(self.root, text="Control descriptions")
        ctrl_label_frame.pack(fill="both", expand=True, padx=pad_x * 2, pady=pad_y * 2)

        ctrl_button_frame = tk.Frame(ctrl_label_frame)
        ctrl_button_frame.pack(side="bottom", fill="x", expand=False, padx=pad_x, pady=(0, pad_y))

        self.ctrl_menu_variable = tk.StringVar(self.root)
        self.ctrl_menu_variable.set("None")  # default value
        controls_list = ["None"]
        self.ctrl_menu = tk.OptionMenu(
            ctrl_button_frame, self.ctrl_menu_variable, *controls_list, command=self.selected_ctrl
        )
        self.ctrl_menu.config(width=25)
        self.ctrl_menu.pack(side="left", padx=pad_x, pady=pad_y, fill="x", expand=True)

        add_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.add_control)
        add_ctrl_button.config(width=25, height=23)
        add_ctrl_button.config(image=self.add_image, compound="center")
        add_ctrl_button.pack(side="left", padx=pad_x, pady=pad_y)

        remove_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.remove_control)
        remove_ctrl_button.config(width=25, height=23)
        remove_ctrl_button.config(image=self.delete_image, compound="center")
        remove_ctrl_button.pack(side="left", padx=pad_x, pady=pad_y)

        ctrl_desc_frame = tk.Frame(ctrl_label_frame)
        ctrl_desc_frame.pack(anchor="nw", side="top", fill="both", expand=True, padx=pad_x, pady=(pad_y, 0))

        ctrl_desc_scrollbar = tk.Scrollbar(ctrl_desc_frame)
        ctrl_desc_scrollbar.pack(side="right", fill="y")

        self.ctrl_desc_text = tk.Text(ctrl_desc_frame, height=4, width=ctrl_w, yscrollcommand=ctrl_desc_scrollbar.set)
        self.ctrl_desc_text.pack(side="bottom", fill="both", expand=True, padx=pad_x, pady=(pad_y, 0))
        self.ctrl_desc_text.bind("<KeyPress>", self.on_ctrl_desc_modified)

        ctrl_desc_scrollbar.config(command=self.ctrl_desc_text.yview)

        save_button_frame = tk.Frame(self.root)
        save_button_frame.pack(side="bottom", expand=False, fill="x", padx=pad_x, pady=(0, pad_y))

        save_button = tk.Button(
            save_button_frame,
            text="Save",
            justify="center",
            height=25,
            width=ctrl_w,
            command=self.submit_gui_save_changes,
        )
        save_button.config(image=self.save_image, compound="left", padx=pad_x)
        save_button.pack(side="right", expand=True, fill="x", padx=pad_x, pady=(0, pad_y))

        remove_file_entry_button = tk.Button(
            save_button_frame, text="Remove", justify="center", command=self.remove_file_entry
        )
        remove_file_entry_button.config(width=70, height=25)
        remove_file_entry_button.config(image=self.delete_image, compound="left", padx=pad_x)
        remove_file_entry_button.pack(side="left", padx=pad_x, pady=(0, pad_y))

    def on_close(self):
        """On gui close"""

        # prompt to save unsaved changes
        self.prompt_to_save_unsaved_changes()

        # undo unsaved changes by reloading from disk
        self.hud.edit.desc.read_from_disk()

        # clear the gui
        self.clear_gui()

        # close gui
        self.hide()

    # pylint: disable=unused-argument
    def on_file_desc_modified(self, event):
        "Register unsaved changes if content has actually changed"
        new_content = self.file_desc_text.get("1.0", "end-1c")
        if new_content != self.prev_file_desc_content:
            self.set_unsaved_changes(True)
            self.prev_file_desc_content = new_content

    # pylint: disable=unused-argument
    def on_ctrl_desc_modified(self, event):
        "Register unsaved changes if content has actually changed"
        new_content = self.ctrl_desc_text.get("1.0", "end-1c")
        if new_content != self.prev_ctrl_desc_content:
            self.set_unsaved_changes(True)
            self.prev_ctrl_desc_content = new_content

    def set_unsaved_changes(self, unsaved_changes_bool):
        "Set unsaved changes variables"
        if unsaved_changes_bool:
            self.unsaved_changes = True
            self.file_desc_text.edit_modified(True)
            self.ctrl_desc_text.edit_modified(True)
            print("Set unsaved changes to true!")
        else:
            self.unsaved_changes = False
            self.file_desc_text.edit_modified(False)
            self.ctrl_desc_text.edit_modified(False)
            print("Set unsaved changes to false!")

    def load_file(self, relative_path):
        """Load description for hud file into the gui"""

        # prompt to save unsaved changes
        self.prompt_to_save_unsaved_changes()

        # save relative path
        self.relative_path = relative_path

        # Check if the file has a custom status using the self.game.dir.is_custom_file function
        is_custom = self.hud.edit.desc.get_is_file_custom(relative_path)

        # Set gui title with custom status if applicable
        if is_custom:
            custom_status = "Custom File"
        else:
            custom_status = "Vanilla File"
        self.root.title(f"{relative_path} ({custom_status})")

        # set file description
        self.file_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.file_desc_text.insert(tk.END, self.hud.edit.desc.get_file_description(relative_path))

        # load controls
        self.load_controls()

        # Modifying the controls through code will trigger the unsaved changes
        self.set_unsaved_changes(False)

        # run mainloop
        self.show()

    def clear_gui(self):
        """Clear input from all controls"""
        self.ctrl_menu_variable.set(None)
        self.ctrl_menu["menu"].delete(0, "end")  # Delete all existing options
        self.file_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.ctrl_desc_text.delete("1.0", tk.END)  # delete all existing text

    def load_controls(self):
        """Load controls into option menu & load the first one"""

        # update the controls list and OptionMenu with new values
        controls_list = self.hud.edit.desc.get_controls(self.relative_path)

        # controls available at all?
        if not controls_list:
            return

        menu = self.ctrl_menu["menu"]  # get the OptionMenu menu object
        menu.delete(0, "end")  # delete all existing options from the menu
        for item in controls_list:
            # iterate over the new controls list and add commands to the menu for each item
            menu.add_command(label=item, command=lambda selected_item=item: self.selected_ctrl(selected_item))
        self.load_control(controls_list[0])

    def load_control(self, input_ctrl):
        """Load hud file control into the gui"""

        # set options menu
        self.ctrl_menu_variable.set(input_ctrl)

        # set control description
        self.ctrl_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.ctrl_desc_text.insert(tk.END, self.hud.edit.desc.get_control_description(self.relative_path, input_ctrl))

    def save_control_description(self):
        """Save control description"""
        selected_control = self.ctrl_menu_variable.get()
        control_desc = self.ctrl_desc_text.get("1.0", "end-1c")
        self.hud.edit.desc.set_control_description(self.relative_path, selected_control, control_desc)

    def save_file_description(self):
        """Save file description"""
        file_description = self.file_desc_text.get("1.0", "end-1c")
        self.hud.edit.desc.set_file_description(self.relative_path, file_description)

    def selected_ctrl(self, input_ctrl):
        """Handle control menu selection"""

        # save currently loaded control
        self.save_control_description()

        # load selected control
        print("You selected:", input_ctrl)
        self.load_control(input_ctrl)

    def add_control(self):
        """Add new control"""
        # Show a dialog box to get the name of the new control
        new_control = simpledialog.askstring("New Control", "Enter the name of the new control:")

        # If user entered a name and clicked OK, add the control
        if new_control:
            # save currently loaded control
            self.save_control_description()

            # Add control
            self.hud.edit.desc.add_control(self.relative_path, new_control)
            self.load_controls()
            self.load_control(new_control)
            print(f"Added {new_control}")

    def remove_file_entry(self):
        """Remove control"""
        if show_message(f"Are you sure you want to remove '{self.relative_path}'?", "yesno"):
            self.hud.edit.desc.remove_entry(self.relative_path)
            self.load_controls()

    def remove_control(self):
        """Remove control"""
        selected_control = self.ctrl_menu_variable.get()
        if show_message("Remove Control", f"Are you sure you want to remove '{selected_control}'?", "yesno"):
            self.hud.edit.desc.remove_control(self.relative_path, selected_control)
            self.load_controls()

    def save_changes(self):
        "Save changes"
        # save file description
        self.save_file_description()

        # save currently loaded control
        self.save_control_description()

        # Reset unsaved_changes flag
        self.set_unsaved_changes(False)

        print(f"Saved descriptions for '{self.relative_path}'")

    def submit_gui_save_changes(self):
        """Submit gui"""

        # save changes
        self.save_changes()

        # import browser here to avoid infinite recursion loop because it also imports this (descriptions gui) module
        # pylint: disable=import-outside-toplevel
        from gui.browser import GuiHudBrowser

        # call browser refresh
        browser = GuiHudBrowser()
        browser.treeview_refresh(browser.treeview)

        self.on_close()

    def prompt_to_save_unsaved_changes(self):
        "Ask user whether to save unsaved changes"
        if self.unsaved_changes:
            response = show_message(
                f"Do you want to save the unsaved changes made to '{self.relative_path}'?", "yesno", "Unsaved Changes"
            )

            if response:
                self.save_changes()
            else:
                self.set_unsaved_changes(False)
