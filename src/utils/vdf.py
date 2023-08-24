# pylint: disable=broad-exception-caught, import-outside-toplevel
"""Class for modifying VDF files."""
import os

import send2trash
import vdf  # type: ignore

from utils.constants import DEVELOPMENT_DIR
from utils.shared_utils import replace_text_between_quotes, show_message


class VDFModifier:
    """Class for modifying VDF files."""

    def __init__(self, vdf_path=None):
        from hud.hud import Hud

        self.hud = Hud()
        self.description_key_name = "__description__"
        self.vdf_text_raw = None
        self.key_order = [
            self.description_key_name,
            "fieldname",
            "controlName",
            "visible",
            "enabled",
            "xpos",
            "ypos",
            "zpos",
            "wide",
            "tall",
            "border",
            "bgcolor_override",
            "PaintBackground",
            "PaintBackgroundType",
            "font",
            "NumberFont",
            "text_font",
            "digit_xpos",
            "digit_ypos",
            "text_xpos",
            "text_ypos",
            "wrap",
            "labelText",
            "dullText",
            "brighttext",
            "textAlignment",
            "fgcolor_override",
            "image",
            "icon",
            "icon_ypos",
            "icon_xpos",
            "icon_tall",
            "icon_wide",
            "scaleImage",
            "inverted",
            "drawcolor",
            "IconColor",
            "FlashColor",
            "pinCorner",
            "autoResize",
            "tabPosition",
            "usetitlesafe",
        ]
        self.key_order = [key.lower() for key in self.key_order]  # Convert key_order to lowercase
        self.vdf_path = vdf_path
        self.vdf_obj = self.__load_vdf() if self.vdf_path else None

        # self.print_current_vdf()

    def get_pretty_printed_vdf(self, align_value_indentation):
        """Return a pretty-printed VDF representation of the object."""
        if self.vdf_obj:
            result = vdf.dumps(self.vdf_obj, pretty=True)
            if align_value_indentation:
                result = self.__obj_align_values_with_indent_to_text(result)
            return result
        return ""

    def get_source_raw_text(self):
        """Return the original raw unmodified vdf text."""
        print("Returning raw text")
        return self.vdf_text_raw

    def get_obj(self):
        """Return the loaded VDF object."""
        if not self.vdf_obj:
            raise ValueError("No VDF object loaded")
        else:
            return self.vdf_obj

    def get_path(self):
        """Return the source VDF path."""
        return self.vdf_path

    def print_current_vdf(self):
        """Print the current VDF object."""
        if self.vdf_obj:
            print(vdf.dumps(self.vdf_obj, pretty=True))

    def __load_vdf(self):
        """Load and preprocess the VDF file."""
        print("Loading and preprocess the VDF file")
        if self.vdf_path:
            with open(self.vdf_path, encoding="utf-8") as vdf_file:
                vdf_text = vdf_file.read()
            self.vdf_text_raw = vdf_text
            cleaned_vdf_text = self.__preprocess_text(vdf_text)
            cleaned_vdf_obj = vdf.loads(cleaned_vdf_text)
            cleaned_vdf_obj = self.__preprocess_obj(cleaned_vdf_obj)
            # cleaned_vdf_obj = self.annotate(cleaned_vdf_obj)
            # cleaned_vdf_obj = self.sort_controls(cleaned_vdf_obj)
            return cleaned_vdf_obj
        return None

    def save_vdf(self, vdf_obj, output_path, align_value_indentation):
        """Save the modified VDF object to a file."""
        print("Save the modified VDF object to a file")
        if os.path.exists(output_path):
            send2trash.send2trash(output_path)  # Move the existing file to the recycle bin

        # align indentation?
        result = vdf.dumps(vdf_obj, pretty=True)  # Re-dump the loaded data
        if align_value_indentation:
            result = self.__obj_align_values_with_indent_to_text(result)

        # Verify the validity of the data format by loading it
        try:
            vdf.loads(result)  # Attempt to load the VDF object
        except Exception as err_info:
            # print(f"Invalid VDF format. Cannot save: {err_info}")
            show_message(f"Invalid VDF format. Cannot save: {err_info}", "error")
            return

        # write to disk
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(result)

    def __preprocess_text(self, vdf_text):
        """Clean up VDF text."""
        cleaned_lines = []
        for line in vdf_text.split("\n"):
            line = line.split("//", 1)[0].strip()  # Ignore text after // to handle comments
            line = line.strip()

            # eg. "if_split_screen_$WIN32" [$WIN32] or
            if ("[$" in line or "[!$ENGLISH]" in line) and "[$WIN32]" not in line:
                line = replace_text_between_quotes(line, "DELETE_ME")

            # eg. overview [$X360]
            if (
                "{" not in line
                and "}" not in line
                and '"' not in line
                and ("[$" in line or "[!$ENGLISH]" in line)
                and "[$WIN32]" not in line
            ):
                line = "DELETE_ME\n"

            cleaned_lines.append(line)

        cleaned_vdf_text = "\n".join(cleaned_lines)
        print(cleaned_vdf_text)
        return cleaned_vdf_text

    def __preprocess_obj(self, vdf_obj):
        modified_vdf_obj = vdf_obj.copy()

        # Remove entire controls with name "DELETE_ME"
        controls_to_remove = []
        controls = modified_vdf_obj[next(iter(vdf_obj))]
        for control_name in controls:
            print(f"control name = {control_name}")
            if control_name == "DELETE_ME":
                controls_to_remove.append(control_name)
        for control_name in controls_to_remove:
            del controls[control_name]

        # Remove keys or values with value "DELETE_ME"
        for controls in modified_vdf_obj.values():
            for control_data in controls.values():
                keys_to_remove = []
                for key, value in control_data.items():
                    if key == "DELETE_ME" or value == "DELETE_ME":
                        keys_to_remove.append(key)
                for key in keys_to_remove:
                    del control_data[key]

        return modified_vdf_obj

    def modify_integers(self, modifier, amount, key_to_modify):
        """Modify integer values in the VDF object."""
        print("Modifying integer values...")

        if modifier not in ["plus", "minus"]:
            raise ValueError("Invalid modifier")

        if not self.vdf_obj:
            raise ValueError("No VDF object loaded")

        def recursive_modify(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == key_to_modify:
                        data[key] = self.__modify_int_value(value, modifier, amount)
                    elif isinstance(value, dict) or isinstance(value, list):
                        recursive_modify(value)
            elif isinstance(data, list):
                for item in data:
                    recursive_modify(item)

        modified_vdf_obj = self.vdf_obj.copy()
        recursive_modify(modified_vdf_obj)
        self.vdf_obj = modified_vdf_obj
        return modified_vdf_obj

    def __modify_int_value(self, value, modifier, amount):
        """Modify integer value. Including formats such as "c-150"""
        try:
            if value[0].isalpha():
                letter = value[0]
                int_value = int(value[1:])
            else:
                letter = None
                int_value = int(value)

            if modifier == "plus":
                modified_value = int_value + amount
            elif modifier == "minus":
                modified_value = int_value - amount
            else:
                modified_value = int_value  # No modification if invalid modifier

            if letter is not None:
                modified_value_str = f"{letter}{modified_value}"
            else:
                modified_value_str = str(modified_value)

            return modified_value_str
        except ValueError:
            return value

    def annotate(self, vdf_obj):
        """Annotate file by adding descriptions"""
        # pass  # To be implemented in subclasses
        # self.hud.get_control_description()

        if not vdf_obj:
            raise ValueError("No VDF object loaded")

        modified_vdf_obj = vdf_obj.copy()
        rel_path = self.__get_relative_path(vdf_obj)
        print(rel_path)

        for controls in modified_vdf_obj.values():
            for control_name, control_data in controls.items():
                control_data[self.description_key_name] = self.hud.edit.desc.get_control_description(
                    rel_path, control_name
                )

        self.vdf_obj = modified_vdf_obj
        return modified_vdf_obj

    def remove_annotations(self, vdf_obj):
        """Remove annotations from the VDF object."""
        if not vdf_obj:
            raise ValueError("No VDF object provided")

        modified_vdf_obj = vdf_obj.copy()

        for controls in modified_vdf_obj.values():
            for control_data in controls.values():
                if self.description_key_name in control_data:
                    del control_data[self.description_key_name]

        return modified_vdf_obj

    def __get_relative_path(self, vdf_obj):
        """Get relative file path. Aka the file header for every resource file"""
        if not vdf_obj:
            raise ValueError("No VDF object loaded")

        first_key = next(iter(vdf_obj))

        modified_string = first_key.replace("/", "\\")
        if "hudlayout" in modified_string:
            modified_string = modified_string.replace("resource", "scripts")
        return modified_string

    def sort_control_keys(self, vdf_obj):
        """Sort control keys in the VDF object."""
        print("Sorting control keys...")

        # pylint: disable=unused-variable
        sorted_vdf_obj = vdf_obj.copy()

        for rel_path, controls in sorted_vdf_obj.items():
            for control_name, control_data in controls.items():
                sorted_control_data = self.__sort_control_keys(control_data)
                controls[control_name] = sorted_control_data

        self.vdf_obj = sorted_vdf_obj
        return sorted_vdf_obj

    def __sort_control_keys(self, control_data):
        """Sort control keys in the controlt."""

        # create a dictionary that maps lower case keys to original keys
        key_map = {key.lower(): key for key in control_data.keys()}
        # convert control_data keys to lower case
        control_data = {key.lower(): value for key, value in control_data.items()}
        existing_keys = [key for key in self.key_order if key in control_data]
        remaining_keys = sorted(key for key in control_data.keys() if key not in self.key_order)
        sorted_keys = existing_keys + remaining_keys
        # restore the original casing of the keys using the key_map
        sorted_control_data = {key_map[key]: control_data[key] for key in sorted_keys}
        return sorted_control_data

    @staticmethod
    def __obj_align_values_with_indent_to_text(vdf_obj):
        """Align values with indent in the VDF object."""
        lines = vdf_obj.strip().split("\n")
        result_lines = []

        current_indent = 0
        in_split_screen_block = False

        for line in lines:
            line = line.split("//", 1)[0].strip()  # Ignore text after // to handle comments
            stripped_line = line.strip()
            num_quotes = stripped_line.count('"')

            if stripped_line.endswith("{"):
                result_lines.append(" " * current_indent + stripped_line)
                current_indent += 4
            elif stripped_line == "}":
                current_indent -= 4
                result_lines.append(" " * current_indent + stripped_line)
                if in_split_screen_block:
                    in_split_screen_block = False
            else:
                parts = stripped_line.split(None, 1)
                if len(parts) == 2:
                    key, value = parts
                    if num_quotes == 2:  # Identify split screen lines by the number of quotes
                        in_split_screen_block = True
                        result_lines.append(" " * current_indent + stripped_line)
                    else:
                        aligned_line = f"{key:<20} {value}"
                        result_lines.append(" " * current_indent + aligned_line)
                else:
                    result_lines.append(" " * current_indent + stripped_line)

        return "\n".join(result_lines)


def debug_vdf_class():
    """Debug the VDFModifier class."""
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )
    # vdf_path = os.path.join(
    #     DEVELOPMENT_DIR, "debug", "vdf", "large_scoreboard - [$X360] BackgroundImage Control.res"
    # )

    modifier = "plus"  # or "minus"
    amount = 15000
    key_to_modify = "xpos"

    modifier_instance = VDFModifier(vdf_path)
    modified_vdf_obj = modifier_instance.modify_integers(modifier, amount, key_to_modify)
    modifier_instance.save_vdf(modified_vdf_obj, "output.vdf", align_value_indentation=True)
    # modifier_instance.print_current_vdf()
