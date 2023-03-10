"Resource/UI/TextWindow.res"
{
	"info"
	{
		"ControlName"		"CTextWindow"
		"fieldName"		"TextWindow"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"480"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"PaintBackgroundType"	"0"
		"settitlebarvisible" "0"
		"bgcolor_override"	"TransparentLightBlack"
		"infocus_bgcolor_override" "TransparentLightBlack"
		"outoffocus_bgcolor_override" "TransparentLightBlack"
	}

	"Background_Custom"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_Custom"
		"xpos"			"c-250"
		"ypos"			"22"
		"wide"			"500"
		"tall"			"400"
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-2000"
		"bgcolor_override"	"TransparentLightBlack"
	}
	
	"MessageTitle"
	{
		"ControlName"		"Label"
		"fieldName"			"MessageTitle"
		"xpos"				"c-240"
		"ypos"				"120"
		"wide"				"480"
		"tall"				"30"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"1"
		"labelText"			"Message Title"
		"textAlignment"		"west"
		"dulltext"			"0"
		"brighttext"		"0"
		"font"				"MainBold"
		"fgcolor_override"	"255 255 255 255"
	}
		
	"HTMLMessage"
	{
		"ControlName"	"HTML"
		"fieldName"		"HTMLMessage"
		"xpos"			"c-240"
		"ypos"			"90"
		"wide"			"480"
		"tall"			"300"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
	}
	
	// This just hides the old text message, because we're replacing it with our fancier TerrorTextMessage below.
	"TextMessage"
	{
		"ControlName"	"TextEntry"
		"fieldName"		"TextMessage"
		"visible"		"0"
		"enabled"		"0"
	}
	
	"TerrorTextMessage"
	{
		"ControlName"	"CTerrorRichText"
		"fieldName"		"TerrorTextMessage"
		"xpos"			"c-240"
		"ypos"			"90"
		"wide"			"480"
		"tall"			"300"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"textAlignment"	"northwest"
		"textHidden"	"0"
		"editable"		"0"
		"maxchars"		"-1"
		"bgcolor_override"	"blank"
	}
	
	"ok"
	{
		"ControlName"	"Button"
		"fieldName"		"ok"
		"xpos"			"c240"
		"ypos"			"400"
		"wide"			"128"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"2"
		"visible"		"0"
		"enabled"		"0"
		"labelText"		"#PropertyDialog_OK"
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"command"		"okay"
		"default"		"0"
	}
	
	"L4Dok"
	{
		"ControlName"	"L4DButton"
		"fieldName"		"L4Dok"
		"xpos"			"c-240"
		"ypos"			"395"
		"wide"			"60"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"2"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"Close"
		"textAlignment"	"west"
		"dulltext"		"0"
		"brighttext"	"0"
		"command"		"okay"
		"default"		"1"
		"paintborder"	"1"
	}
	
	"JoinSteamGroup"
	{
		"ControlName"	"L4DButton"
		"fieldName"		"JoinSteamGroup"
		"xpos"			"c-10"
		"ypos"			"395"
		"wide"			"250"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"2"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_JoinSteamGroup"
		"textAlignment"	"east"
		"dulltext"		"0"
		"brighttext"	"0"
		"command"		"joinsteamgroup"
		"default"		"0"
		"paintborder"	"1"
	}
	
	"NewsKeyBind"
	{
		"ControlName"	"KeybindLabel"
		"fieldName"		"NewsKeyBind"
		"xpos"			"c-240"
		"ypos"			"400"
		"wide"			"240"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"tabPosition"	"0"
		"labelText"		""
		"textAlignment"	"west"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"DefaultBold"
		"textcolor"		"145 145 145 255"
		"keycolor"		"255 255 255 255"
	}
	
	"ThirdPartyServerPanel"
	{
		"ControlName"	"CThirdPartyServerPanel"
		"fieldName"		"ThirdPartyServerPanel"
		"xpos"			"c-240"
		"ypos"			"30"
		"wide"			"270"
		"tall"			"55"
		"visible"		"1"		[$WIN32]
		"visible"		"0"	    [$X360]
		"enabled"		"1"
		"embedded"		"1"
	}
	
	"Background_ThirdPartyServerPanel"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_ThirdPartyServerPanel"
		"xpos"			"c-240"
		"ypos"			"30"
		"wide"			"270"
		"tall"			"55"
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-2000"
		"bgcolor_override"	"TransparentLightBlack"
	}
}
