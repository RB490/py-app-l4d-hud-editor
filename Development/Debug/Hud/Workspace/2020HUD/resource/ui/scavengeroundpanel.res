"Resource/UI/ScavengeRoundPanel.res"		//a single round entry in the scavenge scoreboard
{
	
	"RoundFirstTeamScore"
	{
		"ControlName"		"Label"
		"fieldName"		"RoundFirstTeamScore"
		"xpos"		"0"
		"ypos"		"0"
		"wide"		"18"
		"tall"		"18"
		"visible"		"1"
		"labelText"		""
		"textAlignment"		"center"
		"font"		"Cerbetica10Shadow"
		
		"font"		"Cerbetica10"
		"fgcolor_override"	"White"
	
		"bgcolor_override"  "0 115 0 115"
		"border"            "blackborder"
	}	

	"RoundSecondTeamScore"
	{
		"ControlName"		"Label"
		"fieldName"		"RoundSecondTeamScore"
		"xpos"		"0"
		"ypos"		"19"
		"wide"		"18"
		"tall"		"18"
		"visible"		"1"
		"labelText"		""
		"textAlignment"		"center"
		
		"font"		"Cerbetica10Shadow"
		"fgcolor_override"	"White"
	
		"bgcolor_override"  "115 0 0 115"
		"border"            "blackborder"
	}	
	
	
	
	///////////////////////////////////////////
	
	
	
	"RoundSecondTeamImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"RoundSecondTeamImage"
		"xpos"			"0"
		"ypos"			"21"
		"wide"			"22"
		"tall"			"22"		
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
	
	"RoundFirstTeamImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"RoundFirstTeamImage"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"22"
		"tall"			"22"		
		"visible"		"0"
		"enabled"		"0"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack50_outlineGrey"
		"drawcolor"		"255 64 64 255"
		"src_corner_height"		"16"			// pixels inside the image
		"src_corner_width"		"16"
		"draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"3"	
	}
	
	BGPanelFirstTeam
	{
		"fieldname"         "BGPanelFirstTeam"
		"controlName"       "Panel"
		"visible"           "0"
		"enabled"           "1"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"20"
		"tall"			"20"	
		"zpos"              "20"
		
		"font"		"Cerbetica10"
		"fgcolor_override"	"White"
	
		"bgcolor_override"  "0 115 0 115"
		"border"            "blackborder"
	}
	
	BGPanelSecondTeam
	{
		"fieldname"         "BGPanelSecondTeam"
		"controlName"       "Panel"
		"visible"           "0"
		"enabled"           "1"
		"xpos"			"0"
		"ypos"			"21"
		"wide"			"20"
		"tall"			"20"	
		"zpos"              "0"
		"bgcolor_override"  "TransparentBlack"
		"border"            "BlackBorder"
	}
}
