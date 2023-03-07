#include <sourcemod>
#include <sdktools>
#include <l4d_myStocks>

#pragma newdecls required
#pragma semicolon 1

public Plugin myinfo = {
	name 			= "Character Voice Pitch",
	author 			= "RB",
	description 	= "Change pitch or mute",
	version 		= "1.0",
	url 			= "http://www.sourcemod.net/"
};

static	int		g_iClientPitch[MAXPLAYERS+1];
static	bool	g_bIsMuted[MAXPLAYERS+1] = false;
static	bool	g_bIsTF;
static	bool	g_bIsCSS;
static	bool	g_bIsL4D;

public void OnPluginStart() {
	RegAdminCmd( "sm_setpitch", Command_SetPitch, ADMFLAG_GENERIC );
	RegAdminCmd( "sm_setmute", Command_SetMute, ADMFLAG_GENERIC );
	
	AddNormalSoundHook( NormalSoundHook );
	
	char strGameDir[16];
	GetGameFolderName( strGameDir, sizeof(strGameDir) );
	g_bIsTF = strcmp( strGameDir, "tf", false ) == 0 || strcmp( strGameDir, "tf_beta", false ) == 0;
	g_bIsCSS = strcmp( strGameDir, "cstrike", false ) == 0 || strcmp( strGameDir, "cstrike_beta", false ) == 0;
	g_bIsL4D = strcmp( strGameDir, "left4dead", false ) == 0 || strcmp( strGameDir, "left4dead2", false ) == 0;
	
	for( int i = 0; i <= MAXPLAYERS; i++ )
		ResetData( i );
}

public void OnClientDisconnect( int iClient) {
	ResetData( iClient );
}

public Action NormalSoundHook(int iClients[MAXPLAYERS], int &numClients, char strSample[PLATFORM_MAX_PATH], int &iEntity, int &iChannel, float &flVolume, int &iLevel, int &iPitch, int &iFlags, char soundEntry[PLATFORM_MAX_PATH], int &seed)
{
	if( StrContains( strSample, "/footstep", false ) != -1 )
		return Plugin_Continue;
	
	bool bValid = false;
	
	if( IsValidClient( iEntity ) )
	{
		if( g_bIsCSS )
			bValid = StrContains( strSample, "player/death", false ) == 0 || StrContains( strSample, "radio/", false ) == 0 || StrContains( strSample, "bot/", false ) == 0;
		else if( g_bIsTF )
			bValid = StrContains( strSample, "vo/", false ) == 0 || StrContains( strSample, "player/taunt_rockstar", false ) == 0;
		else if( g_bIsL4D )
			bValid = StrContains( strSample, "player\\", false ) == 0 && StrContains( strSample, "\\voice\\", false ) != -1 || StrContains( strSample, "player/", false ) == 0 && StrContains( strSample, "/voice/", false ) != -1;
		else
			bValid = StrContains( strSample, "player/", false ) == 0 || StrContains( strSample, "player\\", false ) == 0;
	}

	// disable microphone spam:
	// else
	// {
	// 	if( g_bIsL4D )
	// 		bValid = StrContains( strSample, "npc/", false ) == 0 || StrContains( strSample, "player\\", false ) == 0 && StrContains( strSample, "\\voice\\", false ) != -1 || StrContains( strSample, "player/", false ) == 0 && StrContains( strSample, "/voice/", false ) != -1;
	// 	//if( !bValid ) PrintToServer( "entity %d > %s", iEntity, strSample );
	// }
	
	if( bValid )
	{
		iPitch = g_iClientPitch[ IsValidClient( iEntity ) ? iEntity : 0 ];
		iFlags |= SND_CHANGEPITCH;
		return Plugin_Changed;
	}
	
	return Plugin_Continue;
}

public Action Command_SetMute( int client, int args )
{	
	if(args < 1)
	{
		PrintToChat(client, "[SM] Usage: sm_setmute <target>");
		return Plugin_Handled;
	}
	char arg[65];
	GetCmdArg(1, arg, sizeof(arg));
	char target_name[MAX_TARGET_LENGTH];
	int target_list[MAXPLAYERS];
	int target_count;
	bool tn_is_ml;
	if ((target_count = ProcessTargetString(arg, client, target_list, MAXPLAYERS, COMMAND_FILTER_ALIVE, target_name, sizeof(target_name), tn_is_ml)) <= 0)
	{
		ReplyToTargetError(client, target_count);
		return Plugin_Handled;
	}
	
	for (int i = 0; i < target_count; i++)
	{
		// get variables
		char targetName[MAX_NAME_LENGTH];
		char adminName[MAX_NAME_LENGTH];
		GetClientName(target_list[i], targetName, sizeof(targetName));
		GetClientName(client, adminName, sizeof(adminName));
		

		// toggle mute
		if(g_bIsMuted[target_list[i]])
		{
			g_iClientPitch[target_list[i]] = 100;
			g_bIsMuted[target_list[i]] = false;
			PrintToChat(client, "[SM] %s Unmuted %s", adminName, targetName);
		}
		else
		{
			g_iClientPitch[target_list[i]] = 256;
			g_bIsMuted[target_list[i]] = true;
			PrintToChat(client, "[SM] %s Muted %s", adminName, targetName);
		}
	}

	return Plugin_Handled;
}

public Action Command_SetPitch( int iClient, int args )
{
	if (args < 2)
	{
		PrintToChat(iClient, "[SM] Usage: sm_setpitch <target> [number]");
		return Plugin_Handled;
	}

	if ( args >= 2 )
	{
		
		char strPitch[8];
		GetCmdArg( 2, strPitch, sizeof(strPitch) );
		int iPitch = StringToInt( strPitch );
		if( iPitch < 5 || iPitch > 255 )
		{
			ReplyToCommand( iClient, "Pitch value %d is out of bounds [5...255]", iPitch );
			return Plugin_Handled;
		}
		
		char strTargets[64];
		GetCmdArg( 1, strTargets, sizeof(strTargets) );
		if( strTargets[0] == '0' )
		{
			g_iClientPitch[0] = iPitch;
		}
		else
		{
			char target_name[MAX_TARGET_LENGTH];
			int iTargets[MAXPLAYERS];
			int nTargets;
			bool tn_is_ml;
			if((nTargets = ProcessTargetString(strTargets, iClient, iTargets, MAXPLAYERS, 0, target_name, sizeof(target_name), tn_is_ml)) <= 0)
			{
				ReplyToTargetError( iClient, nTargets );
				return Plugin_Handled;
			}
			for( int i = 0; i < nTargets; i++ )
				g_iClientPitch[iTargets[i]] = iPitch;
		}
	}
	
	return Plugin_Handled;
}

void ResetData( int iClient )
{
	if( iClient < 0 || iClient > MAXPLAYERS )
		return;
	g_iClientPitch[iClient] = SNDPITCH_NORMAL;
	g_bIsMuted[iClient] = false;
}