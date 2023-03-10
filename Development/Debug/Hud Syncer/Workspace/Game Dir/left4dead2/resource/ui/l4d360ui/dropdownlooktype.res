"Resource/UI/DropDownLookType.res"
{
	"PnlBackground"
	{
		"ControlName"		"Panel"
		"fieldName"			"PnlBackground"
		"xpos"				"0"
		"ypos"				"0"
		"zpos"				"-1"
		"wide"				"156"
		"tall"				"45"
		"visible"			"1"
		"enabled"			"1"
		"paintbackground"	"1"
		"paintborder"		"1"
	}

	"BtnNormal"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnNormal"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"150"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"wrap"					"1"
		"navUp"					"BtnInverted"
		"navDown"				"BtnInverted"
		"labelText"				"#L4D360UI_Controller_Normal"
		"tooltiptext"			"#L4D360UI_Controller_Tooptip_Look_Normal"
		"style"					"FlyoutMenuButton"
		"command"				"#L4D360UI_Controller_Normal"
		"OnlyActiveUser"		"1"
	}	
	
	"BtnInverted"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnInverted"
		"xpos"					"0"
		"ypos"					"20"
		"wide"					"150"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"wrap"					"1"
		"navUp"					"BtnNormal"
		"navDown"				"BtnNormal"
		"labelText"				"#L4D360UI_Controller_Inverted"
		"tooltiptext"			"#L4D360UI_Controller_Tooptip_Look_Inverted"
		"style"					"FlyoutMenuButton"
		"command"				"#L4D360UI_Controller_Inverted"
		"OnlyActiveUser"		"1"
	}	
}