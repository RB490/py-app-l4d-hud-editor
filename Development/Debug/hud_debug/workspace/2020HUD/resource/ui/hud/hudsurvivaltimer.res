// Survival round timer
"Resource/UI/HUD/HudSurvivalTimer.res"
{

	AwesomeLabel
	{
		"fieldname"      "AwesomeLabel"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "160"
		"ypos"           "0"
		"wide"           "150"
		"tall"           "15"
		"alpha"          "0"		// set to 0
		"font"           "Cerbetica18Shadow"
		"labelText"      "#L4D_SurvivalTimer_Description_KeepGoing"
		"textAlignment"  "west"
		//"border"		"baseborder"
	}

	CurrentTimeDigits
	{
		"fieldname"      "CurrentTimeDigits"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "0"
		"ypos"           "0"
		"zpos"           "1"
		"wide"           "150"
		"tall"           "15"
		"font"           "Cerbetica18Shadow"
		"labelText"      "07:89.00"
		"textAlignment"  "east"
		"fgcolor_override"	""
		//"border"		"baseborder"
	}

	GoalImage
	{
		"fieldname"    "GoalImage"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "150"
		"ypos"         "15"
		"wide"         "15"
		"tall"         "15"
		"icon"         "icon_bronze_medal_small"
		"scaleImage"   "1"
		//"border"		"baseborder"
	}

	NextGoalDescriptor
	{
		"fieldname"      "NextGoalDescriptor"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "0"
		"ypos"           "28"
		"zpos"           "1"
		"wide"           "165"
		"tall"           "15"
		"font"           "Cerbetica10Shadow"
		"labelText"      "WWWWWWWWWWWWWWW's Migliore"
		"textAlignment"  "north-east"
		"fgcolor_override"	""
		//"border"		"baseborder"
	}

	TargetTimeDigits
	{
		"fieldname"      "TargetTimeDigits"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "0"
		"ypos"           "15"
		"zpos"           "1"
		"wide"           "150"
		"tall"           "15"
		"font"           "Cerbetica12Shadow"
		"labelText"      "00:00.00"
		"textAlignment"  "east"
		"fgcolor_override"	""
		//"border"		"baseborder"
	}

	TargetTransition
	{
		"fieldname"      "TargetTransition"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "0"
		"ypos"           "15"
		"zpos"           "1"
		"wide"           "150"
		"tall"           "15"
		"alpha"			"0"
		"font"           "Cerbetica14Shadow"
		"labelText"      "00:00.00"
		"textAlignment"  "east"
		"fgcolor_override"	""
		//"border"		"baseborder"
	}

	Timer
	{
		"fieldname"    "Timer"
		"controlName"  "CircularProgressBar"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "150"
		"ypos"         "0"
		"wide"         "15"
		"tall"         "15"
		"bg_image"     "hud\survivalTimerClock"
		"fg_image"     "hud\survivalTimerClockFace"
		"scaleImage"   "1"
		//"border"		"baseborder"
	}
}
