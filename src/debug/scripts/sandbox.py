def fix_indent(text):
    lines = text.split('\n')
    indent_level = 0
    fixed_lines = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.endswith("{"):
            fixed_lines.append("    " * indent_level + stripped_line)
            indent_level += 1
        elif stripped_line.endswith("}"):
            indent_level -= 1
            fixed_lines.append("    " * indent_level + stripped_line)
        else:
            fixed_lines.append("    " * indent_level + line)

    return '\n'.join(fixed_lines)

input_text = '''
"resource/hudlayout.res"
{
    "overview"
    {
        "__description__"    "None"
        "fieldname"          "overview"
        "visible"            "1"
        "enabled"            "1"
        "xpos"               "10"
        "ypos"               "480"
        "wide"               "0"
        "tall"               "0"
    }
    "HudZombiePanel"
    {
        "__description__"    "Infected Tank approaching / Too far from Survivors"
        "fieldName"          "HudZombiePanel"
        "visible"            "1"
        "enabled"            "1"
        "xpos"               "c-100"
        "ypos"               "c10"
        "wide"               "400"
        "tall"               "155"
        "if_split_screen_$WIN32"
        {
            "xpos"               "c-360"
        }
        "if_split_screen_horizontal"
        {
            "ypos"               "c-45"
        }
        "if_split_screen_left"
        {
            "xpos"               "c-145"
        }
        "if_split_screen_right"
        {
            "xpos"               "c-100"
        }
    }
}
'''

fixed_text = fix_indent(input_text)
print(fixed_text)
