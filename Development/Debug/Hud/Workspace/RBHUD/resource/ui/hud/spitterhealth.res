"Resource/UI/HUD/SpitterHealth.res"
{
	// HudLayout has size/position of HudZombieHealth panel this is part of

	"BackgroundImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"BackgroundImage"
		"xpos"		"189"
		"ypos"		"29"
		"wide"		"224"
		"tall"		"112"
		"visible"	"0"
		"enabled"	"1"
		"scaleImage"	"1"
		"image"		"HUD/infected_healthbar_bg_1"
		"zpos"		"-2"
		"drawColor"	"0 0 0 255"
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
	
	"Health"
	{
		"ControlName"	"HealthPanel"
		"fieldName"	"Health"
		"xpos"		"-2"
		"ypos"		"52"
		"wide"		"92"
		"tall"		"13"
		"visible"	"1"
		"enabled"	"1"
		"zpos"		"1"
	}

	"HealthIcon"
	{
		"ControlName"	"Label"
		"fieldName"	"HealthIcon"
		"xpos"		"254"
		"ypos"		"73"
		"wide"		"20"
		"tall"		"40"
		"visible"	"0"
		"enabled"	"0"
		"labelText"	"+"
		"textAlignment"	"west"
		"font"		"InfectedH"
		"zpos"		"2"
	}

	"HealthNumber"
	{
		"ControlName"	"Label"
		"fieldName"	"HealthNumber"
		"xpos"		"0"
		"ypos"		"63"
		"wide"		"88"
		"tall"		"12"
		"visible"	"1"
		"enabled"	"1"
		"labelText"	"%HealthNumber%"
		"textAlignment"	"center"
		"font"		"TradeGothic11"
		"zpos"		"2"
	}

	
	"DuckingIcon"
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"DuckingIcon"
		"xpos"		"70"
		"ypos"		"0"
		"wide"		"16"
		"tall"		"16"
		"zpos"		"2"
		"visible"	"1"
		"enabled"	"1"
		"scaleImage"	"1"
		"image"		"hud/crouch_infected"
	}
}