# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
import os
import re

import vdf  # type: ignore

from utils.constants import DEVELOPMENT_DIR


class VDFModifier:
    def __init__(self, vdf_path=None):
        self.vdf_path = vdf_path
        self.vdf_obj = self.load_vdf() if self.vdf_path else None
        self.print_current_vdf()

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
            return cleaned_vdf_obj
        return None

    def save_vdf(self, vdf_obj, output_path):
        result = vdf.dumps(vdf_obj, pretty=True)
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(result)

    def modify_controls(self):
        pass  # To be implemented in subclasses

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
        keys_to_delete = []

        for controls in modified_vdf_obj.values():
            for control_data in controls.values():
                keys_to_remove = []
                for key, value in control_data.items():
                    if key == "DELETE_ME" or value == "DELETE_ME":
                        keys_to_remove.append(key)
                for key in keys_to_remove:
                    del control_data[key]

        return modified_vdf_obj

    def annotate(self):
        pass  # To be implemented in subclasses


class IntModifier(VDFModifier):
    def __init__(self, vdf_path=None, modifier=None, amount=None, key_to_modify=None):
        super().__init__(vdf_path)
        self.key_to_modify = key_to_modify or "xpos"
        self.modifier = modifier
        self.amount = amount

    def modify_controls(self):
        if not self.vdf_obj or not self.modifier or self.amount is None:
            raise ValueError("Incomplete configuration for modification")

        modified_vdf_obj = self.vdf_obj.copy()
        for controls in modified_vdf_obj.values():
            for control_data in controls.values():
                for key, value in control_data.items():
                    if key == self.key_to_modify:
                        control_data[key] = self.modify_integers(value)
        return modified_vdf_obj

    def modify_integers(self, value):
        try:
            int_value = int(value)
            if self.modifier == "plus":
                modified_value = int_value + self.amount
            elif self.modifier == "minus":
                modified_value = int_value - self.amount
            else:
                modified_value = int_value  # No modification if invalid modifier
            return str(modified_value)
        except ValueError:
            return value


def remove_blocks(lines, block_identifier):
    filtered_lines = []
    inside_block = False

    for line in lines:
        if "{" in line:
            if block_identifier in line:
                inside_block = True
        elif "}" in line:
            if inside_block:
                inside_block = False
            else:
                filtered_lines.append(line)
        elif block_identifier in line and not inside_block:
            continue

        if not inside_block:
            filtered_lines.append(line)

    return filtered_lines


def print_modified_vdf(vdf_content, block_identifier):
    try:
        modified_lines = remove_blocks(vdf_content, block_identifier)

        # Print the modified content
        modified_content = "".join(modified_lines)
        print(modified_content)
        return modified_content
    except FileNotFoundError:
        print("No content available.")


def replace_text_between_quotes(input_string, replacement_text):
    pattern = r'"([^"]*)"'
    replaced_string = re.sub(pattern, f'"{replacement_text}"', input_string)
    return replaced_string


def clean_vdf(data):
    lines = data.split("\n")
    output = []

    for line in lines:
        line = line.strip()

        if ("[$" in line or "[!$ENGLISH]" in line) and "[$WIN32]" not in line:
            line = replace_text_between_quotes(line, "DELETE_ME")

        output.append(line)

    return "\n".join(output)


def debug_vdf_class():
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )

    modifier = VDFModifier(vdf_path)
    # cleaned_vdf_text = modifier.clean()
    return

    modifier = "plus"  # Modifier ("plus", "minus")
    amount = 100  # Amount to modify with

    int_modifier = IntModifier(vdf_path, modifier, amount)
    modified_vdf_obj = int_modifier.modify_controls()

    # Save to an output path if needed
    output_path = "output.vdf"  # Replace with desired output path or leave None
    if output_path:
        int_modifier.save_vdf(modified_vdf_obj, output_path)
        print(f"Modified VDF saved to '{output_path}':")
    else:
        print("Modified VDF (not saved):")

    print(vdf.dumps(modified_vdf_obj, pretty=True))


if __name__ == "__main__":
    debug_vdf_class()
