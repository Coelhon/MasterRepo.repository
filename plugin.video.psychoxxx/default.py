# -*- coding: utf-8 -*-

import urlparse,sys,re

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

content = params.get('content')

name = params.get('name')

url = params.get('url')

image = params.get('image')

fanart = params.get('fanart')


if action == None:
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().root()

elif action == 'directory':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().youtube(url, action)

elif action == 'play':
    from resources.lib.indexers import jizzplanet
    jizzplanet.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import jizzplanet
    jizzplanet.resolver().browser(url)

elif action == 'search':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().search()

elif action == 'addSearch':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().addSearch(url)

elif action == 'delSearch':
    from resources.lib.indexers import jizzplanet
    jizzplanet.indexer().delSearch()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache':
    from resources.lib.modules import cache
    cache.clear()


