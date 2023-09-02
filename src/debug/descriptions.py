"""Debug descriptions"""
from hud.descriptions import HudDescriptions


def debug_hud_descriptions_class():
    """Debug descriptions"""
    print("hi there!")
    desc = HudDescriptions()
    # file_name = "hudlayout.res"
    file_name = "debug_file.txt"
    # result = desc.get_control_description(file_name, "HudWeaponSelection")
    result = desc.set_file_relative_path(file_name, "some\\path")

    print(f"desc result = {result}")


def test_hud_descriptions():
    """Test hud description class"""
    # Create a HudDescriptions instance
    descr = HudDescriptions()

    # Sample data for testing
    file_name = "sample.txt"
    input_control = "control1"
    control_desc = "Control description"
    file_desc = "File description"
    rela_path = "scripts\\sample.txt"

    # Test add_control
    descr.add_control(file_name, input_control)

    # Test set_control_description
    descr.set_control_description(file_name, input_control, control_desc)

    # Test set_file_description
    descr.set_file_description(rela_path, file_desc)

    # Test get_control_description
    retrieved_control_desc = descr.get_control_description(file_name, input_control)
    assert retrieved_control_desc == control_desc

    # Test get_file_description
    retrieved_file_desc = descr.get_file_description(file_name)
    assert retrieved_file_desc == file_desc

    # Test get_custom_file_status
    custom_status = descr.get_custom_file_status(file_name)
    assert custom_status is False  # Assuming it's not custom in this test

    # Test get_controls
    retrieved_controls = descr.get_controls(file_name)
    assert input_control in retrieved_controls

    # Test remove_control
    descr.remove_control(file_name, input_control)
    retrieved_controls = descr.get_controls(file_name)
    assert input_control not in retrieved_controls

    # Test get_all_descriptions
    all_descriptions = descr.get_all_descriptions()
    assert file_name in all_descriptions

    # Test remove_entry
    descr.remove_entry(file_name)
    retrieved_file_desc = descr.get_file_description(file_name)
    assert retrieved_file_desc == ""  # File should be removed

    print("All HudDescriptions methods tested successfully!")
