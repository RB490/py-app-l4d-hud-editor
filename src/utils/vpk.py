"""A class representing a VPK (Valve Package) file."""
# pylint: disable=broad-exception-caught
import os
import shutil

import vpk  # type: ignore

from utils.functions import (
    create_temp_dir_from_input_dir_exclude_files_without_extension,
)


class VPKClass:
    """
    A class representing a VPK (Valve Package) file.

    This class provides methods for extracting files from a VPK file and
    creating a new VPK file from a directory of files.
    """

    def extract(self, input_file: str, output_dir: str) -> None:
        """
        Extract all files from the VPK file to the specified output directory.

        :param input_file: The path to the VPK file.
        :param output_dir: The directory to extract the files to.
        """
        # Check if input_file exists and is a VPK file
        if not os.path.exists(input_file) or not input_file.endswith(".vpk"):
            raise ValueError("Input file does not exist or is not a VPK file")

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Extract VPK file
        with vpk.open(input_file) as vpk_file:
            for file_path in vpk_file:
                full_path = os.path.join(output_dir, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                try:
                    with open(full_path, "wb") as output_file:
                        output_file.write(vpk_file[file_path].read())
                except Exception as extract_err:
                    print(f"Error extracting file '{file_path}': {str(extract_err)}")

    def create(self, input_dir: str, output_dir: str, output_file_name: str) -> None:
        """
        Create a new VPK file from the specified input directory.

        :param input_dir: The directory containing the files to add to the new VPK file.
        :param output_dir: The directory where the new VPK file will be saved.
        :param output_file_name: The name of the new VPK file.
        """
        # Verify input parameters
        if not os.path.exists(input_dir):
            raise ValueError(f"Input directory does not exist: {input_dir}")
        elif not os.path.exists(output_dir):
            raise ValueError(f"Output directory does not exist: {output_dir}")

        # Exclude files without extensions as they are not supported
        vpk_dir = create_temp_dir_from_input_dir_exclude_files_without_extension(input_dir)

        try:
            # Create new VPK
            new_vpk = vpk.new(vpk_dir)

            # Set the output file name with .vpk extension
            output_file_name = os.path.splitext(output_file_name)[0] + ".vpk"
            output_path = os.path.join(output_dir, output_file_name)

            # Save the VPK
            new_vpk.save(output_path)
            print(f"Created VPK: {output_path}")
        except Exception as err:
            print(f"Error creating VPK: {err}")
        finally:
            # Clean temporary directory
            shutil.rmtree(vpk_dir)


def debug_vpk_class():
    "Debug"
    vpk_file_class = VPKClass()

    # Example usage: Extracting files from a VPK
    input_file = "input.vpk"
    output_dir = "extracted_files"
    vpk_file_class.extract(input_file, output_dir)

    # Example usage: Creating a new VPK
    input_dir = "input_folder"
    output_dir = "output_folder"
    output_file_name = "output.vpk"
    vpk_file_class.create(input_dir, output_dir, output_file_name)

    print("Finished")
