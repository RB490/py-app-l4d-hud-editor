
"Resource/UI/HUD/ProgressBar.res"
{
	"BackgroundImage"
	{
		"ControlName"	"Panel"
		"fieldName"		"BackgroundImage"
		"xpos"			"38"
		"ypos"			"15"
		"wide"			"150"
		"tall"			"5"
		"zpos"			"-1"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"hud/progressbar_bg"
		"drawColor"	"80 76 82 255"
		"bgcolor_override"	"0 0 0 220"
	}
	"BarLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"BarLabel"
		"xpos"			"38"
		"ypos"			"0"
		"wide"			"150"
		"tall"			"20" [$OSX]
		"tall"			"12" [$WINDOWS]
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"ink_shadow_12"
		"fgcolor_override" "White"
	}
	"Bar"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"Bar"
		"xpos"			"38"
		"ypos"			"15"
		"wide"			"150"
		"tall"			"6"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"vgui/hud/healthbar_withglow_white"
	}
	"AwardIcon"
	{
		"ControlName"	"CIconPanel"
		"fieldName"		"AwardIcon"
		"xpos"			"9"
		"ypos"			"10"
		"wide"			"25"
		"tall"			"24"
		"visible"		"0"
		"enabled"		"0"
		"scaleImage"	"1"
		"icon"			"icon_healing"
	}
	"Subtext"
	{
		"ControlName"	"Label"
		"fieldName"		"Subtext"
		"xpos"			"38"
		"ypos"			"22"
		"wide"			"150"
		"tall"			"12"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"ink_shadow_12"
		"fgcolor_override" "255 255 255 100"
	}
}