"Resource/UI/ThirdPartyServerPanel.res"
{
	"BackgroundFill1"
	{
		"ControlName"		"Panel"
		"fieldName"			"CUSTOM1"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"270"
		"tall"			"55"
		"visible"			"0"
		"enabled"			"1"
		"bgcolor_override"	"TransparentLightBlack"
		"zpos"				"-5"
	}
	"HostnameLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"HostnameLabel"
		"xpos"			"40"
		"ypos"			"9"
		"wide"			"190"
		"tall"			"38"
		"zpos"		"1"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"	//0
		"enabled"		"1"
		"labelText"		"%hostname%"	//%hostname% //.: ffn | Zombiehall | HLStatsX | www.ffn-clan.de
		"textAlignment"		"center"
		"dulltext"		"1"
		"brighttext"		"0"
		"font"		"TradeGothic12"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"black"
	}
	"HTMLMessage"
	{
		"ControlName"	"HTML"
		"fieldName"		"HTMLMessage"
		"xpos"			"40"
		"ypos"			"9"
		"wide"			"190"
		"tall"			"38"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"zpos"			"11"
	}
	
	
	
	
	//////////////////////////////////////////////////////////////////////
	
	"BackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"BackgroundImage"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"300"
		"tall"			"130"
		"visible"		"0"
		"enabled"		"0"
		"scaleImage"	"1"
		"image"			"../vgui/hud/ScalablePanel_bgBlack_outlineGrey"
		"zpos"			"-2"
		"src_corner_height"		"16"
		"src_corner_width"		"16"
		"draw_corner_width"		"2"
		"draw_corner_height" 	"2"
		"if_embedded"
		{
			"visible"	"0"
		}
	}
	"TerrorTextMessage"
	{
		"ControlName"	"CTerrorRichText"
		"fieldName"		"TerrorTextMessage"
		"xpos"			"230"
		"ypos"			"0"
		"wide"			"214"
		"tall"			"45"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"textAlignment"	"northwest"
		"textHidden"	"0"
		"editable"		"1"
		"maxchars"		"0"
	}
	"ServerTitle"
	{
		"ControlName"		"Label"
		"fieldName"		"ServerTitle"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"270"
		"tall"			"55"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"Server"
		"textAlignment"		"center"
		"dulltext"		"0"
		"brighttext"		"0"
		"font"		"TradeGothic12"
	}
	"RankLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"RankLabel"
		"xpos"		"3"
		"ypos"		"90"
		"wide"		"220"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"0"
		"labelText"		"#L4D_Server_Rank"
		"textAlignment"		"north-west"
		"dulltext"		"1"
		"brighttext"		"0"
		"fgcolor_override"	"White"
		"auto_wide_tocontents"	"1"
	}
	"RankAmount"
	{
		"ControlName"		"Label"
		"fieldName"		"RankAmount"
		"xpos"		"0"
		"ypos"		"0"
		"wide"		"20"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"0"
		"labelText"		"%rank%"
		"textAlignment"		"north-west"
		"dulltext"		"1"
		"brighttext"		"0"
		"fgcolor_override"	"MediumGray"
		"auto_wide_tocontents"	"1"
		"pin_to_sibling"		"RankLabel"
		"pin_corner_to_sibling"	"0"
		"pin_to_sibling_corner"	"1"
	}
	"PlayerCountLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"PlayerCountLabel"
		"xpos"		"5"
		"ypos"		"107"
		"wide"		"220"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"0"
		"labelText"		"#L4D_Server_Player_Count"
		"textAlignment"		"north-west"
		"dulltext"		"1"
		"brighttext"		"0"
		"fgcolor_override"	"White"
		"auto_wide_tocontents"	"1"
	}
	"PlayerCountAmount"
	{
		"ControlName"		"Label"
		"fieldName"		"PlayerCountAmount"
		"xpos"		"0"
		"ypos"		"0"
		"wide"		"220"
		"tall"		"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"0"
		"labelText"		"%playercount%"
		"textAlignment"		"north-west"
		"dulltext"		"1"
		"brighttext"		"0"
		"fgcolor_override"	"MediumGray"
		"pin_to_sibling"		"PlayerCountLabel"
		"pin_corner_to_sibling"	"0"
		"pin_to_sibling_corner"	"1"
	}
}