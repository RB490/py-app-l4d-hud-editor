// Dead Center finale gascan hud
"Resource/UI/HUD/HudScavengeProgress.res"
{

	GasCanImage
	{
		"fieldname"    "GasCanImage"
		"controlName"  "CIconPanel"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "56"
		"ypos"         "0"
		"wide"         "15"
		"tall"         "15"
		"icon"         "icon_gas_can"
		"scaleImage"   "1"
		"iconcolor"		"195 195 195 255"
	}

	ItemDigitDivider
	{
		"fieldname"      "ItemsRemainingLabel"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "24"
		"ypos"           "0"
		"wide"           "12"
		"tall"           "15"
		"font"           "Cerbetica18Shadow"
		"labelText"      "/"
		"textAlignment"  "center"
		//"border"			"baseborder"
	}

	ItemsCollectedDigits
	{
		"fieldname"      "ItemsCollectedDigits"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "0"
		"ypos"           "0"
		"zpos"           "1"
		"wide"           "24"
		"tall"           "15"
		"font"           "Cerbetica18Shadow"
		"labelText"      "0"
		"textAlignment"  "east"
		//"border"			"baseborder"
	}

	ItemsGoalDigits
	{
		"fieldname"      "ItemsGoalDigits"
		"controlName"    "Label"
		"visible"        "1"
		"xpos"           "36"
		"ypos"           "0"
		"wide"           "24"
		"tall"           "15"
		"font"           "Cerbetica18Shadow"
		"labelText"      "0"
		"textAlignment"  "west"
		//"border"			"baseborder"
	}
}
