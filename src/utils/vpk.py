"""A class representing a VPK (Valve Package) file."""
# pylint: disable=broad-exception-caught, protected-access, invalid-name, logging-fstring-interpolation
import logging
import os
import shutil
import subprocess
import tempfile

import vpk  # type: ignore

from shared_utils.logging_manager import LoggingManager
from shared_utils.shared_utils import copy_directory
from utils.constants import VPK_EXE

logging_manager = LoggingManager(__name__, level=logging.INFO)
log = logging_manager.get_logger()


class VPKClass:
    """
    A class representing a VPK (Valve Package) file.

    This class provides methods for extracting files from a VPK file and
    creating a new VPK file from a directory of files.
    """

    def _validate_extract_params(self, input_file: str, output_dir: str) -> bool:
        log.debug(f"Verifying parameters input_file: '{input_file}' and output_dir: '{output_dir}'")

        # Check if input_file exists and is a VPK file
        if not os.path.isfile(input_file) or not input_file.endswith(".vpk"):
            raise ValueError("Input file does not exist or is not a VPK file")

        # Raise esception if output_dir is a file
        if os.path.isfile(output_dir):
            raise ValueError(f"Output directory is a file! ''{output_dir}''")

        # Create output directory if it doesn't exist
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
            log.debug(f"Created output directory: '{output_dir}'")

        log.debug(f"Verified parameters! intput_file '{input_file}' and output_dir: '{output_dir}'")
        return True

    def extract(self, input_file: str, output_dir: str) -> None:
        """
        Extract all files from the VPK file to the specified output directory using the vpk module

        :param input_file: The path to the VPK file.
        :param output_dir: The directory to extract the files to.
        """
        if not self._validate_extract_params(input_file, output_dir):
            return

        log.info(f"Extracting '{input_file}' -> '{output_dir}'")

        # Extract VPK file
        with vpk.open(input_file) as vpk_file:
            try:
                for file_path in vpk_file:
                    full_path = os.path.join(output_dir, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    try:
                        with open(full_path, "wb") as output_file:
                            output_file.write(vpk_file[file_path].read())
                        log.debug(f"Extract '{file_path}'")
                    except Exception as file_extract_err:
                        log.error(f"Error extracting file '{file_path}': {str(file_extract_err)}")
                        continue
            except Exception as extract_err:
                log.error(f"Error extracting pak01.vpk ''{input_file}'': {str(extract_err)}")
                self._extract_alternate(input_file, output_dir)

        # finish
        log.info(f"Extracted '{input_file}' -> '{output_dir}'!")

    def _extract_alternate(self, input_file: str, output_dir: str) -> None:
        """
        Extract all files from the VPK file to the specified output directory using vpk.exe from the game dir

        :param input_file: The path to the VPK file.
        :param output_dir: The directory to extract the files to.
        """
        if not self._validate_extract_params(input_file, output_dir):
            return

        log.info(f"Extracting '{input_file}' -> '{output_dir}' using alternative method")

        # Run vpk.exe to extract the contents of the input_file
        input_file_quoted = f"{input_file}"
        extract_command = [VPK_EXE, input_file_quoted]

        try:
            subprocess.run(extract_command, check=True)
        except subprocess.CalledProcessError as e:
            log.error(f"Error extracting '{input_file}': {e}")
            return

        # Get the base name of the input file without the extension
        input_file_base = os.path.splitext(os.path.basename(input_file))[0]

        # Construct the source directory path (extracted contents)
        source_dir = os.path.join(output_dir, input_file_base)

        # Construct the destination directory path
        destination_dir = os.path.join(os.path.dirname(input_file))

        # Move the extracted contents to the destination directory
        copy_directory(source_dir, destination_dir)

        # Cleanup source directory (extracted contents)
        shutil.rmtree(source_dir)
        log.debug(f"Deleted source directory! {source_dir}")

        log.info(f"Extracted '{input_file}' -> '{output_dir}' using alternative method!")

    def create(self, input_dir: str, output_dir: str, output_file_name: str) -> None:
        """
        Create a new VPK file from the specified input directory.

        :param input_dir: The directory containing the files to add to the new VPK file.
        :param output_dir: The directory where the new VPK file will be saved.
        :param output_file_name: The name of the new VPK file.
        """
        # Verify input parameters
        if not os.path.exists(input_dir):
            raise ValueError(f"Input directory does not exist: '{input_dir}'")

        log.info(f"Creating '{output_file_name}' from '{input_dir}' in '{output_dir}'!")

        # Exclude files without extensions as they are not supported
        temp_dir = self._create_temp_dir_excluding_files_without_file_extension(input_dir)

        try:
            # Create new VPK
            new_vpk = vpk.new(temp_dir)

            # Set the output file name with .vpk extension
            output_file_name = os.path.splitext(output_file_name)[0] + ".vpk"
            output_path = os.path.join(output_dir, output_file_name)

            # Save the VPK
            new_vpk.save(output_path)
            log.info(f"Created '{output_file_name}' from '{input_dir}' in '{output_dir}'!")
        except Exception as err:
            log.warning(f"Error creating '{output_file_name}' from '{input_dir}' in ! {err}")
        finally:
            # Clean temporary directory
            shutil.rmtree(temp_dir)
            log.debug(f"Cleaned up temporary directory: '{temp_dir}'")

    def _create_temp_dir_excluding_files_without_file_extension(self, input_dir):
        # pylint: disable=unused-variable
        """
        Creates a temporary directory and copies the contents of the input directory to it,
        excluding any files without a file extension.

        :param input_dir: The path of the input directory.
        :type input_dir: str
        :return: The path of the temporary directory.
        :rtype: str
        """
        temp_dir = tempfile.mkdtemp()
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if "." in file:
                    file_path = os.path.join(root, file)
                    temp_path = os.path.join(temp_dir, file)
                    shutil.copy2(file_path, temp_path)
        log.debug(f"Created temporary directory without files without a file extension: '{temp_dir}'")
        return temp_dir


def debug_vpk_class():
    "Debug"
    vpk_class = VPKClass()

    problematic_pak_file = "E:\\Games\\Steam\\steamapps\\common\\Left 4 Dead 2 dev\\left4dead2_dlc3\\pak01_dir.vpk"
    output_dir = "E:\\Games\\Steam\\steamapps\\common\\Left 4 Dead 2 dev\\left4dead2_dlc3"
    # vpk_class.extract(problematic_pak_file, output_dir)
    vpk_class._extract_alternate(problematic_pak_file, output_dir)
    # print(f"result = {result}")

    # # Example usage: Extracting files from a VPK
    # input_file = "input.vpk"
    # output_dir = "extracted_files"
    # vpk_file_class.extract(input_file, output_dir)

    # # Example usage: Creating a new VPK
    # input_dir = "input_folder"
    # output_dir = "output_folder"
    # output_file_name = "output.vpk"
    # vpk_file_class.create(input_dir, output_dir, output_file_name)

    print("Finished")
