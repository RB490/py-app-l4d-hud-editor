"Resource/UI/HUD/VoteHud.res"
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
			"labelText"		"%passedresult%"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"wrap"			"1"
			"fgcolor_override"	"255 255 255 255"
			"noshortcutsyntax" "1"
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
		
		"NotEnoughVotes"
		{
			"ControlName"	"Label"
			"fieldName"		"NotEnoughVotes"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_not_enough_votes"
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
		"visible"		"1"		//0
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
		
		"Header"
		{
			"ControlName"	"Label"
			"fieldName"		"Header"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"20"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"VOTE:"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic18"
			"wrap"			"0"
			"fgcolor_override"	"128 128 128 255"
			"bgcolor_override"		"0 0 0 0"
		}
		
		"CustomHeader"
		{
			"ControlName"	"Label"
			"fieldName"		"CustomHeader"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"160" 
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"VOTE:"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic18"
			"wrap"			"0"
			"fgcolor_override"	"128 128 128 255"
			"bgcolor_override"		"0 0 0 0"
		}
		
		"HeaderCaller"
		{
			"ControlName"	"Label"
			"fieldName"		"HeaderCaller"
			"xpos"			"3"
			"ypos"			"115"
			"wide"			"160" 
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		""	//blank
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothicShadow12"
			"wrap"			"1"
			"fgcolor_override"	"128 128 128 255"
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
			"labelText"		"%voteissue%"	// Change All Talk to Off? (majority for any team required)
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"0 0 0 0"
			"wrap"			"1"
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
	
	"CallVoteFailed"	//you cannot cast a new vote so soon after the last
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"CallVoteFailed"
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
		
		"FailedReason"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedReason"
			"xpos"			"5"
			"ypos"			"20"
			"wide"			"160" 
			"tall"			"30"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_no_vote_spam"
			"textAlignment"	"west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"TradeGothic12"
			"wrap"			"1"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"0 0 0 0"
		}		
	}
}
