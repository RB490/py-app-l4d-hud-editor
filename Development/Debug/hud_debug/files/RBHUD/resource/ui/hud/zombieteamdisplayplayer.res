"Resource/UI/HUD/ZombieTeamDisplayPlayer.res"
{
	"BackgroundImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"BackgroundImage"
		"xpos"		"4"
		"ypos"		"3"
		"wide"		"149"
		"tall"		"76"
		"zpos"		"-1"
		"visible"	"0"
		"enabled"	"1"
		"scaleImage"	"1"
		"image"		"hud/pz_healthbar_250"
	}
	
	"Background_Main"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Background_Main"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"88"
		"tall"					"75"
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
		"ypos"					"54"
		"wide"					"88"
		"tall"					"21"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentLightBlack"
		"zpos"					"-5000"
	}
	
	"ZombieTeamDisplayPlayer"
	{
		"ControlName"	"Panel"
		"fieldName"	"ZombieTeamDisplayPlayer"
		"wide"		"88"
		"tall"		"100"
		"visible"	"1"
		"enabled"	"1"
	}
	"NameLabel"
	{
		"ControlName"	"Label"
		"fieldName"	"NameLabel"
		"xpos"		"0"
		"ypos"		"63"
		"wide"		"88"
		"tall"		"12"
		"visible"	"1"
		"enabled"	"1"
		"textAlignment"	"center"
		"font"		"TradeGothic11"
		"zpos"		"3"
		//"bgcolor_override"	"blue"
	}
	"HealthPanel"
	{
		"ControlName"	"HealthPanel"
		"fieldName"	"HealthPanel"
		"xpos"		"-2"
		"ypos"		"52"
		"wide"		"92"
		"tall"		"13"
		"visible"	"1"
		"enabled"	"1"
		"zpos"		"1"
	}
	"Dead"
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"Dead"
		"xpos"		"5"
		"ypos"		"28"
		"wide"		"256"
		"tall"		"0"
		"zpos"		"3"
		"visible"	"1"
		"enabled"	"1"
		"scaleImage"	"1"
		"image"		"hud/overlay_dead"
	}
	"SkullIconPlacement"
	{
		"ControlName"	"Panel"
		"fieldName"	"SkullIconPlacement"
		"xpos"		"27"
		"ypos"		"10"
		"wide"		"33"
		"tall"		"33"
		"visible"	"1"
		"enabled"	"1"
		//"bgcolor_override"		"blue"
	}
	"SpawnTimeLabel"
	{
		"ControlName"	"Label"
		"fieldName"	"SpawnTimeLabel"
		"xpos"		"27"
		"ypos"		"10"
		"wide"		"33"
		"tall"		"33"
		"zpos"		"1"
		"visible"	"1"
		"enabled"	"1"
		"textAlignment"	"center"
		"font"		"TradeGothicShadow20"
		"zpos"		"3"
	}
	"PlayerImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"PlayerImage"
		"xpos"		"27"
		"ypos"		"10"
		"wide"		"33"
		"tall"		"33"
		"visible"	"1"
		"enabled"	"1"
		"zpos"		"3"
		"fgcolor_override" "255 255 255 255"
	}
	"AbilityProgress"
	{
		"ControlName"	"CircularProgressBar"
		"fieldName"	"AbilityProgress"
		"xpos"		"19"
		"ypos"		"2"
		"wide"		"50"
		"tall"		"50"
		"visible"	"1"
		"enabled"	"1"
		"zpos"		"2"
		"fg_image"	"HUD/PZ_charge_meter"
		"progress"	"0.75"
	}
	"Voice"
	{
		"ControlName"	"Panel"
		"fieldName"		"Voice"
		"xpos"			"72"
		"ypos"			"0"
		"wide"			"16"
		"tall"			"16"
		"visible"		"0"
		"enabled"		"1"
		"zpos"			"3"
		"voice_icon"	"voice_player"
	}
	"Background_Voice"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"Background_One"
		"xpos"				"72"
		"ypos"				"0"
		"wide"				"16"
		"tall"				"16"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"1"
		"tabPosition"		"0"
		"fillColor"			"Red"
		"zpos"				"-5000"
	}
}