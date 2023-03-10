// Versus spawning tutorial panel
"Resource/UI/SpawnModeMenu.res"
{

	ContinueBind
	{
		"fieldname"    "ContinueBind"
		"controlName"  "CBindPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "0"
		"ypos"         "70"
		"zpos"         "2"
		"bind"         "+attack"
	}

	ContinueLabel
	{
		"fieldname"             "ContinueLabel"
		"controlName"           "Label"
		"visible"               "1"
		"enabled"               "1"
		"xpos"                  "0"
		"ypos"                  "73"
		"zpos"                  "2"
		"wide"                  "10"
		"tall"                  "25"
		"auto_wide_tocontents"  "1"
		"fgcolor_override"      "200 200 200 255"
		"font"                  "Cerbetica14Shadow"
		"labelText"             "#L4D_btn_continue"
		"textAlignment"         "center"
		"wrap"                  "0"
	}

	ModeTitle
	{
		"fieldname"      "ModeTitle"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "0"
		"ypos"           "34"
		"zpos"           "1"
		"wide"           "400"
		"tall"           "15"
		"autoResize"     "0"
		"brighttext"     "0"
		"dulltext"       "0"
		"font"           "Cerbetica18Shadow"
		"labelText"      "#L4D_spawn_select_mode_title"
		"pinCorner"      "0"
		"textAlignment"  "center"
		"wrap"           "0"
		"bgcolor_override"			""
	}

	spawnmode
	{
		"fieldname"               "spawnmode"
		"controlName"             "Frame"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "c-200"
		"ypos"                    "c40"
		"wide"                    "400"
		"tall"                    "155"
		"autoResize"              "0"
		"padding"                 "0"
		"pinCorner"               "0"
		"tabPosition"             "0"
	}

	SpawnModeOneText
	{
		"fieldname"      "SpawnModeOneText"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "0"
		"ypos"           "50"
		"zpos"           "1"
		"wide"           "400"
		"tall"           "15"
		"autoResize"     "0"
		"brighttext"     "0"
		"dulltext"       "0"
		"font"           "Cerbetica10Shadow"
		"labelText"      "#L4D_spawn_select_mode_text_1"
		"pinCorner"      "0"
		"textAlignment"  "center"
		"wrap"           "0"
		"bgcolor_override"			""
	}
}
