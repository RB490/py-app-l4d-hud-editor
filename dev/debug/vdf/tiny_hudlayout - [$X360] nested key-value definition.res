"resource/hudlayout.res"
{
    "overview"
    {
        "__description__"    "None"
        "fieldname"          "overview"
        "visible"            "1"
        "enabled"            "1"
        "xpos"               "0"
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
        "custom_key_block"
        {
            "ypos"               "c-45"
        }
        "if_split_screen_$WIN32"
        {
            "xpos"               "c-360"
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