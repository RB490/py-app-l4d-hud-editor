# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
import os
import re

import vdf  # type: ignore

from hud.hud import Hud  # type: ignore
from utils.constants import DEVELOPMENT_DIR


class VDFModifier:
    def __init__(self, persistent_data, vdf_path=None):
        self.hud = Hud(persistent_data)
        self.description_key_name = "__description__"
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
        self.vdf_obj = self.load_vdf() if self.vdf_path else None

        # self.print_current_vdf()

    def print_current_vdf(self):
        if self.vdf_obj:
            print(vdf.dumps(self.vdf_obj, pretty=True))

    def load_vdf(self):
        if self.vdf_path:
            with open(self.vdf_path, encoding="utf-8") as vdf_file:
                vdf_content = vdf_file.read()
            cleaned_vdf_content = self.__clean_string(vdf_content)
            cleaned_vdf_obj = vdf.loads(cleaned_vdf_content)
            cleaned_vdf_obj = self.__clean_obj(cleaned_vdf_obj)
            cleaned_vdf_obj = self.__annotate(cleaned_vdf_obj)
            cleaned_vdf_obj = self.__sort_all_controls(cleaned_vdf_obj)
            return cleaned_vdf_obj
        return None

    def save_vdf(self, vdf_obj, output_path):
        result = vdf.dumps(vdf_obj, pretty=True)
        result = self.__align_values_with_indent(result)
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(result)

    def __clean_string(self, vdf_text):
        cleaned_lines = []
        for line in vdf_text.split("\n"):
            line = line.strip()
            if ("[$" in line or "[!$ENGLISH]" in line) and "[$WIN32]" not in line:
                line = replace_text_between_quotes(line, "DELETE_ME")
            cleaned_lines.append(line)

        cleaned_vdf_text = "\n".join(cleaned_lines)
        return cleaned_vdf_text

    def __clean_obj(self, vdf_obj):
        modified_vdf_obj = vdf_obj.copy()

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
        if modifier not in ["plus", "minus"]:
            raise ValueError("Invalid modifier")

        if not self.vdf_obj:
            raise ValueError("No VDF object loaded")

        modified_vdf_obj = self.vdf_obj.copy()
        for controls in modified_vdf_obj.values():
            for control_data in controls.values():
                for key, value in control_data.items():
                    if key == key_to_modify:
                        control_data[key] = self.modify_int_value(value, modifier, amount)

        return modified_vdf_obj

    def modify_int_value(self, value, modifier, amount):
        try:
            int_value = int(value)
            if modifier == "plus":
                modified_value = int_value + amount
            elif modifier == "minus":
                modified_value = int_value - amount
            else:
                modified_value = int_value  # No modification if invalid modifier
            return str(modified_value)
        except ValueError:
            return value

    def __annotate(self, vdf_obj):
        # pass  # To be implemented in subclasses
        # self.hud.get_control_description()

        if not vdf_obj:
            raise ValueError("No VDF object loaded")

        modified_vdf_obj = vdf_obj.copy()
        rel_path = self.__get_relative_path(vdf_obj)
        print(rel_path)

        for controls in modified_vdf_obj.values():
            for control_name, control_data in controls.items():
                control_data[self.description_key_name] = self.hud.desc.get_control_description(rel_path, control_name)

        return modified_vdf_obj

    def annotate(self):
        if not self.vdf_obj:
            raise ValueError("No VDF object loaded")

        self.__annotate(self.vdf_obj)

    def __get_relative_path(self, vdf_obj):
        if not vdf_obj:
            raise ValueError("No VDF object loaded")

        first_key = next(iter(vdf_obj))

        modified_string = first_key.replace("/", "\\")
        if "hudlayout" in modified_string:
            modified_string = modified_string.replace("resource", "scripts")
        return modified_string

    def __sort_control_keys(self, control_data):
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

    def __sort_all_controls(self, vdf_obj):
        # pylint: disable=unused-variable
        sorted_vdf_obj = vdf_obj.copy()

        for rel_path, controls in sorted_vdf_obj.items():
            for control_name, control_data in controls.items():
                sorted_control_data = self.__sort_control_keys(control_data)
                controls[control_name] = sorted_control_data

        return sorted_vdf_obj

    def sort_all_controls(self, vdf_obj):
        return self.__sort_all_controls(vdf_obj)

    @staticmethod
    def __align_values_with_indent(vdf_obj):
        lines = vdf_obj.strip().split("\n")
        result_lines = []

        current_indent = 0
        in_split_screen_block = False

        for line in lines:
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



def replace_text_between_quotes(input_string, replacement_text):
    pattern = r'"([^"]*)"'
    replaced_string = re.sub(pattern, f'"{replacement_text}"', input_string)
    return replaced_string


def debug_vdf_class(persistent_data):
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )

    modifier = "plus"  # or "minus"
    amount = 10
    key_to_modify = "xpos"

    modifier_instance = VDFModifier(persistent_data, vdf_path)
    modified_vdf_obj = modifier_instance.modify_integers(modifier, amount, key_to_modify)

    modifier_instance.save_vdf(modified_vdf_obj, "output.vdf")
    # modifier_instance.print_current_vdf()
