# -*- coding: utf-8 -*-
#------------------------------------------------------------
# frenchi
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.frenchi'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan001 = 'special://home/addons/plugin.video.frenchi/resources/fan001.jpg'
icon001 = 'special://home/addons/plugin.video.frenchi/resources/icon001.png'
icon002 = 'special://home/addons/plugin.video.frenchi/resources/icon002.png'
icon003 = 'special://home/addons/plugin.video.frenchi/resources/icon003.png'
icon005 = 'special://home/addons/plugin.video.frenchi/resources/icon005.png'
icon006 = 'special://home/addons/plugin.video.frenchi/resources/icon006.png'
icon009 = 'special://home/addons/plugin.video.frenchi/resources/icon009.png'
icon011 = 'special://home/addons/plugin.video.frenchi/resources/icon011.png'
icon012 = 'special://home/addons/plugin.video.frenchi/resources/icon012.png'
icon014 = 'special://home/addons/plugin.video.frenchi/resources/icon014.png'
icon015 = 'special://home/addons/plugin.video.frenchi/resources/icon015.png'
icon016 = 'special://home/addons/plugin.video.frenchi/resources/icon016.png'
icon017 = 'special://home/addons/plugin.video.frenchi/resources/icon017.png'
icon018 = 'special://home/addons/plugin.video.frenchi/resources/icon018.png'
icon019 = 'special://home/addons/plugin.video.frenchi/resources/icon019.png'
icon020 = 'special://home/addons/plugin.video.frenchi/resources/icon020.png'
icon021 = 'special://home/addons/plugin.video.frenchi/resources/icon021.png'
icon026 = 'special://home/addons/plugin.video.frenchi/resources/icon026.png'



def run():
    plugintools.log("frenchi.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("frenchi ===> " + repr(params))
	plugintools.add_item(title = "Angry Birds", url = base + "channel/UCYC2wjLop-S6Ld4raeoUVNA/", thumbnail = icon001, fanart = fan001, folder = True)
	plugintools.add_item(title = "Ruca [PT]", url = base + "channel/UCd9Tr90LbFouCtIv5FpXTWQ/", thumbnail = icon002, fanart = fan001, folder = True)
	plugintools.add_item(title = "Aventuras de Max[BR]", url = base + "user/AventurasMaxBrasil/", thumbnail = icon003, fanart = fan001, folder = True)
	plugintools.add_item(title = "Noddy [PT]", url = base + "channel/UCbJ3FpU6NZ4T4Ca_BxXtaGA/", thumbnail = icon005, fanart = fan001, folder = True)	
	plugintools.add_item(title = "Pocoyo [PT]", url = base + "user/childrenvideos/", thumbnail = icon006, fanart = fan001, folder = True)
	plugintools.add_item(title = "Herois da Cidade [PT]", url = base + "channel/UCnfjtca0KeZND5e27IO4INg/", thumbnail = icon009, fanart = fan001, folder = True)
	plugintools.add_item(title = "Thomas e Amigos [BR]", url = base + "user/ThomaseSeusAmigos/", thumbnail = icon011, fanart = fan001, folder = True)
	plugintools.add_item(title = "Ovelha Choné", url = base + "channel/UCS7H8U-n5mINVJjJsaRtGHg/", thumbnail = icon012, fanart = fan001, folder = True)
	plugintools.add_item(title = "Panda e os Caricas [PT]", url = base + "channel/UCvw-R-r3p6Hc-yj1qyoPslQ/", thumbnail = icon014, fanart = fan001, folder = True)
	plugintools.add_item(title = "Xana Toc Toc [PT]", url = base + "user/XanaTocTocVEVO/", thumbnail = icon015, fanart = fan001, folder = True)
	plugintools.add_item(title = "Violeta [BR]", url = base + "channel/UCHcZNkHd-6DEjUNxw3grEbA/", thumbnail = icon016, fanart = fan001, folder = True)
	plugintools.add_item(title = "Turma da Mónica [BR]", url = base + "user/turmadamonicaTV/", thumbnail = icon017, fanart = fan001, folder = True)
	plugintools.add_item(title = "Charlie Brown [BR]", url = base + "user/fabio44825/", thumbnail = icon018, fanart = fan001, folder = True)
	plugintools.add_item(title = "Daniel Tigre [BR]", url = base + "channel/UC0uzSknyMFmFV6YrKyglYfQ/", thumbnail = icon019, fanart = fan001, folder = True)
	plugintools.add_item(title = "Masha e o Urso [BR]", url = base + "channel/UCJKBSfD5JSUxGhriFeoPCCg/", thumbnail = icon020, fanart = fan001, folder = True)
	plugintools.add_item(title = "Jelly Jamm [BR]"  , url = base + "user/JellyJammPortugues/", thumbnail = icon021, fanart = fan001, folder = True)
	plugintools.add_item(title = "Dartacao [PT]", url = base + "channel/UCXDon77XvV3nYTYkZNIvnEA/", thumbnail = icon026, fanart = fan001, folder = True)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
