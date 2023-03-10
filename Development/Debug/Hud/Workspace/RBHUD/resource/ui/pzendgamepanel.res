"Resource/UI/PZEndGamePanel.res"
{
	"VotePassed"	// vote sucess
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VotePassed"
		"xpos"			"10"
		"ypos"			"10"
		"wide"			"200" 
		"tall"			"67"
		"visible"		"0"	//0
		"enabled"		"1"
		"bgcolor_override"	"0 0 0 0"
		"PaintBackgroundType"	"2" // rounded corners
	
		"Background_Main"
		{
			"ControlName"			"ImagePanel"
			"fieldName"				"Background_Main"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"51"
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
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"31"
			"autoResize"			"0"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"fillColor"				"TransparentLightBlack"
			"zpos"					"-5000"
		}
		
		"PassedIcon"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"PassedIcon"
			"xpos"			"3"
			"ypos"			"3"
			"wide"			"15"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"hud/vote_yes"
		}
		
		"PassedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"PassedTitle"
			"xpos"			"22"
			"ypos"			"0"
			"wide"			"145" 
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_vote_passed"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic20"
			"wrap"			"0"
			"bgcolor_override"	"0 0 0 0"
		}
		
		"PassedResult"
		{
			"ControlName"	"Label"
			"fieldName"		"PassedResult"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_again_won"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"wrap"			"1"
			"fgcolor_override"	"255 255 255 255"
			"noshortcutsyntax" "1"
		}		
	}
	
	"VoteWait"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VoteWait"
		"xpos"			"10"
		"ypos"			"10"
		"wide"			"220" 
		"tall"			"67" 
		"visible"		"0"		//0
		"enabled"		"1"
		"bgcolor_override"	"0 0 0 0"
		"PaintBackgroundType"	"2" // rounded corners
		
		"Background_Main"
		{
			"ControlName"			"ImagePanel"
			"fieldName"				"Background_Main"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"51"
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
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"31"
			"autoResize"			"0"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"fillColor"				"TransparentLightBlack"
			"zpos"					"-5000"
		}
		
		"PassedIcon"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"PassedIcon"
			"xpos"			"3"
			"ypos"			"3"
			"wide"			"15"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"hud/vote_yes"
		}
		
		"PassedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"PassedTitle"
			"xpos"			"22"
			"ypos"			"0"
			"wide"			"145" 
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_team_again"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic20"
			"wrap"			"0"
			"fgcolor_override"	"200 30 30 255"
			"bgcolor_override"	"0 0 0 0"
		}
		
		"FailedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedTitle"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_team_return"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"wrap"			"1"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"0 0 0 0"
		}
		"WaitTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"WaitTitle"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_waiting"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"wrap"			"1"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"0 0 0 0"
		}		
	}	
	
	"VoteFailed"	//vote failed
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VoteFailed"
		"xpos"			"10"
		"ypos"			"10"
		"wide"			"200" 
		"tall"			"67"
		"visible"		"0"		//0
		"enabled"		"1"
		"bgcolor_override"	"0 0 0 0"
		"PaintBackgroundType"	"2" // rounded corners
		
		"Background_Main"
		{
			"ControlName"			"ImagePanel"
			"fieldName"				"Background_Main"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"51"
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
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"31"
			"autoResize"			"0"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"fillColor"				"TransparentLightBlack"
			"zpos"					"-5000"
		}
		
		"FailedIcon"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"FailedIcon"
			"xpos"			"3"
			"ypos"			"3"
			"wide"			"15"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"hud/vote_no"
		}
		
		"FailedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedTitle"
			"xpos"			"22"
			"ypos"			"0"
			"wide"			"145" 
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_vote_failed"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic20"
			"wrap"			"0"
			"fgcolor_override"	"200 30 30 255"
			"bgcolor_override"	"0 0 0 0"
		}
		
		"FailedResult"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedResult"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_return_won"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"wrap"			"1"
			"fgcolor_override"	"255 255 255 255"
		}		
	}
	
	"VoteActive"	// vote window
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VoteActive"
		"xpos"			"10"
		"ypos"			"10"
		"wide"			"200" 
		"tall"			"140"
		"visible"		"0"		//0
		"enabled"		"1"
		"PaintBackgroundType"	"2" // rounded corners
		"bgcolor_override"	"0 0 0 0"		//VoteActive_background_main
		
		"Background_Main"
		{
			"ControlName"			"ImagePanel"
			"fieldName"				"Background_Main"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"116"
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
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"96"
			"autoResize"			"0"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"fillColor"				"TransparentLightBlack"
			"zpos"					"-5000"
		}
		
		"Background_Two"
		{
			"ControlName"			"ImagePanel"
			"fieldName"				"Background_Two"
			"xpos"			"0"
			"ypos"			"50"
			"wide"			"160" 
			"tall"			"40"
			"autoResize"			"0"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"fillColor"				"TransparentLightBlack"
			"zpos"					"-5000"
		}
		
		"EndGameTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"EndGameTitle"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"textAlignment"		"center"	
			"labelText"		"#L4D_vote_endgame_title"
			"font"			"TradeGothic18"
			"wrap"			"0"
			"fgcolor_override"	"128 128 128 255"
			"bgcolor_override"		"0 0 0 0"
		}
		
		"Issue"
		{
			"ControlName"	"Label"
			"fieldName"		"Issue"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"150" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_text"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"0 0 0 0"
			"wrap"			"0"
			"noshortcutsyntax" "1"
		}
		
		// divider
		"Divider"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"Divider"
			"xpos"			"10"
			"ypos"			"55"
			"wide"			"180" 
			"tall"			"1"
			"fillcolor"		"0 0 0 0"
			"zpos"			"0"
		}
		
		// yes legend
		
		"YesBackground_Selected"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"YesBackground_Selected"
			"xpos"			"5"
			"ypos"			"55"
			"zpos"			"-1"
			"wide"			"150" 
			"tall"			"15"
			"zpos"			"1"
			"fillcolor"		"0 64 0 255"
			"zpos"			"0"
			"visible"		"1"
		}
		
		"YesPCLabel"	[$WIN32]
		{
			"ControlName"	"Label"
			"fieldName"		"YesPCLabel"
			"xpos"			"5"
			"ypos"			"55"
			"wide"			"150" 
			"tall"			"15"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_yes_pc_instruction"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"fgcolor_override"	"255 255 255 255"
		}
		
		"NoBackground_Selected"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"NoBackground_Selected"
			"xpos"			"5"
			"ypos"			"70"
			"zpos"			"-1"
			"wide"			"150" 
			"tall"			"15"
			"zpos"			"1"
			"fillcolor"		"64 0 0 255"
			"zpos"			"0"
			"visible"		"1"
		}
		
		"NoPCLabel"	[$WIN32]
		{
			"ControlName"	"Label"
			"fieldName"		"NoPCLabel"
			"xpos"			"5"
			"ypos"			"70"
			"wide"			"150" 
			"tall"			"15"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_no_pc_instruction"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"fgcolor_override"	"255 255 255 255"
		}
		
		// divider
		"Divider2"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"Divider2"
			"xpos"			"10"
			"ypos"			"95"
			"wide"			"180" 
			"tall"			"1"
			"fillcolor"		"0 0 0 0"
			"zpos"			"0"
		}
		
		"VoteCountLabel"
		{
			"ControlName"	"Label"
			"fieldName"		"VoteCountLabel"
			"xpos"			"10"
			"ypos"			"97"
			"wide"			"190" 
			"tall"			"20"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"#L4D_vote_current_vote_count"
			"textAlignment"	"north-west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"128 128 128 255"
		}
		
		// vote bar
		"VoteBar"
		{
			"ControlName"	"Panel"
			"fieldName"		"VoteBar"
			"xpos"			"6"
			"ypos"			"95"
			"wide"			"160" 
			"tall"			"18"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"			
			"box_size"		"16"
			"spacer"		"6"
			"box_inset"		"0"
			"yes_texture"	"vgui/hud/vote_yes"
			"no_texture"	"vgui/hud/vote_no"			
		}			
	}
	
	
	
	// NOT USED ////////////////////////////////////////////////////////
	
	"BackgroundImage"
	{
	    "ControlName"	"ScalableImagePanel"
	    "fieldName"		"BackgroundImage"
	    "xpos"		"20"
	    "ypos"		"30"
	    "wide"		"329"	[!$ENGLISH]
	    "wide"		"319"	[$ENGLISH]
	    "tall"		"120"		
	    "visible"		"0"
	    "enabled"		"1"
	    "scaleImage"	"1"	
	    "image"			"../vgui/hud/ScalablePanel_bgBlack50_outlineGrey"
	    "drawcolor"		"255 64 64 255"
	    "src_corner_height"		"16"			// pixels inside the image
	    "src_corner_width"		"16"
	    "draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
	    "draw_corner_height" 	"3"	
	}

	
	"BackgroundFill"
	{
	    "ControlName"		"ImagePanel"
	    "fieldName"			"BackgroundFill"
	    "xpos"			"20"
	    "ypos"			"30"
	    "wide"			"329"	[!$ENGLISH]
	    "wide"			"319"	[$ENGLISH]
	    "tall"			"120"
	    "scaleImage"		"1"
	    "visible"			"0"
	    "enabled"			"1"
	    "fillcolor" 		"0 0 0 235"
	    "zpos"				"-2"
	}
	
	"Splatter1"
	{
	    "ControlName"		"ImagePanel"
	    "fieldName"			"Splatter1"
	    "xpos"				"0"
	    "ypos"				"10"
	    "wide"				"100"
	    "tall"				"60"
	    "scaleImage"		"1"
	    "visible"			"1"
	    "enabled"			"1"
	    "image"				"../vgui/hud/splatter1"
	    "drawColor"			"64 64 64 255"
	    "zpos"				"-3"
	}
	
	"Splatter3"
	{
	    "ControlName"		"ImagePanel"
	    "fieldName"			"Splatter3"
	    "xpos"				"36"
	    "ypos"				"55"
	    "wide"				"80"
	    "tall"				"80"
	    "scaleImage"		"1"
	    "visible"			"1"
	    "enabled"			"1"
	    "image"				"../vgui/hud/splatter3"
	    "drawColor"			"64 64 64 255"
	    "zpos"				"-3"
	}
	
	"Splatter4"
	{
	    "ControlName"		"ImagePanel"
	    "fieldName"			"Splatter4"
	    "xpos"				"276"
	    "ypos"				"-6"
	    "wide"				"80"
	    "tall"				"80"
	    "scaleImage"		"1"
	    "visible"			"1"
	    "enabled"			"1"
	    "image"				"../vgui/hud/splatter_corner_upper_right"
	    "drawColor"			"64 64 64 255"
	    "zpos"				"-3"
	}
	
	"Splatter6"
	{
	    "ControlName"		"ImagePanel"
	    "fieldName"			"Splatter6"
	    "xpos"				"190"
	    "ypos"				"150"
	    "wide"				"110"
	    "tall"				"30"
	    "scaleImage"		"1"
	    "visible"			"1"
	    "enabled"			"1"
	    "image"				"../vgui/hud/splatter_horizontal_bottom"
	    "drawColor"			"64 64 64 255"
	    "zpos"				"-3"
	}
	
	
		"TeamVsImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"TeamVsImage"
		"xpos"			"27"
		"ypos"			"643333"
		"zpos"			"20"
		"wide"			"78"
		"tall"			"78"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"../vgui/menu_mode_versus"
	}

	"TeamScavengeImage"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"TeamScavengeImage"
		"xpos"			"27"
		"ypos"			"643333"
		"zpos"			"20"
		"wide"			"78"
		"tall"			"78"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"1"
		"image"			"../vgui/menu_mode_scavenge"
	}
	
			"NoLeftLabel"	[$X360]
		{
			"ControlName"	"Label"
			"fieldName"		"NoLeftLabel"
			"xpos"			"5"
			"ypos"			"46"
			"wide"			"94"
			"tall"			"16"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_no_instruction_a"
			"textAlignment"	"east"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"255 255 255 255"
		}
		
		// no legend
		"NoIcon"	[$X360]
		{
			"ControlName"	"Label"
			"fieldName"		"NoIcon"
			"xpos"			"98"
			"ypos"			"46"
			"wide"			"24"
			"tall"			"16"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"4"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"GameUIButtons"
		}
				
		"NoRightLabel"	[$X360]
		{
			"ControlName"	"Label"
			"fieldName"		"NoRightLabel"
			"xpos"			"122"
			"ypos"			"46"
			"wide"			"125"
			"tall"			"16"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_no_instruction_b"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"255 255 255 255"
		}
		
		
		"YesLeftLabel"	[$X360]
		{
			"ControlName"	"Label"
			"fieldName"		"YesLeftLabel"
			"xpos"			"0"
			"ypos"			"30"
			"wide"			"99"
			"tall"			"16"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_yes_instruction_a"
			"textAlignment"	"east"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"255 255 255 255"
		}
		
		"YesIcon"	[$X360]
		{
			"ControlName"	"Label"
			"fieldName"		"YesIcon"
			"xpos"			"98"
			"ypos"			"30"
			"wide"			"24"
			"tall"			"16"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"5"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"GameUIButtons"
		}
				
		"YesRightLabel"	[$X360]
		{
			"ControlName"	"Label"
			"fieldName"		"YesRightLabel"
			"xpos"			"122"
			"ypos"			"30"
			"wide"			"105"
			"tall"			"16"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4D_vote_yes_instruction_b"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"255 255 255 255"
		}
		
				"SplitscreenPlayer1"
		{
			"ControlName"	"Label"
			"fieldName"		"SplitscreenPlayer1"
			"xpos"			"10"
			"ypos"			"66"
			"wide"			"90"
			"tall"			"12"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_player1"
			"textAlignment"	"north-west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"128 128 128 255"
		}
		
		"SplitscreenPlayer2"
		{
			"ControlName"	"Label"
			"fieldName"		"SplitscreenPlayer2"
			"xpos"			"111"
			"ypos"			"66"
			"wide"			"90"
			"tall"			"12"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"#L4D_vote_endgame_vote_player2"
			"textAlignment"	"north-west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"128 128 128 255"
		}
		
				// divider
		"Divider2"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"Divider2"
			"xpos"			"10"
			"ypos"			"643333"
			"wide"			"202"
			"tall"			"0"
			"fillcolor"		"128 128 128 255"
			"zpos"			"0"
		}
		
				// divider
		"Divider"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"Divider"
			"xpos"			"10"
			"ypos"			"283333"
			"wide"			"202"
			"tall"			"0"
			"fillcolor"		"128 128 128 255"
			"zpos"			"0"
		}
		
				// yes legend
		
		"YesBackground_Selected"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"YesBackground_Selected"
			"xpos"			"10"
			"ypos"			"30"
			"zpos"			"-1"
			"wide"			"202"
			"textAlignment"	"west"
			"tall"			"16"
			"zpos"			"1"
			"fillcolor"		"88 119 140 180"
			"zpos"			"0"
			"visible"		"0"
		}
		
		"YesPCLabel"	[$WIN32]
		{
			"ControlName"	"Label"
			"fieldName"		"YesPCLabel"
			"xpos"			"5"
			"ypos"			"45"
			"wide"			"210"
			"tall"			"15"
			"zpos"			"2"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"#L4D_vote_yes_pc_instruction"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"255 255 255 255"
		}
		
		"NoBackground_Selected"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"NoBackground_Selected"
			"xpos"			"10"
			"ypos"			"46"
			"zpos"			"-1"
			"wide"			"202"
			"tall"			"16"
			"zpos"			"1"
			"fillcolor"		"88 119 140 180"
			"zpos"			"0"
			"visible"		"0"
		}
		
		"NoPCLabel"	[$WIN32]
		{
			"ControlName"	"Label"
			"fieldName"		"NoPCLabel"
			"xpos"			"5"
			"ypos"			"50"
			"wide"			"210"
			"tall"			"15"
			"zpos"			"2"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"#L4D_vote_no_pc_instruction"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"255 255 255 255"
		}
		
		"VoteCountLabel"
		{
			"ControlName"	"Label"
			"fieldName"		"VoteCountLabel"
			"xpos"			"669999"
			"ypos"			"669999"
			"wide"			"210"
			"tall"			"12"
			"visible"		"0"
			"enabled"		"0"
			"labelText"		"#L4D_vote_current_vote_count"
			"textAlignment"	"north-west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"DefaultMedium"
			"fgcolor_override"	"128 128 128 255"
		}
}
