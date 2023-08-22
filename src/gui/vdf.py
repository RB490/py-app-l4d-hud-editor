import tkinter as tk
from tkinter import scrolledtext

from utils.constants import APP_ICON
from utils.vdf import VDFModifier


class VDFModifierGUI:
    """GUI Class for modifying VDF files."""

    def __init__(self, persistent_data, vdf_path):
        self.vdf_path = vdf_path
        self.persistent_data = persistent_data
        self.modifier = VDFModifier(self.persistent_data, self.vdf_path)
        self.is_hidden = False
        self.root = tk.Tk()
        self.root.minsize(875, 395)
        self.root.iconbitmap(APP_ICON)
        self.root.title("VDF Modifier")

        self.control_options = ["xpos", "ypos", "wide", "tall", "visible", "enabled"]
        self.selected_control = tk.StringVar(value=self.control_options[0])
        self.previous_output = None

        self.annotate_var = tk.IntVar()
        self.sot_control_keys_var = tk.IntVar()
        self.align_values_indent_var = tk.IntVar()
        self.modify_int_var = tk.IntVar()
        self.modify_amount_var = tk.IntVar()
        self.modify_modifier_var = tk.StringVar(value="plus")

        self.create_widgets()

    def create_widgets(self):
        """Create widgets"""

        # Create a main frame to hold everything
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        right_side_frame = tk.Frame(main_frame, relief=tk.SOLID, borderwidth=0)
        right_side_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.process_button = tk.Button(right_side_frame, text="Process", command=self.process)
        self.process_button.pack(side=tk.BOTTOM, fill=tk.X, padx=(1, 10), pady=(0, 10))

        # Create a frame for integer modifying widgets
        int_mod_frame = tk.Frame(right_side_frame, relief=tk.RIDGE, borderwidth=3)
        int_mod_frame.pack(fill=tk.X, padx=(0, 10), pady=(30, 10))

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

        # Other Options Frame
        other_options_frame = tk.Frame(right_side_frame, width=550, relief=tk.RIDGE, borderwidth=3)
        other_options_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=(0, 10), pady=(0, 10))

        self.annotate_checkbox = tk.Checkbutton(other_options_frame, text="Annotate", variable=self.annotate_var)
        self.annotate_checkbox.pack(anchor="w", padx=(10, 10), pady=(10, 0))

        self.sot_control_keys_checkbox = tk.Checkbutton(
            other_options_frame, text="Sort Keys", variable=self.sot_control_keys_var
        )
        self.sot_control_keys_checkbox.pack(anchor="w", padx=(10, 10), pady=(0, 0))

        self.align_values_indent_checkbox = tk.Checkbutton(
            other_options_frame, text="Align Indentation", variable=self.align_values_indent_var
        )
        self.align_values_indent_checkbox.pack(anchor="w", padx=(10, 10), pady=(0, 10))

        # Create frames for text widgets
        previous_frame = tk.Frame(main_frame)
        previous_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(10, 10))

        current_frame = tk.Frame(main_frame)
        current_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(0, 10), pady=(10, 10))

        # Label for "previous" text box
        previous_label = tk.Label(previous_frame, text="Previous:")
        previous_label.pack(side=tk.TOP)

        # "previous" text box
        self.previous_text = scrolledtext.ScrolledText(previous_frame, width=40, height=10)
        self.previous_text.pack(fill=tk.BOTH, expand=True)

        # Label for "current" text box
        current_label = tk.Label(current_frame, text="Current:")
        current_label.pack(side=tk.TOP)

        # "current" text box
        self.current_text = scrolledtext.ScrolledText(current_frame, width=40, height=10)
        self.current_text.pack(fill=tk.BOTH, expand=True)

        self.process()

    def process(self):
        """Process changes"""
        is_align_values_indentation = self.align_values_indent_var.get()

        self.previous_text.delete(1.0, tk.END)
        if self.previous_output:
            self.previous_text.insert(tk.END, self.previous_output)
        else:
            self.previous_text.insert(tk.END, self.modifier.get_source_raw_text())

        if self.annotate_var.get():
            self.modifier.annotate(self.modifier.get_obj())
        else:
            self.modifier._remove_annotations(self.modifier.get_obj())

        if self.sot_control_keys_var.get():
            self.modifier.sort_control_keys(self.modifier.get_obj())

        if self.modify_int_var.get():
            control_to_modify = self.selected_control.get()
            amount = self.modify_amount_var.get()
            self.modifier.modify_integers(self.modify_modifier_var.get(), amount, control_to_modify)

        output = self.modifier.get_pretty_printed_vdf(is_align_values_indentation)

        self.current_text.delete(1.0, tk.END)
        self.current_text.insert(tk.END, output)

        self.previous_output = output

    def run(self):
        "Show & start main loop"

        self.show()
        self.root.mainloop()

    def show(self):
        """Show gui"""
        self.root.deiconify()
        self.is_hidden = False

    def hide(self):
        """Hide gui"""
        self.root.withdraw()
        self.is_hidden = True


def debug_vdf_gui(persistent_data, vdf_path):
    """Debug GUI"""
    app = VDFModifierGUI(persistent_data, vdf_path)
    app.run()
