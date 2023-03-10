"Resource/UI/Achievements.res"
{
	"Achievements"
	{
		"ControlName"		"Frame"
		"fieldName"		"Achievements"
		
		"xpos"			"0"		[$WIN32]
		"ypos"			"0"		[$WIN32]
		"wide"			"f0"	[$WIN32]
		"tall"			"480"	[$WIN32]
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"usetitlesafe"	"1"
	}
	
	"BackgroundImage"	[$WIN32]
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"BackgroundImage"
		"xpos"			"0"
		"ypos"			"c-150"
		"zpos"			"0"
		"wide"			"f0"
		"tall"			"345"
		"autoResize"	"1"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"tabPosition"	"0"	
		"fillcolor"		"TransparentBlack"
	}
	
	"Background_Header"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_Header"
		"xpos"				"0"
		"ypos"				"20"
		"wide"			"f0"
		"tall"			"40"	//22
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-150033"
		"bgcolor_override"	"TransparentBlack"
	}
	
	"Background_ButtonSave"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_ButtonSave"
		"xpos"				"0"
		"ypos"				"65"
		"wide"			"f0"
		"tall"			"20"	//22
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-1500"
		"bgcolor_override"	"TransparentBlack"
	}
	
	"Background_Progress"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_ButtonSave"
		"xpos"			"c-223"	[$WIN32]
		"ypos"			"410"	[$WIN32]
		"wide"			"447"
		"tall"			"20"	//22
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-1500"
		"bgcolor_override"	"TransparentBlack"
	}
	
	"ProTotalProgress"
	{
		"ControlName"			"ContinuousProgressBar"
		"fieldName"				"ProTotalProgress"
		"xpos"					"c-223"	[$WIN32]
		"ypos"					"410"	[$WIN32]
		"wide"					"447"	[$WIN32]
		"zpos"					"1"
		"tall"					"5"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"proportionalToParent"	"1"
	}
	
	"LblComplete"
	{
		"ControlName"		"Label"
		"fieldName"		"LblComplete"
		"xpos"			"c-221"	[$WIN32]
		"ypos"			"412"	[$WIN32]
		"wide"			"450"
		"zpos"					"1"
		"tall"			"20" [$WIN32]
		"autoResize"		"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"proportionalToParent"	"1"
		"textAlignment"		"west"
	}

	"GplAchievements"
	{
		"ControlName"		"GenericPanelList"
		"fieldName"		"GplAchievements"
		"xpos"			"c-226"	
		"ypos"			"90"	
		"wide"			"450"	
		"tall"			"315"	
		"zpos"					"1"
		"autoResize"		"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"1"
		"proportionalToParent"	"1"
		
		"bgcolor_override"		"TransparentBlack"
	}

	"BtnCancel" [$WIN32]
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnCancel"
		"xpos"					"c-220"
		"ypos"					"68"
		"zpos"					"1"
		"wide"					"75"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"wrap"					"1"
		"labelText"				"#L4D360UI_Done"
		"tooltiptext"			"#L4D360UI_Tooltip_Back"
		"style"					"MainMenuButton"
		"command"				"Back"
		"proportionalToParent"	"1"
		"usetitlesafe" 			"0"
		EnabledTextInsetX		"2"
		DisabledTextInsetX		"2"
		FocusTextInsetX			"2"
		OpenTextInsetX			"2"
		"allcaps"				"1"
	}
	
	"LblGamerscore"
	{
		"ControlName"		"Label"
		"fieldName"		"LblGamerscore"
		"xpos"			"r270"
		"ypos"			"59"
		"wide"			"250"
		"zpos"					"1"
		"autoResize"		"1"
		"pinCorner"		"0"
		"visible"		"0" [$WIN32]
		"enabled"		"1"
		"tabPosition"		"0"
		"proportionalToParent"	"1"
		"textAlignment"		"east"
	}
	
	"Divider2"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Divider2"
		"xpos"					"c-238"	
		"ypos"					"378"	
		"zpos"					"2"
		"wide"					"450"
		"tall"					"2"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"divider_gradient"
		"scaleImage"			"1"
	}

	"Divider1"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Divider1"
		"xpos"					"c-238"	
		"ypos"					"110"	
		"zpos"					"2"
		"wide"					"450"
		"tall"					"2"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"divider_gradient"
		"scaleImage"			"1"
	}
	
	"PnlLowerGarnish"
	{
		"ControlName"		"Panel"
		"fieldName"		"PnlLowerGarnish"
		"xpos"			"0"
		"ypos"			"r45"
		"zpos"			"-1"
		"wide"			"f0"
		"tall"			"45"
		"autoResize"		"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"proportionalToParent"	"1"
	}
}
