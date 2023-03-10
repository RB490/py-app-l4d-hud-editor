// Versus scoreboard end of match
"Resource/UI/VersusModeResults.res"
{

	"BackgroundFill"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"BackgroundFill"
		"xpos"			"0"
		"ypos"			"0"
		"wide"          "364"
		"tall"          "115"
		"visible"			"1"
		"enabled"			"1"
		"zpos"				"-2"
		"fillcolor" 		"0 0 0 200"
		"border"			"BlackBorderMedium"
	}

	ModeTitle
	{
		"fieldname"         "ModeTitle"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "13"
		"ypos"              "11"
		"wide"              "344"
		"tall"              "24"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "0"
		"fgcolor_override"  "White"
		"font"              "Cerbetica18Shadow"
		"labelText"         "#L4D_VSScoreboard_Title"
		"pinCorner"         "0"
		"textAlignment"     "north-west"
	}

	TeamEnemy
	{
		"fieldname"         "TeamEnemy"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "207"
		"ypos"              "30"
		"wide"              "132"
		"tall"              "20"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "1"
		"fgcolor_override"  "White"
		"font"              "Cerbetica12Shadow"
		"labelText"         "#L4D_VSScoreboard_EnemyTeam"
		"pinCorner"         "0"
		"textAlignment"     "center"
	}

	TeamEnemyScoreSurvivors
	{
		"fieldname"         "TeamEnemyScoreSurvivors"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "207"
		"ypos"              "50"
		"wide"              "132"
		"tall"              "20"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "1"
		"fgcolor_override"  "MediumGray"
		"font"              "Cerbetica12Shadow"
		"labelText"         "%EnemySurvivor%"
		"pinCorner"         "0"
		"textAlignment"     "center"
		"border"			"RedborderThick"
		"bgcolor_override"	"TransparentMediumBlack"
	}

	TeamWinLabel
	{
		"fieldname"         "TeamWinLabel"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "15"
		"ypos"              "76"
		"wide"              "334"
		"tall"              "30"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "1"
		"fgcolor_override"  "MediumGray"
		"font"              "Cerbetica12Shadow"
		"labelText"         "#L4D_VSScoreboard_Distance"
		"pinCorner"         "0"
		"textAlignment"     "center"
		"border"			"RedborderThick"
		"bgcolor_override"	"TransparentMediumBlack"
	}

	TeamYours
	{
		"fieldname"         "TeamYours"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "25"
		"ypos"              "30"
		"wide"              "132"
		"tall"              "20"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "1"
		"fgcolor_override"  "White"
		"font"              "Cerbetica12Shadow"
		"labelText"         "#L4D_VSScoreboard_YourTeam"
		"pinCorner"         "0"
		"textAlignment"     "center"
	}

	TeamYourScoreSurvivors
	{
		"fieldname"         "TeamYourScoreSurvivors"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "25"
		"ypos"              "50"
		"wide"              "132"
		"tall"              "20"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "1"
		"fgcolor_override"  "MediumGray"
		"font"              "Cerbetica12Shadow"
		"labelText"         "%YourSurvivor%"
		"pinCorner"         "0"
		"textAlignment"     "Center"
		"border"			"RedborderThick"
		"bgcolor_override"	"TransparentMediumBlack"
	}


	
	
	
	
	
	
	
	
	//////////////////////////////////////////////////////////
	
	
	
	StatBreakdownHighlightImage
	{
		"fieldname"           "StatBreakdownHighlightImage"
		"controlName"         "ScalableImagePanel"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "0"
		"ypos"                "7099"
		"zpos"                "-1"
		"wide"                "364"
		"tall"                "45"
		"draw_corner_height"  "8"
		"draw_corner_width"   "8"
		"image"               "../vgui/hud/ScalablePanel_bgBlack_outlineRed"
		"scaleImage"          "1"
		"src_corner_height"   "16"
		"src_corner_width"    "16"
	}
	
	YourTeamHighlightImage
	{
		"fieldname"           "YourTeamHighlightImage"
		"controlName"         "ScalableImagePanel"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "25"
		"ypos"                "4399"
		"zpos"                "-1"
		"wide"                "132"
		"tall"                "32"
		"draw_corner_height"  "8"
		"draw_corner_width"   "8"
		"image"               "../vgui/hud/ScalablePanel_bgBlack_outlineRed"
		"scaleImage"          "1"
		"src_corner_height"   "16"
		"src_corner_width"    "16"
	}
	
	"EnemyTeamHighlightImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"EnemyTeamHighlightImage"
		"xpos"                "20799"
		"ypos"                "43"
		"wide"                "132"
		"tall"                "32"
		"visible"		"0"
		"enabled"		"0"
		"scaleImage"	"1"	
		"image"               "../vgui/hud/ScalablePanel_bgBlack_outlineRed"
		//"drawcolor"		"0 0 0 255"
		"src_corner_height"		"16"			// pixels inside the image
		"src_corner_width"		"16"
		"draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"3"	
	}
	
	TeamFlipExplanationLabel
	{
		"fieldname"         "TeamFlipExplanationLabel"
		"controlName"       "Label"
		"visible"           "0"
		"enabled"           "1"
		"xpos"              "15"
		"ypos"              "76"
		"wide"              "334"
		"tall"              "30"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "1"
		"fgcolor_override"  "MediumGray"
		"font"              "Cerbetica12Shadow"
		"labelText"         "You will play Survivors first in the next chapter."
		"pinCorner"         "0"
		"textAlignment"     "center"
		"border"			"RedborderThick"
		"bgcolor_override"	"TransparentMediumBlack"
	}
	
	"BackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"BackgroundImage"
		"xpos"			"999"
		"ypos"			"0"
		"wide"          "364"
		"tall"          "115"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack50_outlineGrey"
		"drawcolor"		"0 0 0 255"
		"src_corner_height"		"16"			// pixels inside the image
		"src_corner_width"		"16"
		"draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"3"	
		"bgcolor_override" 		"255 255 255 255"
	}
}
