# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
import os

import vdf  # type: ignore

from utils.constants import DEVELOPMENT_DIR


class VDFModifier:
    def __init__(self, vdf_path=None):
        self.vdf_path = vdf_path
        self.vdf_obj = self.load_vdf() if self.vdf_path else None

    def load_vdf(self):
        if self.vdf_path:
            with open(self.vdf_path, encoding="utf-8") as vdf_file:
                return vdf.load(vdf_file)
        return None

    def save_vdf(self, vdf_obj, output_path):
        result = vdf.dumps(vdf_obj, pretty=True)
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(result)

    def modify_controls(self):
        pass  # To be implemented in subclasses

    def clean(self):
        pass  # To be implemented in subclasses

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


def debug_vdf_class():
    vdf_path = os.path.join(
        DEVELOPMENT_DIR, "debug", "vdf", "tiny_hudlayout - [$X360] nested key-value definition.res"
    )

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
