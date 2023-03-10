"Resource/UI/HUD/ProgressBar.res"
{
	"BackgroundImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"BackgroundImage"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"272"
		"tall"			"68"
		"zpos"			"-1"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"hud/progressbar_bg"
		"drawColor"	"80 76 82 255"
	}
	
	"BarLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"BarLabel"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"200"
		"tall"			"15"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"Center"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"Cerbetica10Shadow"
		"fgcolor_override" ""
		//"border"		"baseborder"
	}
	
	"Bar"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"Bar"
		"xpos"			"50"
		"ypos"			"15"
		"wide"          "100"
		"tall"          "3"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"vgui/hud/healthbar_ticks_withglow_whiteSolid"
	}
	
	"BarBG"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"BarBG"
		"visible"		"1"
		"xpos"			"50"
		"ypos"			"15"
		"tall"                          "3"
		"wide"                          "100"
		"proportionaltoparent"	"1"
		//"border"		"CyanBorder"
		"bgcolor_override"	"ThinBarBgColour"
	}

	"Subtext"
	{
		"ControlName"	"Label"
		"fieldName"		"Subtext"
		"xpos"			"0"
		"ypos"			"17"
		"wide"			"200"
		"tall"			"15"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"Center"
		"font"			"Cerbetica10Shadow"
		"fgcolor_override" ""	
		//"border"		"baseborder"
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
		"enabled"		"1"
		"scaleImage"	"1"
		"icon"			"icon_healing"
	}
}