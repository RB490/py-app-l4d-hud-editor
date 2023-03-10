
"Resource/UI/ZombiePanel.res"
{
	"TooFarFromSurvivors"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"TooFarFromSurvivors"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"1"
		"wide"			"f0"
		"tall"			"155" [$WIN32]
		"visible"		"0"
		"enabled"		"1"
		"bgcolor_override"	"blank"
		"TooFarTitle"
		{
			"ControlName"	"Label"
			"fieldName"		"TooFarTitle"
			"xpos"			"0"
			"ypos"			"20"
			"zpos"			"100"
			"wide"			"f0"
			"tall"			"20" [$WIN32]
			"visible"		"1"
			"enabled"		"1"
			"textAlignment"	"center"
			"labelText"		"#L4D_Zombie_UI_Too_Far"
			"font"				"TradeGothicShadow20"
			"bgcolor_override"	"blank"
			"wrap"			"0"
		}
		"TooFarText"
		{
			"ControlName"	"Label"
			"fieldName"		"TooFarText"
			"zpos"			"1"
			"xpos"			"c-50" 
			"ypos"			"40" 
			"tall"			"20"
			"wide"			"f0"
			"visible"		"1"
			"enabled"		"1"
			"textAlignment"	"west"	
			"labelText"		"#L4D_Zombie_UI_To_Be_Moved"
			"font"				"TradeGothicShadow15" [$WIN32]
			"wrap"			"1"
		}	
		"SurvivorsImage"
		{
			"ControlName"	"CIconPanel"
			"fieldName"		"SurvivorsImage"
			"xpos"			"c-25"
			"ypos"			"70"
			"zpos"			"1"
			"wide"			"50"
			"tall"			"50"
			"visible"		"0"
			"enabled"		"1"
			"scaleImage"	"1"
			"image"			"tip_crouch"
		}
		"UseBind"
		{
			"ControlName"	"CBindPanel"
			"fieldName"		"UseBind"
			"xpos"			"c-82"
			"ypos"			"38" [$WIN32]
			"zpos"			"1"
			"visible"		"1"
			"enabled"		"1"
		}
		"BackgroundImage"
	    {
		    "ControlName"	"ScalableImagePanel"
		    "fieldName"		"BackgroundImage"
		    "xpos"			"99999"
		    "ypos"			"29"
		    "wide"			"319"
		    "tall"			"80"		
		    "visible"		"0"
		    "enabled"		"0"
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
		    "xpos"				"99999"
		    "ypos"				"29"
		    "wide"				"319"
		    "tall"				"80"
		    "scaleImage"		"1"
		    "visible"			"0"
		    "enabled"			"0"
		    "fillcolor" 		"0 0 0 235"
		    "zpos"				"-2"
	    }
	}
	"TankTakeover"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"TankTakeover"
		"xpos"			"0"
		"ypos"			"0"
		"zpos"			"1"
		"wide"			"f0"
		"tall"			"155" [$WIN32]
		"visible"		"0"
		"enabled"		"1"
		"Title"
		{
			"ControlName"	"Label"
			"fieldName"		"Title"
			"xpos"			"0"
			"ypos"			"20"
			"zpos"			"100"
			"wide"			"f0"
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"textAlignment"	"center"
			"labelText"		"%tanktitle%"
			"font"				"TradeGothicShadow20"
			"bgcolor_override"	"blank"
			"wrap"			"0"
		}
		"Text"
		{
			"ControlName"	"Label"
			"fieldName"		"Text"
			"xpos"			"0"
			"ypos"			"40"
			"zpos"			"100"
			"wide"			"f0"
			"tall"			"20"
			"visible"		"1"
			"enabled"		"1"
			"textAlignment"	"center"
			"labelText"		"%tanktext%"
			"font"				"TradeGothicShadow15" [$WIN32]
			"bgcolor_override"	"blank"
			"wrap"			"0"
		}
		"TankImage"
		{
			"ControlName"	"CIconPanel"
			"fieldName"		"TankImage"
			"xpos"			"c-25"
			"ypos"			"60"
			"zpos"			"1"
			"wide"			"50"
			"tall"			"50"
			"visible"		"0"
			"enabled"		"1"
			"scaleImage"	"1"
			"icon"			"tip_tank_incap"
		}
		"BackgroundImage"
	    {
		    "ControlName"	"ScalableImagePanel"
		    "fieldName"		"BackgroundImage"
		    "xpos"			"99999"
		    "ypos"			"29"
		    "wide"			"319"
		    "tall"			"80"		
		    "visible"		"0"
		    "enabled"		"0"
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
		    "xpos"				"99999"
		    "ypos"				"29"
		    "wide"				"319"
		    "tall"				"80"
		    "visible"		"0"
		    "enabled"		"0"
		    "enabled"			"1"
		    "fillcolor" 		"0 0 0 235"
		    "zpos"				"-2"
	    }
	}
}