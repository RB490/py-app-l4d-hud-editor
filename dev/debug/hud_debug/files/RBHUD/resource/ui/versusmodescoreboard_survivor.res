
"Resource/UI/VersusModeScoreboard_Survivor.res"
{
	"TeamImage"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"TeamImage"
		"xpos"				"0"
		"ypos"				"0"
		"wide"				"18"
		"tall"				"18"
		"scaleImage"		"1"
		"visible"			"1"
		"enabled"			"1"
		"image"				"select_survivors"
		"drawColor"			"180 180 180 64"	[!$ENGLISH]
		"drawColor"			"180 180 180 255"	[$ENGLISH]
		"zpos"				"0"
	}
	"CompletionProgressBar"
	{
		"ControlName"	"CVersusModeLevelProgressBar"
		"fieldName"		"CompletionProgressBar"
		"xpos"			"18"
		"ypos"			"0"
		"wide"			"300"
		"tall"			"60"
		"zpos"			"1"
		"visible"		"1"
		"enabled"		"1"
		"bar_x"			"0"
		"bar_y"			"1"
		"bar_w"			"110"
		"bar_h"			"2"
		"bar_gap"		"3"
		"skull_size"	"9"
		"skull_y"		"-4"
		"bar_color"					"VersusBrown"
		"bar_localplayer_color"		"VersusSelected"
		"bar_bgcolor"				"255 255 255 1"
	}
	"Category_Completion"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_Completion"
		"xpos"				"0"
		"ypos"				"20"
		"wide"				"100"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#L4D_VSScoreboard_Completion"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_Completion_Score"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_Completion_Score"
		"xpos"				"100"
		"ypos"				"20"
		"wide"				"50"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"0"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_SurvivalBonus"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_SurvivalBonus"
		"xpos"				"0"
		"ypos"				"35"
		"wide"				"100"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"0"
		"labelText"			"#L4D_VSScoreboard_SurvivalBonus"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_SurvivalBonus_Score"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_SurvivalBonus_Score"
		"xpos"				"100"
		"ypos"				"35"
		"wide"				"50"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"	//0
		"enabled"			"1"
		"labelText"			"0"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_DefibPenalty"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_DefibPenalty"
		"xpos"				"0"
		"ypos"				"50"
		"wide"				"100"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"0"
		"labelText"			"Defib Penalty:"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_DefibPenalty_Score"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_DefibPenalty_Score"
		"xpos"				"100"
		"ypos"				"50"
		"wide"				"50"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"		//0
		"enabled"			"1"
		"labelText"			"0"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_Chapter"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_Chapter"
		"xpos"				"0"
		"ypos"				"65"
		"wide"				"100"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"#L4D_vs_TotalScore"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	"Category_Chapter_Score"
	{
		"ControlName"		"Label"
		"fieldName"			"Category_Chapter_Score"
		"xpos"				"100"
		"ypos"				"65"
		"wide"				"50"
		"tall"				"15"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"0"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		"bgcolor_override"	"blank"
	}
	
	
	"DividerHorizontal"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"DividerHorizontal"
		"xpos"				"100"
		"ypos"				"78"
		"wide"				"30"
		"tall"				"1"
		"scaleImage"		"1"
		"visible"			"0"
		"enabled"			"1"
		"fillcolor" 		"145 145 145 255"
		"zpos"				"0"
	}
}