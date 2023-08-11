"Resource/UI/versusmodescoreboard_tiebreak.res"
{
	"Background_Main"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Background_Main"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"210"
		"tall"					"65"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentLightBlack"
		"zpos"					"-5000"
	}
	
	"Background_One"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Background_One"
		"xpos"					"0"
		"ypos"					"30"
		"wide"					"210"
		"tall"					"35"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentLightBlack"
		"zpos"					"-5000"
	}
	
	"Background_Two"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Background_Two"
		"xpos"					"0"
		"ypos"					"45"
		"wide"					"210"
		"tall"					"20"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentLightBlack"
		"zpos"					"-5000"
	}
	
	"RoundInfoMessage"
	{
		"ControlName"		"Label"
		"fieldName"		"RoundInfoMessage"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"210"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_Scavenge_TieBreaker_Title"
		"textAlignment"		"center"
		"font"		"TradeGothic18"
		"bgcolor_override"	"blank"
	}
	
	
	"TieBreakerMethodLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"TieBreakerMethodLabel"
		"xpos"			"0"
		"ypos"			"13"
		"wide"			"210"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#L4D_Versus_TieBreaker_Description"
		"textAlignment"		"center"
		"font"				"TradeGothic11"
	}
	
	"YourTeamLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"YourTeamLabel"
		"xpos"				"5"
		"ypos"				"30"
		"wide"				"100"
		"tall"				"15"
		"visible"			"1"
		"labelText"			"You:"
		"textAlignment"		"center"
		"font"				"TradeGothic14"
		"bgcolor_override"	"blank"
	}	

	"EnemyTeamLabel"
	{
		"ControlName"		"Label"
		"fieldName"			"EnemyTeamLabel"
		"xpos"				"105"
		"ypos"				"30"
		"wide"				"100"
		"tall"				"15"
		"visible"			"1"
		"labelText"			"Enemy:"
		"textAlignment"		"center"
		"font"				"TradeGothic14"
		"bgcolor_override"	"blank"
	}	

	"YourTeamDamage"
	{
		"ControlName"		"Label"
		"fieldName"			"YourTeamDamage"
		"xpos"				"5"
		"ypos"				"45"
		"wide"				"100"
		"tall"				"20"
		"visible"			"1"
		"labelText"			"0"
		"textAlignment"		"center"
		"font"				"TradeGothic18"
		"bgcolor_override"	"blank"
		
	}	
	
	"EnemyTeamDamage"
	{
		"ControlName"		"Label"
		"fieldName"			"EnemyTeamDamage"
		"xpos"				"105"
		"ypos"				"45"
		"wide"				"100"
		"tall"				"20"
		"visible"			"1"
		"labelText"			"0"
		"textAlignment"		"center"
		"font"				"TradeGothic18"
		"bgcolor_override"	"blank"
	}	
	
	"YourTeamBonus"
	{
		"ControlName"		"Label"
		"fieldName"			"YourTeamBonus"
		"xpos"				"220"
		"ypos"				"40"
		"wide"				"100"
		"tall"				"20"
		"visible"			"0"
		"labelText"			"+ 25"
		"textAlignment"		"west"
		"font"				"TradeGothic18"
		"bgcolor_override"	"blank"
	}
	
	"EnemyTeamBonus"
	{
		"ControlName"		"Label"
		"fieldName"			"EnemyTeamBonus"
		"xpos"				"220"
		"ypos"				"60"
		"wide"				"100"
		"tall"				"20"
		"visible"			"0"
		"labelText"			"+ 25"
		"textAlignment"		"west"
		"font"				"TradeGothic18"
		"bgcolor_override"	"blank"
	}
	
	
	// NOT USED //////////////////////////////////////////////////////////
	
	"HeaderBackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"HeaderBackgroundImage"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"280"
		"tall"			"26"		
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

	"HeaderBackgroundFill"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"HeaderBackgroundFill"
		"xpos"				"0"
		"ypos"				"0"
		"wide"				"280"
		"tall"				"26"
		"scaleImage"		"1"
		"visible"			"0"
		"enabled"			"1"
		"fillcolor" 		"0 0 0 255"
		"zpos"				"-2"
	}
	
	"CenterBackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"CenterBackgroundImage"
		"xpos"			"0"
		"ypos"			"25"
		"wide"			"280"
		"tall"			"65"		
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
		"xpos"				"0"
		"ypos"				"25"
		"wide"				"280"
		"tall"				"65"
		"scaleImage"		"1"
		"visible"			"0"
		"enabled"			"1"
		"fillcolor" 		"0 0 0 255"
		"zpos"				"-2"
	}
}