"""Creating & extracting VPK files"""
import os
import shutil

import vpk

from packages.utils.functions import (
    create_temp_dir_from_input_dir_exclude_files_without_extension,
)


class VPKClass:
    """
    A class representing a VPK (Valve Package) file.

    This class provides methods for extracting files from a VPK file and
    creating a new VPK file from a directory of files.
    """

    def __init__(self):
        """
        Initialize a new VPK object with the given filename.

        :param filename: The filename of the VPK file to operate on.
        """

    def extract(self, input_file, output_dir):
        """
        Extract all files from the VPK file to the specified output directory.

        :param output_dir: The directory to extract the files to.
        """
        # Check if self.filename exists and is a VPK file
        if not os.path.exists(input_file) or not input_file.endswith(".vpk"):
            raise ValueError("File does not exist or is not a VPK file")

        # create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # open VPK file
        with vpk.open(input_file) as vpk_file:
            # iterate over all files in the VPK
            try:
                for filepath in vpk_file:
                    # create directories if necessary
                    full_path = os.path.join(output_dir, filepath)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)

                    # extract the file
                    with open(full_path, "wb") as output_file:
                        # print(f'writing file: {full_path} -> output_file: {output_file}')
                        output_file.write(vpk_file[filepath].read())
            except NotImplementedError as err_info:
                # tk.messagebox.showerror("Error", str(e))
                print(f"Extract error: {str(err_info)}")

    def create(self, input_dir, output_dir, output_file_name):
        """
        Create a new VPK file from the specified input directory.

        :param input_directory: The directory containing the files to add to the new VPK file.
        :param output_directory: The directory where the new VPK file will be saved.
        :param output_file_name: The name of the new VPK file.
        """
        # verify input parameters
        if not os.path.exists(input_dir):
            raise ValueError(f"input_directory does not exist: {input_dir}")
        elif not os.path.exists(output_dir):
            raise ValueError(f"output_directory does not exist: {output_dir}")

        # exclude files without extensions as they are not supported
        vpk_dir = create_temp_dir_from_input_dir_exclude_files_without_extension(input_dir)

        # create new VPK
        new_vpk = vpk.new(vpk_dir)

        # save the VPK
        output_file_name = os.path.splitext(output_file_name)[0] + ".vpk"
        output_path = os.path.normpath(os.path.join(output_dir, output_file_name))
        new_vpk.save(output_path)
        print(f"Created VPK: {output_path}")

        # clean temporary dir
        shutil.rmtree(vpk_dir)


if __name__ == "__main__":
    # Extracting a file
    vpk_file_class = VPKClass()
    # vpk_file_class.extract()

    # Creating a file
    vpk_file_class = VPKClass()
    # vpk_file_class.create()

    print("finished")
