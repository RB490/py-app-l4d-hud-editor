// Infected spawn hud
"Resource/UI/HudGhostPanel.res"
{
	Ready
	{
		"fieldname"      "Ready"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "0"
		"ypos"           "0"
		"zpos"           "1"
		"wide"           "400"
		"tall"           "15"
		"font"           "Cerbetica14Shadow"
		"labelText"      "%ready%"
		"textAlignment"  "center"
		"wrap"           "0"
		"border"		"noborder"
	}

	Info
	{
		"fieldname"      "Info"
		"controlName"    "Label"
		"visible"        "1"
		"enabled"        "1"
		"xpos"           "0"
		"ypos"           "15"
		"zpos"           "1"
		"wide"           "400"
		"tall"           "15"
		"font"           "Cerbetica10Shadow"
		"labelText"      "%info%"
		"textAlignment"  "center"
		"wrap"           "0"
		"bgcolor_override"		"blank"
		"border"				"noborder"
	}

	SpawnBind
	{
		"fieldname"    "SpawnBind"
		"controlName"  "CBindPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "184"
		"ypos"         "20"
		"zpos"         "2"
		"border"		"noborder"
	}

	SpawnLabel
	{
		"fieldname"         "SpawnLabel"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "100"
		"ypos"              "60"
		"zpos"              "1"
		"wide"              "230"
		"tall"              "25"
		"fgcolor_override"  "200 200 200 0"
		"font"              "Cerbetica14Shadow"
		"labelText"         "#L4D_Zombie_UI_Press_Fire_To_Play"
		"textAlignment"     "west"
		"wrap"              "0"
		"border"		"noborder"
	}
	
	
	
	
	
	
	
	
	
	
	ClassImage
	{
		"fieldname"    "ClassImage"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "22"
		"ypos"         "3099"
		"zpos"         "1"
		"wide"         "78"
		"tall"         "78"
		"image"        "tip_boomer"
		"scaleImage"   "1"
		"border"		"noborder"
		"iconcolor"		"255 255 255 125"
	}

	ClassName
	{
		"fieldname"      "ClassName"
		"controlName"    "Label"
		"visible"        "0"
		"enabled"        "1"
		"xpos"           "0"
		"ypos"           "0"
		"zpos"           "1"
		"wide"           "200"
		"tall"           "15"
		"font"           "Cerbetica18Shadow"
		"labelText"      "%classname%"
		"textAlignment"  "West"
		"wrap"           "0"
		"border"		"noborder"
		"fgcolor_override"	"255 255 255 255"
	}
	
	SelectSpawn
	{
		"fieldname"      "SelectSpawn"
		"controlName"    "Label"
		"visible"        "0"
		"enabled"        "0"
		"xpos"           "105"
		"ypos"           "53"
		"zpos"           "1"
		"wide"           "230"
		"tall"           "15"
		"font"           "Cerbetica10Shadow"
		"labelText"      "#L4D_spawn_select_mode_title"
		"textAlignment"  "west"
		"wrap"           "0"
		"border"		"noborder"
	}
}
