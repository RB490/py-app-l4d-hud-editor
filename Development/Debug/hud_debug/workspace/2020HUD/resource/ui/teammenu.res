"Resource/UI/TeamMenu.res"			//select which side to join, usually when coming from spectator
{
	"team"
	{
		"ControlName"		"CTeamMenu"
		"fieldName"		"team"
		"xpos"			"c-67"
		"ypos"			"c67"
		"wide"			"135"
		"tall"			"135"
		"autoResize"		"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"0"
		"PaintBackgroundType"	"2"
	}
	
    "BackgroundImage"
	{
		"ControlName"	"ScalableImagePanel"
		"fieldName"		"BackgroundImage"
		"xpos"			"0"
		"ypos"			"999"
		"wide"			"135"
		"tall"			"93"		
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"	
		"image"			"../vgui/hud/ScalablePanel_bgBlack"
		"drawcolor"		"255 255 255 255"
		"fgcolor_override"		"255 255 255 255"
		"src_corner_height"		"16"			// pixels inside the image
		"src_corner_width"		"16"
		"draw_corner_width"		"3"				// screen size of the corners ( and sides ), proportional
		"draw_corner_height" 	"3"	
	}

	"HealthBGPanel"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"HealthBGPanel"
		"visible"                       "1"
		"enabled"                       "1"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"135"
		"tall"			"93"	
		"zpos"			"-100"
		"proportionaltoparent"	"1"
		"border"		"BlackBorder"
		"bgcolor_override"	"TransparentLightBlack"
	}

	"FullTitle"
	{
		"ControlName"	"Label"
		"fieldName"		"FullTitle"
		"xpos"			"33"
		"ypos"			"4099"
		"wide"			"420"
		"tall"			"24"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_spectator_select_side"
		"textAlignment"	"north-west"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"Cerbetica18Shadow"
	}

	"NoSwitchTitle"
	{
		"ControlName"	"Label"
		"fieldName"		"NoSwitchTitle"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"135"
		"tall"			"15"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_spectator_cant_change_teams"
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"Cerbetica10Shadow"
		"border"		"noborder"
	}

	"NoSwitchLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"NoSwitchLabel"
		"xpos"			"5"
		"ypos"			"15"
		"wide"			"130"
		"tall"			"50"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"wrap"			"1"
		"labelText"		"#L4D_spectator_select_side"
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"font"			"Cerbetica10Shadow"
		"border"		"noborder"
	}

	"SurvivorBackground"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"SurvivorBackground"
		"xpos"			"5"
		"ypos"			"5"
		"zpos"			"1"
		"wide"			"60"
		"tall"			"60"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"autoResize"	"0"
		"pinCorner"		"0"
		"image"			"select_survivors"
		"zpos"			"-1"
	}
	"SurvivorFullBackground"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"SurvivorFullBackground"
		"xpos"			"5"
		"ypos"			"5"
		"zpos"			"1"
		"wide"			"60"
		"tall"			"60"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"autoResize"	"0"
		"pinCorner"		"0"
		"image"			"select_survivors"
		"drawcolor"		"100 100 100 255"
		"zpos"			"-1"
	}
	"SurvivorButton"
	{
		"ControlName"		"Button"
		"fieldName"		"SurvivorButton"
		"xpos"			"5"
		"ypos"			"5"
		"zpos"			"2"
		"wide"			"60"
		"tall"			"60"
		"autoResize"	"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"2"
		"labelText"		""
		"dulltext"		"0"
		"brighttext"	"0"
		"wrap"			"0"
		"Command"		"survivor"
		"Default"		"0"
		"selected"		"0"		
		"defaultBgColor_override"	"0 0 0 165"
		"armedBgColor_override"		"0 0 0 0"
		"depressedBgColor_override"	"0 0 0 0"	
	}
	"SurvivorFullLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"SurvivorFullLabel"
		"xpos"			"85"
		"ypos"			"69"
		"zpos"			"3"
		"wide"			"95"
		"tall"			"95"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_team_menu_full"
		"textAlignment"	"south"
		"font"			"MenuTitle"
	}

	"InfectedBackground"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"InfectedBackground"
		"xpos"			"70"
		"ypos"			"5"
		"zpos"			"1"
		"wide"			"60"
		"tall"			"60"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"autoResize"	"0"
		"pinCorner"		"0"
		"image"			"select_PZ"
		"zpos"			"-1"
	}
	"InfectedFullBackground"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"InfectedFullBackground"
		"xpos"			"70"
		"ypos"			"5"
		"zpos"			"1"
		"wide"			"60"
		"tall"			"60"
		"visible"		"1"
		"enabled"		"1"
		"scaleImage"	"1"
		"autoResize"	"0"
		"pinCorner"		"0"
		"image"			"select_PZ"
		"drawcolor"		"120 120 120 255"
	}
	"InfectedButton"
	{
		"ControlName"	"Button"
		"fieldName"		"InfectedButton"
		"xpos"			"70"
		"ypos"			"5"
		"zpos"			"2"
		"wide"			"60"
		"tall"			"60"
		"autoResize"	"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"2"
		"labelText"		""
		"dulltext"		"0"
		"brighttext"	"0"
		"wrap"			"0"
		"Command"		"infected"
		"Default"		"0"
		"selected"		"0"
		"defaultBgColor_override"	"0 0 0 165"
		"armedBgColor_override"		"0 0 0 0"
 		"depressedBgColor_override"	"0 0 0 0"
	}
	"InfectedFullLabel"
	{
		"ControlName"		"Label"
		"fieldName"		"InfectedFullLabel"
		"xpos"			"220"
		"ypos"			"69"
		"zpos"			"3"
		"wide"			"95"
		"tall"			"95"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"#L4D_team_menu_full"
		"textAlignment"	"south"
		"font"			"MenuTitle"
	}

	"Cancel"
	{
		"ControlName"		"RoundedButton"
		"fieldName"		"Cancel"
		"xpos"		"5"
		"ypos"		"70"
		"wide"		"125"
		"tall"		"18"
		"zpos"		"100"
		"autoResize"		"1"
		"pinCorner"		"3"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"		"1"
		"labelText"		"#L4D_btn_cancel"
		"textAlignment"		"center"
		"dulltext"		"0"
		"brighttext"		"0"
		"wrap"		"0"
		"Command"		"close"
		"Default"		"0"
		"selected"		"0"		
		"font"			"Cerbetica10"
	}

}