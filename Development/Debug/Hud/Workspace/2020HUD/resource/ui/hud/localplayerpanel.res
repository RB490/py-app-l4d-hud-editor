// Local player health hud
"Resource/UI/HUD/LocalPlayerPanel.res"
{

	Dead
	{
		"fieldname"    "Dead"
		"controlName"  "ImagePanel"
		"visible"      "0"
		"enabled"      "0"
		"xpos"         "0"
		"ypos"         "1899"
		"zpos"         "3"
		"wide"         "256"
		"tall"         "128"
		"image"        "hud/overlay_dead"
		"scaleImage"   "1"
	}

	Head
	{
		"fieldname"    "Head"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "9999"
		"ypos"         "0"
		"zpos"			"-3"
		"wide"         "20"
		"tall"         "20"
		"scaleImage"   "1"
	}

	Health
	{
		"fieldname"                     "Health"
		"controlName"                   "HealthPanel"
		"visible"                       "1"
		"enabled"                       "1"
		"xpos"           				"r89"
		"ypos"           				"r25"
		"zpos"                          "1"
		"wide"                          "49"
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
		
		"bgcolor_override"	"ThinBarBgColour"
	}
	
	HealthNumber
	{
		"fieldname"      "HealthNumber"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "r115"
		"ypos"           "r99"
		"zpos"           "2"
		"wide"           "75"
		"tall"           "100"
		"font"           "Cerbetica50Shadow"
		"labelText"      "%HealthNumber%"
		"textAlignment"  "east"
		//"border"		"4Colours"
		//"bgcolor_override" "TransparentBlack"
		//"bgcolor_override" "Black"
	}
	
	HealthNumberFakey
	{
		"fieldname"      "HealthNumberFakey"
		"controlName"    "Label"
		"visible"        "0"
		"enabled"        "0"
		"xpos"           "r172"
		"ypos"           "r127"
		"zpos"           "2"
		"wide"           "75"
		"tall"           "100"
		"font"           "Cerbetica50"
		"labelText"      "%HealthNumber%"
		"textAlignment"  "center"
		"fgcolor_override"	"125 125 125 125"
		//"border"		"BaseBorder"
		//"bgcolor_override" "TransparentBlack"
		//"bgcolor_override" "Black"
		//"border"		"baseborder"
	}

	IconForSlot_First_Aid
	{
		"fieldname"    "IconForSlot_First_Aid"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"           "c15099"
		"ypos"           "c130"
		"zpos"         "2"
		"wide"         "12"
		"tall"         "12"
		"icon"         "icon_equip_medkit_small"
		"scaleImage"   "1"
	}

	IconForSlot_Pills
	{
		"fieldname"    "IconForSlot_Pills"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"           "c17099"
		"ypos"           "c130"
		"zpos"         "2"
		"wide"         "12"
		"tall"         "12"
		"icon"         "icon_equip_pills_small"
		"scaleImage"   "1"
	}

	IconForSlot_Grenade
	{
		"fieldname"    "IconForSlot_Grenade"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"           "c19099"
		"ypos"           "c130"
		"zpos"         "2"
		"wide"         "12"
		"tall"         "12"
		"icon"         "icon_equip_pipebomb_small"
		"scaleImage"   "1"
	}

	Name
	{
		"fieldname"         "Name"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "2"
		"ypos"              "2399"
		"zpos"              "3"
		"wide"              "93"
		"tall"              "11"
		"fgcolor_override"  "0 0 0 255"
		//"bgcolor_override"  "0 0 0 255"
		"font"              "Cerbetica11"
		"labelText"         "asdffffefefe"
		"textAlignment"     "west"
	}

	Voice
	{
		"fieldname"    "Voice"
		"controlName"  "TeamDisplayVoicePanel"
		"visible"      "0"
		"enabled"      "1"
		"xpos"         "100"
		"ypos"         "0"
		"zpos"         "3"
		"wide"         "16"
		"tall"         "16"
		"voice_icon"   "voice_player"
	}
}
