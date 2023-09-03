"Debug"
import os

from game.constants import DirectoryMode
from game.game import Game
from utils.vpk import VPKClass


def debug_vpk_class():
    "Debug"
    vpk_class = VPKClass()

    g = Game()
    dev_dir = g.dir.get(DirectoryMode.DEVELOPER)
    problematic_pak_dir = os.path.join(dev_dir, "left4dead2_dlc3")
    problematic_pak_file = os.path.join(problematic_pak_dir, "pak01_dir.vpk")
    output_dir = "d:\\Downloads\\temp_folder"
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
