"Resource/UI/HUD/TeammatePanel.res"
{

	Dead
	{
		"fieldname"    "Dead"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "7899"
		"ypos"         "3"
		"zpos"			"-15"
		"wide"         "15"
		"tall"         "15"
		"scaleImage"   "1"
		"image"        "hud/overlay_dead"
		"scaleImage"   "1"
	}

	Head
	{
		"fieldname"    "Head"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "0"
		"ypos"         "0"
		"zpos"			"-3"
		"wide"         "15"
		"tall"         "15"
		"scaleImage"   "1"
	}

	Health
	{
		"fieldname"                     "Health"
		"controlName"                   "HealthPanel"
		"visible"                       "1"
		"enabled"                       "1"
		"xpos"                          "0"
		"ypos"                          "18"
		"zpos"                          "1"
		"wide"                          "100"
		"tall"                          "3"
		//"healthbar_image_high"		"vgui/hud/healthbar_withglow_green"
		//"healthbar_image_medium"		"vgui/hud/healthbar_withglow_orange"
		//"healthbar_image_low"			"vgui/hud/healthbar_withglow_red"
		//"healthbar_image_grey"		"vgui/hud/healthbar_withglow_white"
		
		"healthbar_image_high_ticks"	"vgui/hud/healthbar_ticks_withglow_green"
		"healthbar_image_medium_ticks"	"vgui/hud/healthbar_ticks_withglow_orange"
		"healthbar_image_low_ticks"		"vgui/hud/healthbar_ticks_withglow_red"
		"healthbar_image_grey_ticks"	"vgui/hud/healthbar_ticks_withglow_white"
		"new_material_style"            "1"
		"textAlignment"                 "east"
	}
	
	"HealthBGPanel"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"HealthBGPanel"
		"visible"                       "1"
		"enabled"                       "1"
		"xpos"                          "0"
		"ypos"                          "18"
		"zpos"                          "-10"
		"wide"                          "100"
		"tall"                          "3"
		"proportionaltoparent"	"1"
		//"border"		"CyanBorder"
		"bgcolor_override"	"ThinBarBgColour"
	}
	
	HealthNumber
	{
		"fieldname"      "HealthNumber"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "72"
		"ypos"           "0"
		"zpos"           "2"
		"wide"           "28"
		"tall"           "15"
		"font"           "Cerbetica18Shadow"
		"labelText"      "%HealthNumber%"
		"textAlignment"  "east"
		//"border"		"BaseBorder"
		//"bgcolor_override" "TransparentBlack"
		//"bgcolor_override" "Black"
	}

	IconForSlot_First_Aid
	{
		"fieldname"    "IconForSlot_First_Aid"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "23"
		"ypos"         "0"
		"zpos"         "2"
		"wide"         "15"
		"tall"         "15"
		"icon"         "icon_equip_medkit_small"
		"scaleImage"   "1"
		//"bgcolor_override"	"Black"
	}

	IconForSlot_Pills
	{
		"fieldname"    "IconForSlot_Pills"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "40"
		"ypos"         "0"
		"zpos"         "2"
		"wide"         "15"
		"tall"         "15"
		"icon"         "icon_equip_pills_small"
		"scaleImage"   "1"
		//"bgcolor_override"	"Black"
	}

	IconForSlot_Grenade
	{
		"fieldname"    "IconForSlot_Grenade"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "57"
		"ypos"         "0"
		"zpos"         "2"
		"wide"         "15"
		"tall"         "15"
		"icon"         "icon_equip_pipebomb_small"
		"scaleImage"   "1"
		//"bgcolor_override"	"Black"
	}

	Name
	{
		"fieldname"         "Name"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "0"
		"ypos"              "22"
		"zpos"              "3"
		"wide"              "250"
		"tall"              "11"
		"fgcolor_override"  "0 255 0 255"
		//"bgcolor_override"  "0 0 0 255"
		"font"              "Cerbetica10Shadow"
		"labelText"         "asdffffefefe"
		"textAlignment"     "west"
		//"border"			"baseborder"
	}

	Status
	{
		"fieldname"         "Status"
		"controlName"       "Label"
		"visible"           "0"		//Set to 0
		"enabled"           "1"
		"xpos"              "15"
		"ypos"              "9"
		"zpos"              "30"
		"wide"              "15"
		"tall"              "6"
		"fgcolor_override"  "White"
		"bgcolor_override"  "0 0 0 245"
		"font"              "Fira Code5"
		"labelText"         ""	//DOWN / IDLE
		"textAlignment"     "Center"
		//"border"			"baseborder"
	}

	Voice
	{
		"fieldname"    "Voice"
		"controlName"  "TeamDisplayVoicePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "8"
		"ypos"         "-5"
		"zpos"         "3"
		"wide"         "16"
		"tall"         "16"
		"voice_icon"   "voice_player"
	}
}
