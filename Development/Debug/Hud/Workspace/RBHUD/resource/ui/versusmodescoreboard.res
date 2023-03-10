
"Resource/UI/VersusModeScoreboard.res"
{
	"Background_Main"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_Main"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"275"
		"tall"			"130"
		"visible"		"1"
		"enabled"		"1"
		"bgcolor_override"		"TransparentLightBlack"
		"zpos"			"-2"
	}
	"Background_One"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_One"
		"xpos"			"0"
		"ypos"			"20"
		"wide"			"275"
		"tall"			"110"
		"visible"		"1"
		"enabled"		"1"
		"bgcolor_override"		"TransparentLightBlack"
		"zpos"			"-2"
	}
	
	"Background_Two"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_One"
		"xpos"			"0"
		"ypos"			"40"
		"wide"			"275"
		"tall"			"90"
		"visible"		"1"
		"enabled"		"1"
		"bgcolor_override"		"TransparentLightBlack"
		"zpos"			"-2"
	}
	
	"ModeTitle"
	{
		"ControlName"	"Label"
		"fieldName"		"ModeTitle"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"275"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_VSScoreboard_Title"
		"textAlignment"	"center"
		"dulltext"			"0"
		"brighttext"		"0"
		"font"				"TradeGothic18"
		
	}
	"TeamYours"
	{
		"ControlName"	"Label"
		"fieldName"		"TeamYours"
		"xpos"			"5"
		"ypos"			"20"
		"wide"			"125"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"You"	//#L4D_VSScoreboard_YourTeam
		"textAlignment"	"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		
		"bgcolor_override"	"blank"
		
	}
	"TeamEnemy"
	{
		"ControlName"		"Label"
		"fieldName"		"TeamEnemy"
		"xpos"			"140"
		"ypos"			"20"
		"wide"			"125"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"Enemy"	//#L4D_VSScoreboard_EnemyTeam
		"textAlignment"		"west"
		"dulltext"		"1"
		"brighttext"		"0"
		"font"		"TradeGothic14"
		"fgcolor_override"	"MediumGray"
		
		"bgcolor_override"	"blank"
	}
	
	"CampaignScore_Yours_Score"
	{
		"ControlName"	"Label"
		"fieldName"		"CampaignScore_Yours_Score"
		"xpos"			"5"
		"ypos"			"20"
		"wide"			"125"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"0"
		"textAlignment"	"east"
		"dulltext"		"1"
		"brighttext"	"0"
		"font"			"TradeGothic18"
		"fgcolor_override"	"MediumGray"
		
		"bgcolor_override"	"blank"
		
	}

	"CampaignScore_Enemy_Score"
	{
		"ControlName"		"Label"
		"fieldName"			"CampaignScore_Enemy_Score"
		"xpos"			"140"
		"ypos"			"20"
		"wide"			"125"
		"tall"			"20"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"labelText"			"0"
		"textAlignment"		"east"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"TradeGothic18"
		"fgcolor_override"	"MediumGray"
		
		"bgcolor_override"	"blank"
		
	}
	
	"LeftScorePanel"
	{
		"ControlName"		"EditablePanel"
		"fieldName"			"LeftScorePanel"
		"xpos"				"5"
		"ypos"				"45"
		"wide"				"235"
		"tall"				"100"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
	}
	"RightScorePanel"
	{
		"ControlName"		"EditablePanel"
		"fieldName"			"RightScorePanel"
		"xpos"				"140"
		"ypos"				"45"
		"wide"				"235"
		"tall"				"100"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
	}
	"TieBreakerPanel"
	{
		"ControlName"		"EditablePanel"
		"fieldName"			"TieBreakerPanel"
		"xpos"				"c-285"
		"ypos"				"135"
		"wide"				"280"
		"tall"				"150"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"	//0
		"enabled"			"1"
		"tabPosition"		"0"
		"padding"			"4"
		"zpos"				"50"
	}
	
	
	
	
	
	
	"CampaignScoreBackgroundImageLeft"
	{
		"ControlName"	"Panel"
		"fieldName"		"CampaignScoreBackgroundImageLeft"
		"xpos"			"68"
		"ypos"			"147"
		"wide"			"232"
		"tall"			"2"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"
		"bgcolor_override"		"TransparentLightBlack"
		"zpos"			"-2"
		"src_corner_height"		"16"
		"src_corner_width"		"16"
		"draw_corner_width"		"8"
		"draw_corner_height" 	"8"
	}
	
	"CampaignScore_Yours"
	{
		"ControlName"		"Label"
		"fieldName"			"CampaignScore_Yours"
		"xpos"				"64"
		"ypos"				"145"
		"wide"				"190"
		"tall"				"26"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"1"
		"labelText"			"#L4D_vs_CampaignScore_Short"
		"textAlignment"		"east"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"BodyText_medium"
		
	}
	
	"CampaignScore_Enemy"
	{
		"ControlName"		"Label"
		"fieldName"			"CampaignScore_Enemy"
		"xpos"				"240"
		"ypos"				"145"
		"wide"				"190"
		"tall"				"26"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"0"
		"enabled"			"1"
		"labelText"			"#L4D_vs_CampaignScore_Short"
		"textAlignment"		"west"
		"dulltext"			"1"
		"brighttext"		"0"
		"font"				"BodyText_medium"
		
	}
}