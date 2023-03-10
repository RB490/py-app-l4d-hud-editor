"Resource/UI/HUD/VoteHud.res"
{	
	"VotePassed"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VotePassed"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"300"
		"tall"			"50"
		"visible"		"0"
		"enabled"		"1"
		"bgcolor_override"	"0 0 0 0"
		"border"			"noborder"
		"PaintBackgroundType"	"2" // rounded corners
		
		"PassedIcon"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"PassedIcon"
			"xpos"			"70"
			"ypos"			"5"
			"wide"			"14"
			"tall"			"14"
			"visible"		"0"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"hud/vote_yes"
		}
		
		"PassedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"PassedTitle"
			"xpos"			"0"
			"ypos"			"5"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_vote_passed"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica18"
			"wrap"			"0"
			"fgcolor_override"	"255 255 255 255"
		}
		
		"PassedResult"
		{
			"ControlName"	"Label"
			"fieldName"		"PassedResult"
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"%passedresult%"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"wrap"			"0"
			"fgcolor_override"	"215 215 215 255"
			"noshortcutsyntax" "1"
		}		
	}
	
	"VoteFailed"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VoteFailed"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"300"
		"tall"			"50"
		"visible"		"0"
		"enabled"		"1"
		"bgcolor_override"	"0 0 0 00"
		"border"			"noborder"
		"PaintBackgroundType"	"0" // rounded corners
		
		"FailedIcon"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"FailedIcon"
			"xpos"			"80"
			"ypos"			"5"
			"wide"			"14"
			"tall"			"14"
			"visible"		"0"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"hud/vote_no"
		}
		
		"FailedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedTitle"
			"xpos"			"0"
			"ypos"			"5"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_vote_failed"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica18"
			"wrap"			"0"
			"fgcolor_override"	"255 0 0 255"
		}
		
		"NotEnoughVotes"
		{
			"ControlName"	"Label"
			"fieldName"		"NotEnoughVotes"
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_not_enough_votes"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"wrap"			"0"
			"fgcolor_override"	"215 215 215 255"
			"bgcolor_override"	""
		}		
	}
	
	"VoteActive"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"VoteActive"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"250"
		"wide"			"300"
		"tall"			"140"
		"visible"		"0"
		"enabled"		"1"
		"PaintBackgroundType"	"2" // rounded corners
		"bgcolor_override"	"0 0 0 0"
		"border"		"noborder"
		
		"HeaderCaller"
		{
			"ControlName"	"Label"
			"fieldName"		"HeaderCaller"
			"xpos"			"0"
			"ypos"			"0"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		""
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"wrap"			"0"
			"fgcolor_override"	"255 255 255 255"
			"border"		"noborder"
		}
		
		"Issue"
		{
			"ControlName"	"Label"
			"fieldName"		"Issue"
			"xpos"			"0"
			"ypos"			"15"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"%voteissue%"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"fgcolor_override"	"215 215 215 255"
			"wrap"			"0"
			"noshortcutsyntax" "1"
			"border"		"noborder"
		}
		
		// yes legend
		
		"YesBackground_Selected"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"YesBackground_Selected"
			"xpos"			"75"
			"ypos"			"32"
			"zpos"			"-1"
			"wide"			"75"
			"tall"			"15"
			"zpos"			"1"
			"fillcolor"		"ColorTeal"
			"border"		"noborder"
			"zpos"			"0"
			"visible"		"1"
		}
		
		"YesPCLabel"	[$WIN32]
		{
			"ControlName"	"Label"
			"fieldName"		"YesPCLabel"
			"xpos"			"75"
			"ypos"			"32"
			"wide"			"75"
			"tall"			"15"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"F5"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"0 255 128 15"
			"border"		"BlackBorder"
		}
		
		"NoBackground_Selected"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"NoBackground_Selected"
			"xpos"			"155"
			"ypos"			"32"
			"zpos"			"-1"
			"wide"			"75"
			"tall"			"15"
			"zpos"			"1"
			"fillcolor"		"ColorRuby"
			"zpos"			"0"
			"visible"		"1"
		}
		
		"NoPCLabel"	[$WIN32]
		{
			"ControlName"	"Label"
			"fieldName"		"NoPCLabel"
			"xpos"			"155"
			"ypos"			"32"
			"wide"			"75"
			"tall"			"15"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"F6"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"fgcolor_override"	"255 255 255 255"
			"bgcolor_override"	"255 0 128 15"
			"border"		"BlackBorder"
		}
		
		// vote bar
		"VoteBar"
		{
			"ControlName"	"Panel"
			"fieldName"		"VoteBar"
			"xpos"			"75"
			"ypos"			"51"
			"wide"			"180"
			"tall"			"18"
			"zpos"			"2"
			"visible"		"1"
			"enabled"		"1"			
			"box_size"		"15"
			"spacer"		"4"
			"box_inset"		"0"
			"yes_texture"	"vgui/hud/vote_yes"
			"no_texture"	"vgui/hud/vote_no"
			"textAlignment"	"east"
		}	

		"VoteBarBgDebug"
		{
			"ControlName"	"EditablePanel"
			"fieldName"		"VoteBarBgDebug"
			"visible"       "1"
			"enabled"       "1"
			"xpos"			"75"
			"ypos"			"51"
			"wide"			"180"
			"tall"			"15"
			"zpos"			"1"
			"proportionaltoparent"	"1"
			"border"		"noborder"
			"bgcolor_override"	"0 0 0 0"
		}
		
		
		
		
		
		
		
		
		
		
		
		// divider
		"Divider2"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"Divider2"
			"xpos"			"0"
			"ypos"			"75"
			"wide"			"190"
			"tall"			"0"
			"fillcolor"		"0 0 0 255"
			"zpos"			"0"
		}
		// divider
		"Divider"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"Divider"
			"xpos"			"0"
			"ypos"			"50"
			"wide"			"190"
			"tall"			"0"
			"fillcolor"		"0 0 0 255"
			"zpos"			"0"
		}
		"VoteCountLabel" // disabled
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
			"font"			"Cerbetica10"
			"fgcolor_override"	"128 128 128 255"
		}
		"Header" // disabled
		{
			"ControlName"	"Label"
			"fieldName"		"Header"
			"xpos"			"10"
			"ypos"			"5"
			"wide"			"180"
			"tall"			"20"
			"visible"		"0"
			"enabled"		"1"
			"labelText"		"#L4D_vote_header"
			"textAlignment"	"north-west"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica18"
			"wrap"			"1"
			"fgcolor_override"	"128 128 128 255"
			"border"		"noborder"
		}
	}
	
	"CallVoteFailed"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"CallVoteFailed"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"300"
		"tall"			"50"
		"visible"		"0"
		"enabled"		"1"
		"bgcolor_override"	"0 0 0 00"
		"border"			"noborder"
		"PaintBackgroundType"	"0" // rounded corners
		
		"FailedIcon"
		{
			"ControlName"	"ImagePanel"
			"fieldName"		"FailedIcon"
			"xpos"			"5"
			"ypos"			"5"
			"wide"			"14"
			"tall"			"14"
			"visible"		"0"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"hud/vote_no"
		}
		
		"FailedTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedTitle"
			"xpos"			"0"
			"ypos"			"5"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_vote_failed"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica18"
			"wrap"			"0"
			"fgcolor_override"	"255 0 0 255"
		}
		
		"FailedReason"
		{
			"ControlName"	"Label"
			"fieldName"		"FailedReason"
			"xpos"			"0"
			"ypos"			"20"
			"wide"			"300"
			"tall"			"15"
			"visible"		"1"
			"enabled"		"1"
			"labelText"		"#L4d_vote_no_vote_spam"
			"textAlignment"	"center"
			"dulltext"		"0"
			"brighttext"	"0"
			"font"			"Cerbetica10"
			"wrap"			"0"
			"fgcolor_override"	"215 215 215 255"
			"bgcolor_override"	""
		}		
	}
}
