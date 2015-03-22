#-*- condig: utf=8 -*-
__author__ = 'wangqiang'


import urllib
import urllib2
import json
from Entity import wsqmodel

def callWsqAndParse(conf, start=0):
    if conf is None:
        return None

    param = {
        'appToken': conf['appToken'],
        'sId': conf['sId'],
        'sort': conf['sort'],
        'start': start
    }

    result = {}
    try:
        encParam = urllib.urlencode(param)
        wsqUrl = conf['urlPrefix'] + encParam

        response = urllib2.urlopen(wsqUrl, timeout=float(conf['timeout']))
        text = response.read()
        jsonDict = json.loads(text)

        result['errCode'] = jsonDict['errCode']
        if result['errCode'] == 0 and jsonDict.has_key('data'):
            result['next'] = jsonDict['data']['next']
            result['total'] = jsonDict['data']['total']
            if len(jsonDict['data']['threads']) > 0:
                wsqThreadList = []
                for wsqt in jsonDict['data']['threads']:
                    wsqThreadList.append(wsqmodel.WsqThread(wsqt))

                result['threads'] = wsqThreadList
        else:
            result['next'] = start
    except Exception:
        print Exception.message

    return result