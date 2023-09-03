"""GUI Class for modifying VDF files."""
# pylint: disable=broad-exception-caught
import tkinter as tk
from tkinter import scrolledtext

from gui.base import BaseGUI
from shared_utils.shared_utils import show_message
from utils.constants import APP_ICON, ImageConstants
from utils.persistent_data_manager import PersistentDataManager
from utils.vdf import VDFModifier


class VDFModifierGUI(BaseGUI):
    """GUI Class for modifying VDF files."""

    def __init__(self, parent_root, vdf_path):
        # variables
        self.settings_geometry_key = "GuiGeometryVDF"
        self.vdf_path = vdf_path
        self.root = None  # load_file() uses this to check if the gui was loaded
        self.load_file()  # confirm whether the file is valid

        # setup gui
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.data_manager = PersistentDataManager()
        self.img = ImageConstants()
        self.modifier = None  # vdf modifier class
        self.root.minsize(875, 425)
        self.root.iconbitmap(APP_ICON)
        self.root.title("VDF Modifier")
        self.control_options = ["xpos", "ypos", "wide", "tall", "visible", "enabled"]
        self.selected_control = tk.StringVar(value=self.control_options[0])
        self.previous_output = None
        self.annotate_var = tk.IntVar(value=self.data_manager.get("VDFGui_annotate"))
        self.sort_control_keys_var = tk.IntVar(value=self.data_manager.get("VDFGui_sort_keys"))
        self.align_values_indent_var = tk.IntVar(value=self.data_manager.get("VDFGui_indent_values"))
        self.modify_int_var = tk.IntVar(value=self.data_manager.get("VDFGui_modify_int"))
        self.modify_amount_var = tk.IntVar()
        self.modify_modifier_var = tk.StringVar(value="plus")
        self.set_window_geometry(self.data_manager.get(self.settings_geometry_key))
        self.__create_widgets()

        # load file
        self.load_file()

    def load_file(self):
        "Load VDF file"
        self.previous_output = None
        try:
            self.modifier = VDFModifier(self.vdf_path)
        except Exception as err_info:
            show_message(f"Unable to load VDF file! {err_info}", "error")
            self.destroy()
            return False
        self.process()
        return True

    def __create_widgets(self):
        """Create widgets"""
        # Create a main frame to hold everything
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        info_msg = "Expect incorrect results on larger and/or more complex VDF files like sourcescheme.res! "
        info_msg += "(comments are not saved!)"

        self.info_label = tk.Label(self.main_frame, text=info_msg)
        self.info_label.pack(side=tk.BOTTOM, pady=(0, 5))

        self.__create_right_side_frame()

    def __create_right_side_frame(self):
        # pylint: disable=attribute-defined-outside-init
        self.right_side_frame = tk.Frame(self.main_frame, relief=tk.SOLID, borderwidth=0)
        self.right_side_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.reload_button = tk.Button(self.right_side_frame, text="Reload", height=16, command=self.load_file)
        self.reload_button.pack(fill=tk.X, padx=(1, 10), pady=(0, 10))
        self.reload_button.config(
            image=self.img.arrows_couple_counterclockwise_rotating_symbol, compound="left", padx=10
        )

        self.save_to_file_button = tk.Button(self.right_side_frame, text="Save", height=16, command=self.save_vdf)
        self.save_to_file_button.pack(side=tk.BOTTOM, fill=tk.X, padx=(1, 10), pady=(0, 10))
        self.save_to_file_button.config(image=self.img.save_black_diskette_interface_symbol, compound="left", padx=10)

        self.process_button = tk.Button(self.right_side_frame, text="Modify", height=32, command=self.process)
        self.process_button.pack(side=tk.BOTTOM, fill=tk.X, padx=(1, 10), pady=(0, 10))
        self.process_button.config(image=self.img.pencil_black_square, compound="left", padx=10)

        self.__create_modify_integers_frame()
        self.__create_other_options_frame()
        self.__create_previous_vdf_frame()
        self.__create_current_vdf_frame()

    def __create_modify_integers_frame(self):
        # pylint: disable=attribute-defined-outside-init
        # Create a frame for integer modifying widgets
        int_mod_frame = tk.Frame(self.right_side_frame, relief=tk.RIDGE, borderwidth=3)
        int_mod_frame.pack(fill=tk.X, padx=(0, 10), pady=(0, 10))

        self.modify_int_checkbox = tk.Checkbutton(int_mod_frame, text="Modify Integers", variable=self.modify_int_var)
        self.modify_int_checkbox.pack(anchor="w", padx=(10, 10), pady=(10, 0))

        self.control_label = tk.Label(int_mod_frame, text="Select Control:")
        self.control_label.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        self.control_dropdown = tk.OptionMenu(int_mod_frame, self.selected_control, *self.control_options)
        self.control_dropdown.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        # Spinbox for Modify Amount
        self.modify_amount_label = tk.Label(int_mod_frame, text="Modify Amount:")
        self.modify_amount_label.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        # Validate function to allow only integers
        def validate_int_input(action, value_if_allowed):
            if action == "1":  # Inserting text
                try:
                    int(value_if_allowed)
                    return True
                except ValueError:
                    return False
            return True

        self.validate_int_input = self.root.register(validate_int_input)

        self.modify_amount_spinbox = tk.Spinbox(
            int_mod_frame,
            textvariable=self.modify_amount_var,
            from_=0,
            to=100,
            validate="key",
            validatecommand=(self.validate_int_input, "%d", "%P"),
        )
        self.modify_amount_spinbox.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        self.modify_modifier_label = tk.Label(int_mod_frame, text="Modifier:")
        self.modify_modifier_label.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        self.modify_modifier_plus_radio = tk.Radiobutton(
            int_mod_frame, text="Plus", variable=self.modify_modifier_var, value="plus"
        )
        self.modify_modifier_plus_radio.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        self.modify_modifier_minus_radio = tk.Radiobutton(
            int_mod_frame, text="Minus", variable=self.modify_modifier_var, value="minus"
        )
        self.modify_modifier_minus_radio.pack(anchor="w", padx=(10, 10), pady=(0, 10))

    def __create_other_options_frame(self):
        # pylint: disable=attribute-defined-outside-init
        # Other Options Frame
        other_options_frame = tk.Frame(self.right_side_frame, width=550, relief=tk.RIDGE, borderwidth=3)
        other_options_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=(0, 10), pady=(0, 10))

        self.annotate_checkbox = tk.Checkbutton(other_options_frame, text="Annotate", variable=self.annotate_var)
        self.annotate_checkbox.pack(anchor="w", padx=(10, 10), pady=(10, 0))

        self.sort_control_keys_checkbox = tk.Checkbutton(
            other_options_frame, text="Sort Keys", variable=self.sort_control_keys_var
        )
        self.sort_control_keys_checkbox.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        self.align_values_indent_checkbox = tk.Checkbutton(
            other_options_frame, text="Align Indentation", variable=self.align_values_indent_var
        )
        self.align_values_indent_checkbox.pack(anchor="w", padx=(10, 10), pady=(0, 10))

    def __create_previous_vdf_frame(self):
        # pylint: disable=attribute-defined-outside-init
        # Create frames for text widgets
        previous_frame = tk.Frame(self.main_frame)
        previous_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(10, 10))

        # Label for "previous" text box
        previous_label = tk.Label(previous_frame, text="Previous:")
        previous_label.pack(side=tk.TOP, pady=(0, 5))

        # "previous" text box
        self.previous_text = scrolledtext.ScrolledText(previous_frame, width=40, height=10)
        self.previous_text.pack(fill=tk.BOTH, expand=True)

    def __create_current_vdf_frame(self):
        # pylint: disable=attribute-defined-outside-init
        current_frame = tk.Frame(self.main_frame)
        current_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(0, 10), pady=(10, 10))

        # Label for "current" text box
        current_label = tk.Label(current_frame, text="Current:")
        current_label.pack(side=tk.TOP, pady=(0, 5))

        # "current" text box
        self.current_text = scrolledtext.ScrolledText(current_frame, width=40, height=10)
        self.current_text.pack(fill=tk.BOTH, expand=True)

    def process(self):
        """Process changes"""
        # if gui not loaded yet
        if not self.root:
            return

        self.previous_text.configure(state="normal")
        self.current_text.configure(state="normal")

        is_align_values_indentation = self.align_values_indent_var.get()

        self.previous_text.delete(1.0, tk.END)
        if self.previous_output:
            self.previous_text.insert(tk.END, self.previous_output)
        else:
            self.previous_text.insert(tk.END, self.modifier.get_source_raw_text())

        if self.annotate_var.get():
            self.modifier.annotate(self.modifier.get_obj())
        else:
            self.modifier.remove_annotations(self.modifier.get_obj())

        if self.sort_control_keys_var.get():
            self.modifier.sort_control_keys(self.modifier.get_obj())

        if self.modify_int_var.get():
            control_to_modify = self.selected_control.get()
            amount = self.modify_amount_var.get()
            self.modifier.modify_integers(self.modify_modifier_var.get(), amount, control_to_modify)

        output = self.modifier.get_pretty_printed_vdf(is_align_values_indentation)

        self.current_text.delete(1.0, tk.END)
        self.current_text.insert(tk.END, output)

        self.previous_output = output

        self.save_window_settings()

        self.previous_text.configure(state="disabled")
        self.current_text.configure(state="disabled")

    def save_vdf(self):
        "Save vdf to disk"

        self.save_window_settings()

        self.modifier.save_vdf(
            self.modifier.get_obj(), self.modifier.get_path(), self.data_manager.get("VDFGui_indent_values")
        )

    def save_window_settings(self):
        "Save gui settings"
        self.data_manager.set("VDFGui_indent_values", self.align_values_indent_var.get())
        self.data_manager.set("VDFGui_modify_int", self.modify_int_var.get())
        self.data_manager.set("VDFGui_annotate", self.annotate_var.get())
        self.data_manager.set("VDFGui_sort_keys", self.sort_control_keys_var.get())

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""

        self.data_manager.set(self.settings_geometry_key, self.get_window_geometry())
