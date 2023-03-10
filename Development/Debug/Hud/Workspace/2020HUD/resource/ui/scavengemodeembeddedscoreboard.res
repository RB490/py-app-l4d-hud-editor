"Resource/UI/ScavengeModeEmbeddedScoreboard.res"
{

	BGPanel
	{
		"fieldname"         "BGPanel"
		"controlName"       "Panel"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "0"
		"ypos"              "0"
		"zpos"              "0"
		"wide"              "320"
		"tall"              "41"
		"bgcolor_override"  "TransparentLightBlack"
		"border"            "BlackBorder"
	}

	"RoundLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"RoundLabel"
		"xpos"		"120"
		"ypos"		"0"
		"wide"		"100"
		"tall"		"40"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_Scavenge_Round_Current"
		"textAlignment"		"center"
		"font"		"Cerbetica10Shadow"
		"border"			"noborder"
	}

	"RoundLimitLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"RoundLimitLabel"
		"xpos"		"220"
		"ypos"		"0"
		"wide"		"100"
		"tall"		"40"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_Scavenge_RoundLimit"
		"textAlignment"		"center"
		"font"		"Cerbetica10Shadow"
		"border"			"noborder"
	}

// **********  ROUND PANELS  ******************* 

	"Round1Panel"
	{
		"ControlName"	"CScavengeRoundPanel"
		"fieldName"		"Round1Panel"
		"xpos"			"2"
		"ypos"			"2"
		"wide"			"24"
		"tall"			"44"		
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"15"
	}
	"Round2Panel"
	{
		"ControlName"	"CScavengeRoundPanel"
		"fieldName"		"Round2Panel"
		"xpos"			"21"
		"ypos"			"2"
		"wide"			"24"
		"tall"			"44"		
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"15"
	}
	"Round3Panel"
	{
		"ControlName"	"CScavengeRoundPanel"
		"fieldName"		"Round3Panel"
		"xpos"			"40"
		"ypos"			"2"
		"wide"			"24"
		"tall"			"44"		
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"15"
	}
	"Round4Panel"
	{
		"ControlName"	"CScavengeRoundPanel"
		"fieldName"		"Round4Panel"
		"xpos"			"59"
		"ypos"			"2"
		"wide"			"24"
		"tall"			"44"		
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"15"
	}
	"Round5Panel"
	{
		"ControlName"	"CScavengeRoundPanel"
		"fieldName"		"Round5Panel"
		"xpos"			"78"
		"ypos"			"2"
		"wide"			"24"
		"tall"			"44"		
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"15"
	}

	"FinalScorePanel"
	{
		"ControlName"	"CScavengeRoundPanel"
		"fieldName"		"FinalScorePanel"
		"xpos"			"0"		//hardcoded
		"ypos"			"0"		//hardcoded
		"wide"			"18"
		"tall"			"54"		
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"15"
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	//////////////////////////////////////////////////////////////
	"ScoreBackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"ScoreBackgroundImage"
		"xpos"			"8"
		"ypos"			"70"
		"wide"			"290"
		"tall"			"60"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"alpha"			"212"
		"image"			"../vgui/hud/ScalablePanel_bgBlack_outlineRed"
		"zpos"			"10"
		
		"src_corner_height"		"16"				// pixels inside the image
		"src_corner_width"		"16"
			
		"draw_corner_width"		"8"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"8"	
	}
	
	"YourTeamLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"YourTeamLabel"
		"xpos"		"25"	[$WIN32]
		"ypos"		"82"	[$WIN32]
		"wide"		"200"
		"tall"		"16"
		"visible"		"0"
		"labelText"		"#L4D_Scavenge_YourTeam"
		"textAlignment"		"west"
		"font"		"PlayerDisplayName"
		"fgcolor_override"	"White"
	}	
	
	"EnemyTeamLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"EnemyTeamLabel"
		"xpos"		"25"	[$WIN32]
		"ypos"		"102"	[$WIN32]
		"wide"		"200"
		"tall"		"16"
		"visible"		"0"
		"labelText"		"#L4D_Scavenge_Opponent"
		"textAlignment"		"west"
		"font"		"PlayerDisplayName"
		"fgcolor_override"	"White"
	}	
	
	
	"CenterBackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"CenterBackgroundImage"
		"xpos"			"3"
		"ypos"			"59"
		"wide"			"300"
		"tall"			"71"		
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack50_outlineGrey"
		"drawcolor"		"255 64 64 255"
		"src_corner_height"		"16"			// pixels inside the image
		"src_corner_width"		"16"
		"draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"3"	
	}
	
	"CenterBackgroundFill"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"CenterBackgroundFill"
		"xpos"				"3"
		"ypos"				"59"
		"wide"				"300"
		"tall"				"71"
		"scaleImage"		"1"
		"visible"			"0"
		"enabled"			"1"
		"fillcolor" 		"0 0 0 235"
		"zpos"				"-2"
	}
}
