"""A class representing a VPK (Valve Package) file."""
# pylint: disable=broad-exception-caught, protected-access, invalid-name, logging-fstring-interpolation
import os
import shutil
import subprocess
import tempfile

import vpk  # type: ignore
from loguru import logger as logger

from shared_utils.shared_utils import copy_directory
from utils.constants import VPK_EXE_EXTRACT


class VPKClass:
    """
    A class representing a VPK (Valve Package) file.

    This class provides methods for extracting files from a VPK file and
    creating a new VPK file from a directory of files.
    """

    def _validate_extract_params(self, input_file: str, output_dir: str) -> bool:
        logger.debug(f"Verifying parameters input_file: '{input_file}' and output_dir: '{output_dir}'")

        # Check if input_file exists and is a VPK file
        if not os.path.isfile(input_file) or not input_file.endswith(".vpk"):
            raise ValueError("Input file does not exist or is not a VPK file")

        # Raise esception if output_dir is a file
        if os.path.isfile(output_dir):
            raise ValueError(f"Output directory is a file! ''{output_dir}''")

        # Create output directory if it doesn't exist
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
            logger.debug(f"Created output directory: '{output_dir}'")

        logger.debug(f"Verified parameters! intput_file '{input_file}' and output_dir: '{output_dir}'")
        return True

    def extract(self, input_file: str, output_dir: str) -> None:
        """
        Extract all files from the VPK file to the specified output directory using the vpk module

        :param input_file: The path to the VPK file.
        :param output_dir: The directory to extract the files to.
        """
        if not self._validate_extract_params(input_file, output_dir):
            return

        self._extract_alternate(input_file, output_dir)
        return

        # just using nosteam for everything. because issues... see readme in vpk.exe directory
        # pylint: disable=unreachable
        logger.info(f"Extracting '{input_file}' -> '{output_dir}'")

        # Extract VPK file
        with vpk.open(input_file) as vpk_file:
            try:
                for file_path in vpk_file:
                    full_path = os.path.join(output_dir, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    try:
                        with open(full_path, "wb") as output_file:
                            output_file.write(vpk_file[file_path].read())
                        logger.debug(f"Extract '{file_path}'")
                    except Exception as file_extract_err:
                        logger.error(f"Error extracting file '{file_path}': {str(file_extract_err)}")
                        continue
            except Exception as extract_err:
                logger.error(f"Error extracting pak01.vpk ''{input_file}'': {str(extract_err)}")
                self._extract_alternate(input_file, output_dir)

        # finish
        logger.info(f"Extracted '{input_file}' -> '{output_dir}'!")

    def _extract_alternate(self, input_file: str, output_dir: str) -> None:
        """
        Extract all files from the VPK file to the specified output directory using vpk.exe from the game dir

        :param input_file: The path to the VPK file.
        :param output_dir: The directory to extract the files to.
        """
        if not self._validate_extract_params(input_file, output_dir):
            return

        logger.info(f"Extracting '{input_file}' -> '{output_dir}' using alternative method")

        # Variables
        input_file_base = os.path.splitext(os.path.basename(input_file))[0]
        input_file_dir = os.path.dirname(input_file)
        extract_dir = os.path.join(input_file_dir, input_file_base)
        input_file_quoted = f"{input_file}"
        extract_command = [VPK_EXE_EXTRACT, input_file_quoted]

        # Cleanup extract directory (extracted contents) incase it exists
        self._delete_extracting_dir(extract_dir)

        # Run vpk.exe to extract the contents of the input_file
        try:
            subprocess.run(extract_command, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Error extracting '{input_file}': {e}")
            return

        # Move the extracted contents to the destination directory
        copy_directory(extract_dir, output_dir)

        # Finish
        self._delete_extracting_dir(extract_dir)
        logger.info(f"Extracted '{input_file}' -> '{output_dir}' using alternative method!")

    def _delete_extracting_dir(self, dir_path: str) -> None:
        """
        Delete an extracted directory.

        :param dir_path: The path to the directory to delete.
        """
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            logger.debug(f"Deleted directory: {dir_path}")

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

        logger.info(f"Creating '{output_file_name}' from '{input_dir}' in '{output_dir}'!")

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
            logger.info(f"Created '{output_file_name}' from '{input_dir}' in '{output_dir}'!")
        except Exception as err:
            logger.warning(f"Error creating '{output_file_name}' from '{input_dir}' in ! {err}")
        finally:
            # Clean temporary directory
            shutil.rmtree(temp_dir)
            logger.debug(f"Cleaned up temporary directory: '{temp_dir}'")

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
        logger.debug(f"Created temporary directory without files without a file extension: '{temp_dir}'")
        return temp_dir
