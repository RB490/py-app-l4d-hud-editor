"""Module for the hud file descriptions gui"""
import tkinter as tk
from tkinter import simpledialog

from shared_gui.base import BaseGUI
from shared_utils.functions import Singleton, show_message

from src.game.game import Game
from src.hud.hud import Hud
from src.utils.constants import APP_ICON, DATA_MANAGER
from src.utils.functions import show_browser_gui


class GuiHudDescriptions(BaseGUI, metaclass=Singleton):
    """Class for the hud file descriptions gui"""

    def __init__(self, parent_root):
        # variables
        self.settings_geometry_key = "GuiGeometryDescriptions"
        self.parent = parent_root
        self.file_name = None
        self.relative_path = None
        self.unsaved_changes = False
        self.prev_file_desc_content = None
        self.prev_ctrl_desc_content = None
        self.data_manager = DATA_MANAGER
        self.game = Game()
        self.hud = Hud()

        # gui
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.set_title("File")
        self.set_icon(APP_ICON)
        self.set_always_on_top(True)
        # self.root.minsize(450, 400)
        self.set_window_geometry(self.data_manager.get(self.settings_geometry_key))
        self.__create_widgets()

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        self.data_manager.set(self.settings_geometry_key, self.get_window_geometry())

    def __create_widgets(self):
        """Create widgets"""
        # define constants for padding and sizing
        self.pad_x = 10
        self.pad_y = 10
        self.ctrl_w = 40

        self.__create_file_widgets()
        self.__create_control_widgets()

    def __create_file_widgets(self):
        """Create widgets"""
        # pylint: disable=attribute-defined-outside-init
        file_desc_frame = tk.Frame(self.root)
        file_desc_frame.pack(fill="both", expand=True, padx=self.pad_x, pady=(0, 0))

        file_desc_label = tk.Label(file_desc_frame, text="File description")
        file_desc_label.pack(side="top", anchor="w", padx=self.pad_x, pady=self.pad_y)

        file_desc_scrollbar = tk.Scrollbar(file_desc_frame)
        file_desc_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_desc_text = tk.Text(
            file_desc_frame, height=6, width=self.ctrl_w, yscrollcommand=file_desc_scrollbar.set
        )
        self.file_desc_text.pack(side="top", fill="both", expand=True, padx=self.pad_x, pady=0)
        self.file_desc_text.bind("<KeyPress>", self.on_file_desc_modified)

        file_desc_scrollbar.config(command=self.file_desc_text.yview)

    def __create_control_widgets(self):
        """Create widgets"""
        # pylint: disable=attribute-defined-outside-init
        ctrl_label_frame = tk.LabelFrame(self.root, text="Control descriptions")
        ctrl_label_frame.pack(fill="both", expand=True, padx=self.pad_x * 2, pady=self.pad_y * 2)

        ctrl_button_frame = tk.Frame(ctrl_label_frame)
        ctrl_button_frame.pack(side="bottom", fill="x", expand=False, padx=self.pad_x, pady=(0, self.pad_y))

        self.ctrl_menu_variable = tk.StringVar(self.root)
        self.ctrl_menu_variable.set("None")  # default value
        controls_list = ["None"]
        self.ctrl_menu = tk.OptionMenu(
            ctrl_button_frame, self.ctrl_menu_variable, *controls_list, command=self.selected_ctrl
        )
        self.ctrl_menu.config(width=25)
        self.ctrl_menu.pack(side="left", padx=self.pad_x, pady=self.pad_y, fill="x", expand=True)

        add_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.add_control)
        add_ctrl_button.config(width=25, height=23)
        add_ctrl_button.config(image=self.img.get("plus", 2), compound="center")
        add_ctrl_button.pack(side="left", padx=self.pad_x, pady=self.pad_y)

        remove_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.remove_control)
        remove_ctrl_button.config(width=25, height=23)
        remove_ctrl_button.config(image=self.img.get("delete", 2), compound="center")
        remove_ctrl_button.pack(side="left", padx=self.pad_x, pady=self.pad_y)

        ctrl_desc_frame = tk.Frame(ctrl_label_frame)
        ctrl_desc_frame.pack(anchor="nw", side="top", fill="both", expand=True, padx=self.pad_x, pady=(self.pad_y, 0))

        ctrl_desc_scrollbar = tk.Scrollbar(ctrl_desc_frame)
        ctrl_desc_scrollbar.pack(side="right", fill="y")

        self.ctrl_desc_text = tk.Text(
            ctrl_desc_frame, height=4, width=self.ctrl_w, yscrollcommand=ctrl_desc_scrollbar.set
        )
        self.ctrl_desc_text.pack(side="bottom", fill="both", expand=True, padx=self.pad_x, pady=(self.pad_y, 0))
        self.ctrl_desc_text.bind("<KeyPress>", self.on_ctrl_desc_modified)

        ctrl_desc_scrollbar.config(command=self.ctrl_desc_text.yview)

        save_button_frame = tk.Frame(self.root)
        save_button_frame.pack(side="bottom", expand=False, fill="x", padx=self.pad_x, pady=(0, self.pad_y))

        save_button = tk.Button(
            save_button_frame,
            text="Save",
            justify="center",
            height=25,
            width=self.ctrl_w,
            command=self.submit_gui_save_changes,
        )
        save_button.config(image=self.img.get("save", 2), compound="left", padx=self.pad_x)
        save_button.pack(side="right", expand=True, fill="x", padx=self.pad_x, pady=(0, self.pad_y))

        remove_file_entry_button = tk.Button(
            save_button_frame, text="Remove", justify="center", command=self.remove_file_entry
        )
        remove_file_entry_button.config(width=70, height=25)
        remove_file_entry_button.config(image=self.img.get("delete", 2), compound="left", padx=self.pad_x)
        remove_file_entry_button.pack(side="left", padx=self.pad_x, pady=(0, self.pad_y))

    def on_close(self):
        """On gui close"""

        # prompt to save unsaved changes
        self.prompt_to_save_unsaved_changes()

        # undo unsaved changes by reloading from disk
        self.hud.desc.read_from_disk()

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

    def load_file(self, file_name, relative_path):
        """Load description for hud file into the gui"""

        # prompt to save unsaved changes
        self.prompt_to_save_unsaved_changes()

        # save relative path
        self.file_name = file_name
        self.relative_path = relative_path

        # Check if the file has a custom status using the self.game.dir.is_custom_file function
        is_custom = self.hud.desc.get_custom_file_status(relative_path)

        # Set gui title with custom status if applicable
        if is_custom:
            custom_status = "Custom File"
        elif is_custom is None:
            custom_status = "New File"
        else:
            custom_status = "Vanilla File"
        self.root.title(f"{relative_path} ({custom_status})")

        # set file description
        self.file_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.file_desc_text.insert(tk.END, self.hud.desc.get_file_description(file_name))

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
        controls_list = self.hud.desc.get_controls(self.file_name)

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
        self.ctrl_desc_text.insert(tk.END, self.hud.desc.get_control_description(self.file_name, input_ctrl))

    def save_control_description(self):
        """Save control description"""
        selected_control = self.ctrl_menu_variable.get()
        control_desc = self.ctrl_desc_text.get("1.0", "end-1c")
        self.hud.desc.set_control_description(self.file_name, selected_control, control_desc)

    def save_file_description(self):
        """Save file description"""
        file_description = self.file_desc_text.get("1.0", "end-1c")
        self.hud.desc.set_file_description(self.file_name, file_description)

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
            self.hud.desc.add_control(self.file_name, new_control)
            self.load_controls()
            self.load_control(new_control)
            print(f"Added {new_control}")

    def remove_file_entry(self):
        """Remove control"""
        if show_message(f"Are you sure you want to remove '{self.file_name}'?", "yesno"):
            self.hud.desc.remove_entry(self.file_name)
            self.load_controls()

    def remove_control(self):
        """Remove control"""
        selected_control = self.ctrl_menu_variable.get()
        if show_message("Remove Control", f"Are you sure you want to remove '{selected_control}'?", "yesno"):
            self.hud.desc.remove_control(self.file_name, selected_control)
            self.load_controls()

    def save_changes(self):
        "Save changes"
        # save file description
        self.save_file_description()

        # save currently loaded control
        self.save_control_description()

        # save relative path
        self.hud.desc.set_file_relative_path(self.file_name, self.relative_path)

        # Reset unsaved_changes flag
        self.set_unsaved_changes(False)

        print(f"Saved descriptions for '{self.file_name}'")

    def submit_gui_save_changes(self):
        """Submit gui"""

        # save changes
        self.save_changes()

        show_browser_gui()

        self.on_close()

    def prompt_to_save_unsaved_changes(self):
        "Ask user whether to save unsaved changes"
        if self.unsaved_changes:
            response = show_message(
                f"Do you want to save the unsaved changes made to '{self.file_name}'?", "yesno", "Unsaved Changes"
            )

            if response:
                self.save_changes()
            else:
                self.set_unsaved_changes(False)


def main():
    root = tk.Tk()
    root.withdraw()
    descriptions_gui = GuiHudDescriptions(root)
    descriptions_gui.load_file("hudlayout.res", "scripts\\hudlayout.res")
    # descriptions_gui.show()
    # descriptions_gui.hud.desc.remove_entry("custom_hudlayout.res")

    # descriptions_gui.load_file("custom_hudlayout.res")

    input("Press enter to exit script...")


if __name__ == "__main__":
    main()
