"""Creating & extracting VPK files"""
import os
import shutil
import vpk


class VPK:
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

        :param input_dir: The directory containing the files to add to the new VPK file.
        """
        # create new VPK
        new_vpk = vpk.new(input_dir)

        # (apparently this step isn't needed?)
        # iterate over all files in the input directory
        # for dirpath, dirnames, filenames in os.walk(input_dir):
        #     for filename in filenames:
        #         # add the file to the VPK
        #         full_path = os.path.join(dirpath, filename)
        #         with open(full_path, "rb") as input_file:
        #             new_vpk.add_file(full_path[len(input_dir) + 1 :], input_file.read())

        # save the VPK
        output_file = output_file_name + ".vpk"
        new_vpk.save(output_file)
        output_file = os.path.join(input_dir, output_file)
        shutil.move(output_file, os.path.join(output_dir, output_file))


if __name__ == "__main__":
    # Extracting a file
    vpk_file_class = VPK()
    # vpk_file_class.extract()

    # Creating a file
    vpk_file_class = VPK()
    # vpk_file_class.create()

    print("finished")
