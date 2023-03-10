// Tab scoreboard survivor player
"Resource/UI/ScoreBoardSurvivor.res"
{

	IconForSlot_FirstAid
	{
		"fieldname"    "IconForSlot_FirstAid"
		"controlName"  "CIconPanel"
		"visible"      "0"
		"enabled"      "1"
		"xpos"         "142"
		"ypos"         "12"
		"zpos"         "2"
		"wide"         "12"
		"tall"         "12"
		"icon"         "icon_equip_medkit_small"
		"scaleImage"   "1"
	}

	IconForSlot_Grenade
	{
		"fieldname"    "IconForSlot_Grenade"
		"controlName"  "CIconPanel"
		"visible"      "0"
		"enabled"      "1"
		"xpos"         "128"
		"ypos"         "12"
		"zpos"         "2"
		"wide"         "12"
		"tall"         "12"
		"icon"         "icon_equip_pipebomb_small"
		"scaleImage"   "1"
	}

	IconForSlot_Pills
	{
		"fieldname"    "IconForSlot_Pills"
		"controlName"  "CIconPanel"
		"visible"      "0"
		"enabled"      "1"
		"xpos"         "156"
		"ypos"         "12"
		"zpos"         "2"
		"wide"         "12"
		"tall"         "12"
		"icon"         "icon_equip_pills_small"
		"scaleImage"   "1"
	}

	PingImage
	{
		"fieldname"      "PingImage"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "278"
		"ypos"           "4"
		"zpos"           "52"
		"wide"           "16"
		"tall"           "16"
		"autoResize"     "1"
		"font"           "GameUIButtons"
		"labelText"      ""
		"pinCorner"      "0"
		"tabPosition"    "0"
		"textAlignment"  "east"
	}

	PingLabel
	{
		"fieldname"      "PingLabel"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "296"
		"ypos"           "4"
		"zpos"           "2"
		"wide"           "32"
		"tall"           "16"
		"font"           "Cerbetica12"
		"labelText"      "0"
		"textAlignment"  "west"
	}

	PlayerBackground
	{
		"fieldname"         "PlayerBackground"
		"controlName"       "Panel"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "-2"
		"ypos"              "0"
		"zpos"              "0"
		"wide"              "320"
		"tall"              "24"
		"autoResize"        "1"
		"bgcolor_override"  "255 255 255 0"
		"border"            ""
		"pinCorner"         "0"
		"tabPosition"       "0"
	}

	PlayerBackground_Selected
	{
		"fieldname"         "PlayerBackground_Selected"
		"controlName"       "Panel"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "-2"
		"ypos"              "0"
		"zpos"              "0"
		"wide"              "320"
		"tall"              "24"
		"autoResize"        "1"
		"bgcolor_override"  "255 255 255 0"
		"border"            ""
		"pinCorner"         "0"
		"tabPosition"       "0"
	}

	SurvivorStatsAvatar
	{
		"fieldname"      "SurvivorStatsAvatar"
		"controlName"    "DontAutoCreate"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "28"
		"ypos"           "1"
		"zpos"           "50"
		"wide"           "28"
		"tall"           "14"
		"autoResize"     "3"
		"color_outline"  "0 0 0 0"
		"pinCorner"      "0"
		"tabPosition"    "0"
	}

	SurvivorStatsHead
	{
		"fieldname"    "SurvivorStatsHead"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "0"
		"ypos"         "0"
		"zpos"         "50"
		"wide"         "24"
		"tall"         "24"
		"scaleImage"   "1"
	}

	SurvivorStatsHealth
	{
		"fieldname"                     "SurvivorStatsHealth"
		"controlName"                   "HealthPanel"
		"visible"                       "1"
		"enabled"                       "1"
		"xpos"                          "28"
		"ypos"                          "17"
		"zpos"                          "51"
		"wide"                          "96"
		"tall"                          "7"
		"autoResize"                    "3"
		"healthbar_image_grey_ticks"    "vgui/hud/healthbar_ticks_withglow_white"
		"healthbar_image_high_ticks"    "vgui/hud/healthbar_ticks_withglow_green"
		"healthbar_image_low_ticks"     "vgui/hud/healthbar_ticks_withglow_red"
		"healthbar_image_medium_ticks"  "vgui/hud/healthbar_ticks_withglow_orange"
		"monochrome_color"              "Gray"
		"new_material_style"            "1"
		"pinCorner"                     "0"
		"tabPosition"                   "0"
	}

	SurvivorStatsHealthBG
	{
		"fieldname"         "SurvivorStatsHealthBG"
		"controlName"       "Panel"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "28"
		"ypos"              "17"
		"zpos"              "50"
		"wide"              "96"
		"tall"              "7"
		"autoResize"        "1"
		"bgcolor_override"  "ThinBarBgColour"
		"pinCorner"         "0"
		"tabPosition"       "0"
	}

	SurvivorStatsName
	{
		"fieldname"         "SurvivorStatsName"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "44"
		"ypos"              "2"
		"zpos"              "51"
		"wide"              "230"
		"tall"              "18"
		"autoResize"        "0"
		"brighttext"        "1"
		"dulltext"          "0"
		"font"              "Cerbetica12"
		"labelText"         ""
		"noshortcutsyntax"  "1"
		"pinCorner"         "0"
		"textAlignment"     "north-west"
	}

	SurvivorStatsNoAvatarName
	{
		"fieldname"         "SurvivorStatsNoAvatarName"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "28"
		"ypos"              "2"
		"zpos"              "51"
		"wide"              "230"
		"tall"              "18"
		"autoResize"        "0"
		"brighttext"        "1"
		"dulltext"          "0"
		"font"              "Cerbetica12"
		"labelText"         ""
		"noshortcutsyntax"  "1"
		"pinCorner"         "0"
		"textAlignment"     "north-west"
	}

	SurvivorStatsNoAvatarStatus
	{
		"fieldname"      "SurvivorStatsNoAvatarStatus"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "173"
		"ypos"           "10"
		"zpos"           "51"
		"wide"           "130"
		"tall"           "16"
		"autoResize"     "0"
		"brighttext"     "1"
		"dulltext"       "0"
		"font"           "Cerbetica12"
		"labelText"      ""
		"pinCorner"      "0"
		"textAlignment"  "west"
	}

	SurvivorStatsStatus
	{
		"fieldname"      "SurvivorStatsStatus"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "173"
		"ypos"           "10"
		"zpos"           "51"
		"wide"           "130"
		"tall"           "16"
		"autoResize"     "0"
		"brighttext"     "1"
		"dulltext"       "0"
		"font"           "Cerbetica12"
		"labelText"      ""
		"pinCorner"      "0"
		"textAlignment"  "west"
	}

	SurvivorSurvivalRecord
	{
		"fieldname"      "SurvivorSurvivalRecord"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "213"
		"ypos"           "10"
		"zpos"           "2"
		"wide"           "160"
		"tall"           "14"
		"font"           "Cerbetica12"
		"labelText"      "00:00.00"
		"textAlignment"  "west"
	}

	SurvivorSurvivalRecordImage
	{
		"fieldname"    "SurvivorSurvivalRecordImage"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "194"
		"ypos"         "7"
		"zpos"         "2"
		"wide"         "18"
		"tall"         "18"
		"icon"         "icon_gold_medal_small"
		"scaleImage"   "1"
	}

	Voice
	{
		"fieldname"    "Voice"
		"controlName"  "Panel"
		"visible"      "0"
		"enabled"      "1"
		"xpos"         "-2"
		"ypos"         "-24"
		"wide"         "0"
		"tall"         "0"
	}
}
