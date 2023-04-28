"Resource/UI/BaseChat.res"
{
	// chat screen position
	"HudChat"
	{
		"ControlName"			"EditablePanel"
		"fieldName" 			"HudChat"
		"visible" 				"1"
		"enabled" 				"1"
		"xpos"					"20"
		"ypos"                  "r315"	// r335
		"wide"	 				"280"
		"tall"	 				"120"
		"PaintBackgroundType"	"0"
		"usetitlesafe"			"1"
		"bgcolor_override"		"40 40 40 255"
		"border" "TitleButtonBorder"
	}

	// multiplier key combinations
	KeyStateLabel
	{
		"ControlName"		"Label"
		"fieldname"			"KeyStateLabel"
		"visible" 			"1"
		"enabled" 			"1"
		"xpos"				"10999"
		"ypos"				"2"
		"wide"	 			"260"
		"tall"				"12"
		"textAlignment"		"north-west"
	}

	// chat input line. hardcoded: 'ypos', 'tall'. these are calculated with values defined in "chatscheme.res" fonts->Default
	ChatInputLine
	{
		"ControlName"			"EditablePanel"
		"fieldName" 			"ChatInputLine"
		"visible" 				"1"
		"enabled" 				"1"
		"xpos"					"10"
		"ypos"					"195"
		"wide"	 				"260"
		"tall"	 				"2"
		"PaintBackgroundType"	"0"
	}

	// chat filters button. hidden by default because it's buggy
	"ChatFiltersButton"
	{
		"ControlName"		"Button"
		"fieldName"			"ChatFiltersButton"
		"xpos"				"225"
		"ypos"				"2"
		"wide"				"45"
		"tall"				"15"
		"autoResize"		"1"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"0"
		"tabPosition"		"0"
		"labelText"			"#chat_filterbutton"
		"textAlignment"		"center"
		"dulltext"			"0"
		"brighttext"		"0"
		"Default"			"0"		
	}

	// chat history. hard coded: 'tall'
	"HudChatHistory"
	{
		"ControlName"		"RichText"
		"fieldName"			"HudChatHistory"
		"xpos"				"0"
		"ypos"				"0"
		"wide"	 			"280"	[$WIN32]
		"tall"				"0"	[$WIN32]
		"wrap"				"1"
		"autoResize"		"0"
		"pinCorner"			"1"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			""
		"textAlignment"		"south-west"
		"font"				"ChatFont"
		"maxchars"			"-1"
	}
}
