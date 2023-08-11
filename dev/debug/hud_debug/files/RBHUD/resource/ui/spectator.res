"Resource/UI/SpectatorGUI.res"
{
	"specgui"
	{
		"ControlName"	"Frame"
		"fieldName"		"specgui"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"480"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
	}
	"SpectatingTextCustom"
	{
		"ControlName"	"Label"
		"fieldName"		"SpectatingTextCustom"
		"xpos"		"c-150"
		"ypos"		"40"
		"wide"		"300"
		"tall"		"25"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"SPECTATING"
		"textAlignment"		"center"
		"dulltext"		"0"
		"brighttext"		"0"
		"font"		"TradeGothicShadow20"
	}
	"playerlabel"
	{
		"ControlName"	"Label"
		"fieldName"		"playerlabel"
		"xpos"			"c-150"
		"ypos"			"60"
		"wide"			"300"
		"tall"			"15"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"	//0
		"enabled"		"1"
		"tabPosition"	"0"
		"textAlignment"	"center"
		"bgcolor_override"		"blank"
		"font"			"TradeGothicShadow15"
	}
	
	//////////////////////////////////////////////////////////////////////////
	
	
	"topbar"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"topbar"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"52"
		"visible"		"0"
		"enabled"		"0"
		"fillcolor_override"	"0 0 0 196"
	}
	"bottombar"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"bottombar"
		"xpos"			"0"
		"ypos"			"r52"
		"wide"			"f0"
		"tall"			"52"
		"visible"		"0"
		"enabled"		"0"
		"fillcolor_override"	"0 0 0 196"
	}
	"RescueMessage" // suppress
	{
		"ControlName"		"Label"
		"fieldName"		"RescueMessage"
		"visible"	"0"
		"wide"		"0"
		"tall"		"0"
	}
}
