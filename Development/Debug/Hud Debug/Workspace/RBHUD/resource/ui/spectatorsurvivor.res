"Resource/UI/SpectatorSurvivor.res"
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
	
	"death"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"death"
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

	"DeathMessage"
	{
		"ControlName"	"Label"
		"fieldName"		"DeathMessage"
		"xpos"		"c-150"
		"ypos"		"40"
		"wide"		"300"
		"tall"		"25"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_pz_spectator_title"
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
		"visible"		"0" //0
		"enabled"		"1"
		"tabPosition"	"0"
		"textAlignment"	"center"
		"bgcolor_override"		"blank"
		"font"			"TradeGothicShadow15"
	}

	////////////////////////////////////////////////////////////////////////////////
	
	"HeaderBackground"
	{
		"ControlName"	"Panel"
		"fieldName"		"HeaderBackground"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"75"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"0"
		"tabPosition"	"0"
		"bgcolor_override"	"Black"
		"zpos"			"-2"
		"paintbackground"	"1"
	}
	
	"FooterBackground"
	{
		"ControlName"		"Panel"
		"fieldName"			"FooterBackground"
		"xpos"				"0"
		"ypos"				"r90"	[$WIN32]
		"ypos"				"r115"	[$X360]
		"wide"				"f0"
		"tall"				"90"	[$WIN32]
		"tall"				"115"	[$X360]
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"		
		"enabled"			"0"
		"tabPosition"		"0"
		"bgcolor_override"	"Black"
		"zpos"				"-2"
		
		"if_split_screen_active"
		{
			"visible"	"0"
		}
	}
	"InfoIcon"
	{
		"ControlName"		"CIconPanel"
		"fieldName"			"InfoIcon"
		"xpos"				"29"
		"ypos"				"r43"
		"wide"				"24"
		"tall"				"24"
		"visible"			"0"
		"enabled"			"0"
		"tabPosition"		"0"
		"icon"			    "icon_tip"
		"zpos"				"60"
		"scaleImage"	    "1"
		"usetitlesafe"		"1"
		
		"if_split_screen_active"
		{
			"visible"	"0"
		}
	}
	
	"InfoIconBackground"
	{
		"ControlName"		"Panel"
		"fieldName"			"InfoIconBackground"
		"xpos"				"30"
		"ypos"				"r55"
		"wide"				"17"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"0"
		"tabPosition"		"0"
		"bgcolor_override"	"TransparentLightBlack"
		"zpos"				"60"
		"usetitlesafe"		"1"
		
		"if_split_screen_active"
		{
			"visible"	"0"
		}
	}

	"TipText"
	{
		"ControlName"		"Label"
		"fieldName"			"TipText"
		"xpos"				"57"
		"ypos"				"r43"
		"wide"				"300"
		"tall"				"45"
		"wrap"				"1"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"0"
		"labelText"			"#L4D_SpecSurvivorTip"
		"textAlignment"		"north-west"
		"dulltext"			"0"
		"brighttext"		"1"
		"font"				"BodyText_small"
		"zpos"				"40"
		"usetitlesafe"		"1"
		
		"if_split_screen_active"
		{
			"visible"	"0"
		}
	}
	
	"SkullIcon"
	{		
		"ControlName"		"CIconPanel"
		"fieldName"			"SkullIcon"
		"xpos"				"c-11"
		"ypos"				"7"
		"wide"				"22"
		"tall"				"22"
		"visible"			"0"
		"enabled"			"1"
		"tabPosition"		"0"
		"icon"			    "icon_skull"
		"zpos"				"60"
		"scaleImage"	    "1"
	}
	
	"RescueMessage"
	{
		"ControlName"		"Label"
		"fieldName"		"RescueMessage"
		"xpos"		"c-1509999"
		"ypos"		"50"
		"wide"		"300"
		"tall"		"15"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"labelText"		"%rescuemsg%"
		"textAlignment"		"center"
		"dulltext"		"0"
		"brighttext"		"0"
		"wrap"		"0"
		"fgcolor_override"	"DeepRed"
		"font"		"TradeGothicShadow15"
	}
}
