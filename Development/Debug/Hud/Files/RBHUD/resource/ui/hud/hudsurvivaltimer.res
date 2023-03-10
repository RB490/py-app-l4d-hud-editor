"Resource/UI/HUD/HudSurvivalTimer.res"
{	
	"SurvivalTimerBackgroundImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"SurvivalTimerBackgroundImage"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"440"
		"tall"			"100"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"hud/SurvivalTimerBackground"
		"zpos"			"-2"
	}
	
	"Background_Main"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Background_Main"
		"xpos"			"c-80"
		"ypos"			"0" 
		"zpos"			"0"
		"wide"			"160"
		"tall"			"30" 
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentLightBlack"
		"zpos"					"-5000"
	}
	
	"Background_One"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Background_One"
		"xpos"			"c-80"
		"ypos"			"10" 
		"zpos"			"0"
		"wide"			"160"
		"tall"			"20" 
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentLightBlack"
		"zpos"					"-5000"
	}
	
	"CurrentTimeDigits"
	{
		"ControlName"	"Label"
		"fieldName"		"CurrentTimeDigits"
		"xpos"			"c-35"
		"ypos"			"0" 
		"zpos"			"500"
		"wide"			"85"
		"tall"			"20" 
		"visible"		"1"
		"labelText"		"555:55.55"
		"textAlignment"	"west"
		"font"			"TradeGothicShadow20"
		"bgcolor_override"	"blank"
	}
	
	"TargetTransition"
	{
		"ControlName"	"Label"
		"fieldName"		"TargetTransition"
		"xpos"			"c-40"
		"ypos"			"10" 
		"zpos"			"500"
		"wide"			"85"
		"tall"			"20" 
		"visible"		"0"
		"alpha"			"0"
		"labelText"		"00:00.00"
		"textAlignment"	"west"
		"zpos"			"500"
		"font"			"TradeGothicShadow11"
	}
	
	"TargetTimeDigits"
	{
		"ControlName"	"Label"
		"fieldName"		"TargetTimeDigits"
		"xpos"			"c-55"
		"ypos"			"0"
		"zpos"			"500"
		"wide"			"50"
		"tall"			"10" 
		"visible"		"0"
		"labelText"		"555:55.55"
		"textAlignment"	"east"
		"zpos"			"500"
		"font"			"TradeGothicShadow11"
		"bgcolor_override"	"blank"
	}
	
	"Timer"
	{
		"ControlName"	"CircularProgressBar"
		"fieldName"		"Timer"
		"xpos"			"c-5"
		"ypos"			"0"
		"wide"			"11"
		"tall"			"11"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"bg_image"			"hud\SurvivalTimerClock"
		"fg_image"			"hud\SurvivalTimerClockFace"
	}
	
	"NextGoalDescriptor"
	{
		"ControlName"	"Label"
		"fieldName"		"NextGoalDescriptor"
		"xpos"			"c6"
		"ypos"			"0"
		"wide"			"50"
		"tall"			"10" 
		"visible"		"0"
		"labelText"		"EXTREMEBLOODYREVENGE"	//WWWWWWWWWWWWWWW's Migliore
//		"labelText"		"Gold Standard"
		"textAlignment"	"west"
		"zpos"			"500"
		"font"			"TradeGothicShadow11"
		"bgcolor_override"	"blank"
	}
	
	"AwesomeLabel"	// new team record!
	{
		"ControlName"	"Label"
		"fieldName"		"AwesomeLabel"
		"xpos"			"1209999"
		"ypos"			"62"
		"wide"			"200"
		"tall"			"12"
		"alpha"			"0"
		"visible"		"1"
		"labelText"		"#L4D_SurvivalTimer_Description_KeepGoing"
		"textAlignment"	"center"
		"font"			"PlayerDisplayHealth"
	}

	"SurvivalTargetTimeBackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"SurvivalTargetTimeBackgroundImage"
		"xpos"			"180"
		"ypos"			"29"
		"wide"			"257"
		"tall"			"42"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgMidGrey_glow"
		"zpos"			"-1"
		
		"src_corner_height"		"16"				// pixels inside the image
		"src_corner_width"		"16"
			
		"draw_corner_width"		"8"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"8"	
	}
	
	"CurrentTimeBackground"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"CurrentTimeBackground"
		"xpos"			"2"
		"ypos"			"29"
		"wide"			"180"
		"tall"			"42"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgMidGrey_glow"
		"zpos"			"-1"
		
		"src_corner_height"		"16"				// pixels inside the image
		"src_corner_width"		"16"
			
		"draw_corner_width"		"8"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"8"	
	}
	
	"GoalImage"
	{
		"ControlName"	"CIconPanel"
		"fieldName"		"GoalImage"
		"xpos"			"c-7"
		"ypos"			"c0"
		"wide"			"15"
		"tall"			"15"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"	
		"zpos"			"500"
		"icon"			"icon_bronze_medal_small"
	}
}
