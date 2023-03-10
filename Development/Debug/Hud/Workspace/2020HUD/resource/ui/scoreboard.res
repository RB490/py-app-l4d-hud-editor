"Resource/UI/ScoreBoard.res"
{

	BGPanel
	{
		"fieldname"         "BGPanel"
		"controlName"       "Panel"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "20"
		"ypos"              "20"
		"zpos"              "0"
		"wide"              "330"
		"tall"              "195"
		"bgcolor_override"  "TransparentBlack"
		"border"            "BlackBorder"
	}

	CScavengeModeEmbeddedScoreboard
	{
		"fieldname"     "ScavengeModeScoreboard"
		"controlName"   "CScavengeModeEmbeddedScoreboard"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "50"
		"wide"          "354"
		"tall"          "140"
		"usetitlesafe"  "1"
	}

	CVersusModeEmbeddedScoreboard
	{
		"fieldname"     "VersusModeScoreboard"
		"controlName"   "CVersusModeEmbeddedScoreboard"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "50"	//300
		"wide"          "354"
		"tall"          "140"
		"usetitlesafe"  "1"
	}

	CurrentMap
	{
		"fieldname"            "CurrentMap"
		"controlName"          "Label"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "378"
		"ypos"                 "11109"
		"wide"                 "90"
		"tall"                 "12"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"brighttext"           "1"
		"centerwrap"           "1"
		"dulltext"             "0"
		"font"                 "Cerbetica12"
		"labelText"            "#L4D_Scoreboard_Current_Map"
		"pinCorner"            "0"
		"tabPosition"          "0"
		"textAlignment"        "center"
	}

	CurrentMapArrow
	{
		"fieldname"            "CurrentMapArrow"
		"controlName"          "Label"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "0"
		"ypos"                 "78"
		"zpos"                 "2"
		"wide"                 "60"
		"tall"                 "14"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"brighttext"           "1"
		"dulltext"             "0"
		"font"                 "GameUIButtons"
		"labelText"            "r"
		"pinCorner"            "0"
		"tabPosition"          "0"
		"textAlignment"        "center"
		"fgcolor_override"		"255 255 255 255"
	}
	
	ImgBronzeMedal
	{
		"fieldname"    "ImgBronzeMedal"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "130"
		"ypos"         "60"
		"zpos"         "2"
		"wide"         "20"
		"tall"         "20"
		"image"        "hud/survival_medal_bronze"
		"pinCorner"    "0"
		"scaleImage"   "1"
		"tabPosition"  "0"
	}

	LblBronzeMedalTime
	{
		"fieldname"      "LblBronzeMedalTime"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "150"
		"ypos"           "60"
		"zpos"           "2"
		"wide"           "50"
		"tall"           "20"
		"autoResize"     "0"
		"Font"           "Cerbetica10"
		"labelText"      "0:00"
		"pinCorner"      "0"
		"tabPosition"    "0"
		"textAlignment"  "west"
	}
	
	ImgSilverMedal
	{
		"fieldname"    "ImgSilverMedal"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "190"
		"ypos"         "60"
		"zpos"         "2"
		"wide"         "20"
		"tall"         "20"
		"image"        "hud/survival_medal_silver"
		"pinCorner"    "0"
		"scaleImage"   "1"
		"tabPosition"  "0"
	}

	LblSilverMedalTime
	{
		"fieldname"      "LblSilverMedalTime"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "210"
		"ypos"           "60"
		"zpos"           "2"
		"wide"           "50"
		"tall"           "20"
		"autoResize"     "0"
		"Font"           "Cerbetica10"
		"labelText"      "0:00"
		"pinCorner"      "0"
		"tabPosition"    "0"
		"textAlignment"  "west"
	}
	
	ImgGoldMedal
	{
		"fieldname"    "ImgGoldMedal"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "250"
		"ypos"         "60"
		"zpos"         "2"
		"wide"         "20"
		"tall"         "20"
		"image"        "hud/survival_medal_gold"
		"pinCorner"    "0"
		"scaleImage"   "1"
		"tabPosition"  "0"
	}
	
	LblGoldMedalTime
	{
		"fieldname"      "LblGoldMedalTime"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "270"
		"ypos"           "60"
		"zpos"           "2"
		"wide"           "50"
		"tall"           "20"
		"autoResize"     "0"
		"Font"           "Cerbetica10"
		"labelText"      "0:00"
		"pinCorner"      "0"
		"tabPosition"    "0"
		"textAlignment"  "west"
	}

	ImgLevelLargeImage
	{
		"fieldname"    "ImgLevelLargeImage"
		"controlName"  "ImagePanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "25"
		"ypos"         "50"
		"wide"         "80"
		"tall"         "40"
		"image"        "maps/any"
		"pinCorner"    "0"
		"scaleImage"   "1"
		"tabPosition"  "0"
	}

	Infected1
	{
		"fieldname"     "Infected1"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "205"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "50"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
	}

	Infected2
	{
		"fieldname"     "Infected2"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "205"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "50"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
	}

	Infected3
	{
		"fieldname"     "Infected3"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "205"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "50"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
	}

	Infected4
	{
		"fieldname"     "Infected4"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "205"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "50"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
	}

	Infected5
	{
		"fieldname"     "Infected5"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "205"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "50"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
	}

	InfectedBackground
	{
		"fieldname"           "InfectedBackground"
		"controlName"         "ScalableImagePanel"
		"visible"             "0"
		"enabled"             "1"
		"xpos"                "25"
		"ypos"                "30099"
		"zpos"                "-2"
		"wide"                "311"
		"tall"                "90"
		"usetitlesafe"        "1"
		"draw_corner_height"  "8"
		"draw_corner_width"   "8"
		"image"               "../vgui/hud/ScalablePanel_bgBlack"
		"scaleImage"          "1"
		"src_corner_height"   "16"
		"src_corner_width"    "16"
	}

	Map1
	{
		"fieldname"            "Map1"
		"controlName"          "ImagePanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "25"
		"ypos"                 "55"
		"wide"                 "60"
		"tall"                 "30"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"fillcolor_override"   "DarkGray"
		"pinCorner"            "0"
		"tabPosition"          "0"
	}

	Map2
	{
		"fieldname"            "Map2"
		"controlName"          "ImagePanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "90"
		"ypos"                 "55"
		"wide"                 "60"
		"tall"                 "30"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"fillcolor_override"   "DarkGray"
		"pinCorner"            "0"
		"tabPosition"          "0"
	}

	Map3
	{
		"fieldname"            "Map3"
		"controlName"          "ImagePanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "155"
		"ypos"                 "55"
		"wide"                 "60"
		"tall"                 "30"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"fillcolor_override"   "DarkGray"
		"pinCorner"            "0"
		"tabPosition"          "0"
	}

	Map4
	{
		"fieldname"            "Map4"
		"controlName"          "ImagePanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "220"
		"ypos"                 "55"
		"wide"                 "60"
		"tall"                 "30"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"fillcolor_override"   "DarkGray"
		"pinCorner"            "0"
		"tabPosition"          "0"
	}

	Map5
	{
		"fieldname"            "Map5"
		"controlName"          "ImagePanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "285"
		"ypos"                 "55"
		"wide"                 "60"
		"tall"                 "30"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"fillcolor_override"   "DarkGray"
		"pinCorner"            "0"
		"tabPosition"          "0"
	}

	MissionObjective
	{
		"fieldname"         "MissionObjective"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "70"
		"ypos"              "53"
		"wide"              "330"
		"tall"              "24"
		"usetitlesafe"      "1"
		"autoResize"        "0"
		"brighttext"        "1"
		"dulltext"          "0"
		"fgcolor_override"  "MediumGray"
		"font"              "Default"
		"labelText"         ""
		"pinCorner"         "0"
		"textAlignment"     "north-west"
		"wrap"              "1"
	}

	MissionTitle
	{
		"fieldname"         "MissionTitle"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "20"
		"ypos"              "25"
		"wide"              "330"
		"tall"              "20"
		"autoResize"        "0"
		//"bgcolor_override"  "TransparentBlack"
		"brighttext"        "1"
		"dulltext"          "0"
		//"fgcolor_override"  "White"
		"font"              "Cerbetica18"
		"labelText"         ""
		"pinCorner"         "0"
		"textAlignment"     "Center"
		"wrap"              "0"
		//"border"			"baseborder"
	}

	OpponentMap
	{
		"fieldname"            "OpponentMap"
		"controlName"          "Label"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "378"
		"ypos"                 "60"
		"wide"                 "60"
		"tall"                 "0"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"brighttext"           "1"
		"centerwrap"           "1"
		"dulltext"             "0"
		"font"                 "Cerbetica12"
		"labelText"            "#L4D_Scoreboard_Opponent_Map"
		"pinCorner"            "0"
		"tabPosition"          "0"
		"textAlignment"        "center"
	}

	RescueMap
	{
		"fieldname"            "RescueMap"
		"controlName"          "Label"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "378"
		"ypos"                 "11398"
		"wide"                 "80"
		"tall"                 "14"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"brighttext"           "1"
		"dulltext"             "0"
		"font"                 "Cerbetica12"
		"labelText"            "#L4D_Scoreboard_Rescue_Map"
		"pinCorner"            "0"
		"tabPosition"          "0"
		"textAlignment"        "center"
	}

	RescueMapArrow
	{
		"fieldname"            "RescueMapArrow"
		"controlName"          "Label"
		"visible"              "0"
		"enabled"              "0"
		"xpos"                 "378"
		"ypos"                 "10409"
		"wide"                 "60"
		"tall"                 "12"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"brighttext"           "1"
		"dulltext"             "0"
		"fgcolor_override"     "White"
		"font"                 "GameUIButtons"
		"labelText"            "r"
		"pinCorner"            "0"
		"tabPosition"          "0"
		"textAlignment"        "center"
	}

	scores
	{
		"fieldname"              "scores"
		"controlName"            "CClientScoreBoardDialog"
		"visible"                "0"
		"enabled"                "1"
		"xpos"                   "10"
		"ypos"                   "52"
		"wide"                   "f0"
		"tall"                   "480"
		"autoResize"             "0"
		"infected_avatar_size"   "24"
		"infected_death_width"   "30"
		"infected_name_width"    "110"
		"infected_ping_width"    "30"
		"infected_score_width"   "30"
		"infected_status_width"  "30"
		"pinCorner"              "0"
		"scoreboard_position"    "north-west"
		"tabPosition"            "0"
	}

	ServerName
	{
		"fieldname"         "ServerName"
		"controlName"       "Label"
		"visible"           "0"
		"enabled"           "1"
		"xpos"              "30"
		"ypos"              "20"
		"wide"              "330"
		"tall"              "24"
		"autoResize"        "0"
		"brighttext"        "1"
		"dulltext"          "0"
		"fgcolor_override"  "White"
		"font"              "FrameTitle"
		"labelText"         ""
		"pinCorner"         "0"
		"textAlignment"     "north-west"
	}

	Spectators
	{
		"fieldname"         "Spectators"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "20"
		"ypos"              "0"
		"zpos"              "1"
		"wide"              "f0"
		"tall"              "20"
		"usetitlesafe"      "1"
		"autoResize"        "0"
		"font"              "Cerbetica10Shadow"
		"labelText"         "%spectators%"
		"noshortcutsyntax"  "1"
		"pinCorner"         "0"
		"textAlignment"     "west"
		"bgcolor_override"	"blank"
		"border"			"blank"
	}

	Survivor1
	{
		"fieldname"     "Survivor1"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "98"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "24"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
		"bgcolor_override"	"0 0 0 90"
		"border"		"blackborder"
	}

	Survivor2
	{
		"fieldname"     "Survivor2"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "127"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "24"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
		"bgcolor_override"	"0 0 0 90"
		"border"		"blackborder"
	}

	Survivor3
	{
		"fieldname"     "Survivor3"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "156"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "24"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
		"bgcolor_override"	"0 0 0 90"
		"border"		"blackborder"
	}

	Survivor4
	{
		"fieldname"     "Survivor4"
		"controlName"   "DontAutoCreate"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "25"
		"ypos"          "185"
		"zpos"          "1"
		"wide"          "320"
		"tall"          "24"
		"usetitlesafe"  "1"
		"autoResize"    "0"
		"pinCorner"     "0"
		"tabPosition"   "0"
		"bgcolor_override"	"0 0 0 90"
		"border"		"blackborder"
	}

	SurvivorBackground
	{
		"fieldname"         "SurvivorBackground"
		"controlName"       "Panel"
		"visible"           "0"
		"enabled"           "1"
		"xpos"              "20"
		"ypos"              "c-75"
		"zpos"              "-2"
		"wide"              "322"
		"tall"              "129"
		"usetitlesafe"      "1"
		"bgcolor_override"  "TransparentLightBlack"
		//"border"            "BlackBorder"
	}

	ThirdPartyServerPanel
	{
		"fieldname"    "ThirdPartyServerPanel"
		"controlName"  "CThirdPartyServerPanel"
		"visible"      "0"
		"enabled"      "0"
		"xpos"         "10"
		"ypos"         "25"
		"wide"         "300"
		"tall"         "130"
	}
}
