# pylint: disable=protected-access, unspecified-encoding, missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name
import hashlib
import os
import random
import string
import tempfile
import unittest
from unittest.mock import patch

from hud.syncer import (
    HudSyncer,
    calculate_md5_hash,
    files_differ,
    get_all_files_and_dirs,
    get_subdirectories_names,
)


class TestHudSyncer(unittest.TestCase):
    def _create_file(self, path):
        with open(path, "w") as file:
            random_text = "".join(random.choices(string.ascii_letters + string.digits, k=10))
            file.write(random_text)

    def create_fake_source_files(self):
        self.fake_source_dir = os.path.join(self.temp_dir, "my_source_dir")
        os.makedirs(self.fake_source_dir, exist_ok=True)

        self._create_file(os.path.join(self.fake_source_dir, "my_source_test_file.txt"))
        os.makedirs(os.path.join(self.fake_source_dir, "scripts"))
        self._create_file(os.path.join(self.fake_source_dir, "scripts", "hudlayout.res"))
        os.makedirs(os.path.join(self.fake_source_dir, "my_custom_source_folder"))
        self._create_file(os.path.join(self.fake_source_dir, "my_custom_source_folder", "my_custom_source_file.txt"))

    def create_fake_target_files(self):
        self.fake_target_dir = os.path.join(self.temp_dir, "my_target_dir")
        os.makedirs(self.fake_target_dir, exist_ok=True)

        self.fake_target_sub_dir = os.path.join(self.fake_target_dir, "left4dead2")
        os.makedirs(self.fake_target_sub_dir, exist_ok=True)
        self._create_file(os.path.join(self.fake_target_sub_dir, "just_some_target_file.txt"))
        os.makedirs(os.path.join(self.fake_target_sub_dir, "materials"))
        os.makedirs(os.path.join(self.fake_target_sub_dir, "scripts"))
        self._create_file(os.path.join(self.fake_target_sub_dir, "scripts", "hudlayout.res"))

        self.fake_target_sub_dir_dlc1 = os.path.join(self.fake_target_dir, "left4dead2_dlc1")
        os.makedirs(self.fake_target_sub_dir_dlc1, exist_ok=True)
        os.makedirs(os.path.join(self.fake_target_sub_dir_dlc1, "materials"))
        os.makedirs(os.path.join(self.fake_target_sub_dir_dlc1, "scripts"))
        self._create_file(os.path.join(self.fake_target_sub_dir_dlc1, "scripts", "hudlayout.res"))

    def setUp(self):
        self.syncer = HudSyncer()
        # Create a temporary directory to use as source and target
        self.test_dir = tempfile.mkdtemp()
        self.temp_dir = os.path.join(self.test_dir, "hud_sync_debug")
        # self.temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_test_dir", "hud_sync_debug")
        # shutil.rmtree(self.temp_dir)
        # os.makedirs(self.temp_dir, exist_ok=True)

        # Create the required files and directories for source
        self.create_fake_source_files()

        # Create the required files and directories for target
        self.create_fake_target_files()

        self.fake_main_name = "left4dead2"

    def tearDown(self):
        # shutil.rmtree(self.test_dir)
        # shutil.rmtree(self.temp_dir)
        pass

    @patch("builtins.print")  # Mock the print function
    def test_sync(self, mock_print):
        self.syncer.target_sub_dir_names = ["left4dead2", "left4dead2_dlc1"]

        fake_main_dir = os.path.join(self.fake_target_dir, self.fake_main_name)
        fake_main_sub_dir = os.path.join(self.fake_target_dir, self.syncer.target_sub_dir_names[1])

        self.syncer.sync(self.fake_source_dir, self.fake_target_dir, self.fake_main_name)

        # Assertions for variable validity
        self.assertEqual(self.syncer.source_dir, self.fake_source_dir)
        self.assertEqual(self.syncer.target_dir_root, self.fake_target_dir)
        self.assertEqual(self.syncer.target_dir_main_name, self.fake_main_name)
        self.assertTrue(self.syncer.is_synced)
        self.assertIn(self.fake_main_name, self.syncer.target_sub_dir_names)

        # Assertions for directory structure
        required_dirs = [
            self.syncer.target_dir_root,
            os.path.join(self.syncer.target_dir_root, "left4dead2"),
            os.path.join(self.syncer.target_dir_root, "left4dead2", "scripts"),
            os.path.join(self.syncer.target_dir_root, "left4dead2_dlc1"),
            os.path.join(self.syncer.target_dir_root, "left4dead2_dlc1", "scripts"),
        ]
        for dir_path in required_dirs:
            self.assertTrue(os.path.isdir(dir_path))

        # Assertions for synced files and folders
        synced_files = [
            os.path.join(fake_main_dir, "my_source_test_file.txt"),
            os.path.join(fake_main_dir, "my_custom_source_folder"),
            os.path.join(fake_main_dir, "my_custom_source_folder", "my_custom_source_file.txt"),
            os.path.join(fake_main_dir, "scripts", "hudlayout.res.backup"),
            os.path.join(fake_main_sub_dir, "scripts", "hudlayout.res.backup"),
        ]
        for file_path in synced_files:
            self.assertTrue(os.path.exists(file_path))

    @patch("builtins.print")  # Mock the print function
    def test_unsync(self, mock_print):
        # Set up syncer instance and attributes
        self.syncer.source_dir = self.fake_source_dir
        self.syncer.target_dir_root = self.fake_target_dir
        self.syncer.target_dir_main_name = self.fake_main_name
        self.syncer.target_sub_dir_names = ["left4dead2", "left4dead2_dlc1"]
        self.syncer.is_synced = True

        fake_main_dir = os.path.join(self.fake_target_dir, self.fake_main_name)
        fake_main_sub_dir = os.path.join(self.fake_target_dir, self.syncer.target_sub_dir_names[1])

        # Manually set the hud_items attribute with example values
        self.syncer.hud_items = get_all_files_and_dirs(self.fake_source_dir)

        # Perform sync and unsync
        self.syncer.sync(self.fake_source_dir, self.fake_target_dir, self.fake_main_name)
        print(f"custom items: {self.syncer.hud_items_custom}")
        self.syncer.unsync()

        # Assertions for directory structure
        self.assertTrue(os.path.isdir(self.syncer.source_dir))
        self.assertTrue(os.path.isdir(self.syncer.target_dir_root))
        for subdir_name in self.syncer.target_sub_dir_names:
            self.assertTrue(os.path.isdir(os.path.join(self.syncer.target_dir_root, subdir_name)))
            self.assertTrue(os.path.isdir(os.path.join(self.syncer.target_dir_root)))

        os.startfile(self.fake_target_dir)

    def test_calculate_md5_hash(self):
        content = "test data"
        file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(file_path, "w") as f:
            f.write(content)
        expected_hash = hashlib.md5(content.encode()).hexdigest()

        result = calculate_md5_hash(file_path)

        self.assertEqual(expected_hash, result)

    def test_files_differ(self):
        file_path1 = os.path.join(self.test_dir, "file1.txt")
        file_path2 = os.path.join(self.test_dir, "file2.txt")
        with open(file_path1, "w") as f1, open(file_path2, "w") as f2:
            f1.write("data1")
            f2.write("data2")

        result = files_differ(file_path1, file_path2)

        self.assertTrue(result)

    def test_get_all_files_and_dirs(self):
        dir_path = os.path.join(self.test_dir, "test_dir")
        os.mkdir(dir_path)
        file_path = os.path.join(dir_path, "file.txt")
        with open(file_path, "w") as f:
            f.write("test data")

        result = get_all_files_and_dirs(self.test_dir)

        self.assertIn(dir_path, result)
        self.assertIn(file_path, result)

    def test_get_subdirectories_names(self):
        dir_path = os.path.join(self.test_dir, "test_dir")
        os.mkdir(dir_path)

        result = get_subdirectories_names(self.test_dir)

        self.assertIn("test_dir", result)


if __name__ == "__main__":
    unittest.main()


def debug_hud_syncer():
    # pylint: disable=line-too-long
    """Debugs the hud syncer class"""

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestHudSyncer))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
