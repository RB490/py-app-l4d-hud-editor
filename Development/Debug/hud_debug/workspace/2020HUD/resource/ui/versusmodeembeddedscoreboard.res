"Resource/UI/VersusModeEmbeddedScoreboard.res"
{
	
	"CompletionAmountLabel"	// current map score
	{
		"ControlName"	"Label"
		"fieldName"		"CompletionAmountLabel"
		"xpos"			"45"
		"ypos"			"3"
		"wide"			"60"
		"tall"			"11"
		"zpos"			"50"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%completion%"
		"textAlignment"	"center"
		"dulltext"		"1"
		"brighttext"	"0"
		
		"font"		"Cerbetica10"
		"fgcolor_override"	"White"
	
		"bgcolor_override"  "0 0 0 115"
		"border"            "blackborder"
	}
	
	"TeamYourScoreSurvivors"
	{
		"ControlName"		"Label"
		"fieldName"		"TeamYourScoreSurvivors"
		"xpos"			"150"
		"ypos"			"3"
		"wide"			"60"
		"tall"			"11"
		"zpos"		"50"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%YourSurvivor%"
		"textAlignment"		"center"
		"dulltext"		"1"
		"brighttext"		"0"
		
		"font"		"Cerbetica10"
		"fgcolor_override"	"White"
	
		"bgcolor_override"  "0 115 0 115"
		"border"            "blackborder"
	}

	"TeamEnemyScoreSurvivors"
	{
		"ControlName"		"Label"
		"fieldName"		"TeamEnemyScoreSurvivors"
		"xpos"			"255"
		"ypos"			"3"
		"wide"			"60"
		"tall"			"11"
		"zpos"		"50"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"%EnemySurvivor%"
		"textAlignment"		"center"
		"dulltext"		"1"
		"brighttext"		"0"
		
		"font"		"Cerbetica10"
		"fgcolor_override"	"White"
	
		"bgcolor_override"  "115 0 0 115"
		"border"            "blackborder"
	}
	
	BGPanel
	{
		"fieldname"         "BGPanel"
		"controlName"       "Panel"
		"visible"           "1"
		"enabled"           "1"
		"xpos"		"0"
		"ypos"		"0"
		"wide"		"320"	
		"tall"		"40"
		"zpos"              "0"
		"bgcolor_override"  "TransparentBlack"
		"border"            "BlackBorder"
	}
	
	"TeamImage"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TeamImage"
		"xpos"				"0"
		"ypos"				"0"
		"wide"				"40"
		"tall"				"40"
		"scaleImage"		"1"
		"visible"			"1"
		"enabled"			"1"
		"image"				"select_survivors"
		"drawColor"			"180 180 180 255"
		"zpos"				"0"
	}
	
	"CompletionProgressBar"
	{
		"ControlName"	"CVersusModeLevelProgressBar"
		"fieldName"		"CompletionProgressBar"
		"xpos"			"35"
		"ypos"			"7"
		"wide"			"400"
		"tall"			"60"
		"zpos"			"1"
		"visible"		"1"
		"enabled"		"1"	
		
		"bar_x"			"10"
		"bar_y"			"10"
		"bar_w"			"271"
		"bar_h"			"3"
		"bar_gap"		"3"
		
		"skull_size"	"10"
		"skull_y"		"-4"
		
		"bar_color"					"VersusBrown"
		"bar_localplayer_color"		"VersusSelected"
		"bar_bgcolor"				"ThinBarBgColour"
	}
	
	
	
	
	
	
	//////////////////////////////////////////////////////////////
	
	
	
	// progress background box
	"BackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"BackgroundImage"
		"xpos"		"3"
		"ypos"		"70"
		"wide"		"305"	
		"tall"		"68"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack50_outlineGrey"
		"drawcolor"		"0 0 0 255"
		"zpos"			"-1"
		
		"src_corner_height"		"16"				// pixels inside the image
		"src_corner_width"		"16"
			
		"draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"3"	
	}
	
	"EnemyTeamBackground"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"EnemyTeamBackground"
		"xpos"		"158"
		"ypos"		"25"
		"wide"		"150"
		"tall"		"45"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack"
		"zpos"			"-2"
		
		"src_corner_height"		"16"				// pixels inside the image
		"src_corner_width"		"16"
			
		"draw_corner_width"		"8"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"8"	
	}
	
	"YourTeamBackground"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"YourTeamBackground"
		"xpos"		"3"
		"ypos"		"25"
		"wide"		"150"
		"tall"		"45"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack"
		"zpos"			"-2"
		
		"src_corner_height"		"16"				// pixels inside the image
		"src_corner_width"		"16"
			
		"draw_corner_width"		"8"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"8"	
	}
	
	"TotalScoreEnemyTeam"	// "Total Score:"
	{
		"ControlName"		"Label"
		"fieldName"		"TotalScoreEnemyTeam"
		"xpos"		"169"
		"ypos"		"45"
		"wide"		"125"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"#L4D_vs_TotalScore_Embedded"
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
		"font"		"InstructorTitle_ss"
		"fgcolor_override"	"White"
	}

	"TotalScoreYourTeam"	//"Total Score:"
	{
		"ControlName"		"Label"
		"fieldName"		"TotalScoreYourTeam"
		"xpos"		"16"
		"ypos"		"45"
		"wide"		"125"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"#L4D_vs_TotalScore_Embedded"
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
		"font"		"InstructorTitle_ss"
		"fgcolor_override"	"White"
	}
	
	"CompletionLabel"		//map name
	{
		"ControlName"	"Label"
		"fieldName"		"CompletionLabel"
		"xpos"			"65"
		"ypos"			"72"
		"wide"			"320"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"#L4D_VSScoreboard_Completion"
		"textAlignment"	"south-west"
		"dulltext"		"1"
		"brighttext"	"0"
		"fgcolor_override"	"White"
		"font"				"BodyText_medium"
		"auto_wide_tocontents"	"1"
	}

	"TeamYours"
	{
		"ControlName"		"Label"
		"fieldName"		"TeamYours"
		"xpos"		"16"	[$WIN32]
		"ypos"		"30"	[$WIN32]
		"wide"		"125"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"#L4D_VSScoreboard_YourTeam"
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
		"font"		"InstructorTitle_ss"
		"fgcolor_override"	"White"
	}	
	
	
	"TeamEnemy"
	{
		"ControlName"		"Label"
		"fieldName"		"TeamEnemy"
		"xpos"		"169"			[$WIN32]
		"ypos"		"30"			[$WIN32]
		"wide"		"125"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"#L4D_VSScoreboard_EnemyTeam"
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
		"font"		"InstructorTitle_ss"
		"fgcolor_override"	"White"
	}
}
