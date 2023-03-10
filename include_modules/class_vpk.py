import os
# import tkinter as tk
import vpk


class VPK:
    """
    A class representing a VPK (Valve Package) file.

    VPK files are used by the Source engine in many Valve games to store game assets.

    This class provides methods for extracting files from a VPK file and creating a new VPK file from a directory of files.
    """

    def __init__(self, filename):
        """
        Initialize a new VPK object with the given filename.

        :param filename: The filename of the VPK file to operate on.
        """
        self.filename = filename

    def extract(self, output_dir):
        """
        Extract all files from the VPK file to the specified output directory.

        :param output_dir: The directory to extract the files to.
        """
        # Check if self.filename exists and is a VPK file
        if not os.path.exists(self.filename) or not self.filename.endswith(".vpk"):
            raise ValueError("File does not exist or is not a VPK file")

        # create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # open VPK file
        with vpk.open(self.filename) as vpk_file:
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
            except Exception as e:
                # tk.messagebox.showerror("Error", str(e))
                print(f'Extract error: {str(e)}')

    def create(self, input_dir):
        """
        Create a new VPK file from the specified input directory.

        :param input_dir: The directory containing the files to add to the new VPK file.
        """
        # create new VPK
        new_vpk = vpk.new(os.path.splitext(self.filename)[0])

        # iterate over all files in the input directory
        for dirpath, dirnames, filenames in os.walk(input_dir):
            for filename in filenames:
                # add the file to the VPK
                full_path = os.path.join(dirpath, filename)
                with open(full_path, "rb") as input_file:
                    new_vpk.add_file(full_path[len(input_dir) + 1 :], input_file.read())

        # save the VPK
        new_vpk.save(os.path.splitext(self.filename)[0] + ".vpk")


if __name__ == "__main__":
    # Extracting a file
    vpk_file = VPK(
        "E:\Games\Steam\steamapps\common\Left 4 Dead 2\left4dead2\pak01_dir.vpk"
    )
    vpk_file.extract("D:\Downloads\extracted_python")
    # Creating a file
    vpk_file = VPK("D:\Downloads\extracted_python")
    vpk_file.create("D:\Downloads\pak01_dir_python")

    print("finished")
