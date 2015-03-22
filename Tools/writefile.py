# -*- coding: utf-8 -*-
__author__ = 'wangqiang'

import codecs
import time


def writeFinished(sId, next):
    fileName = 's' + str(sId) + '.finished'
    fp = open(fileName, 'w')
    fp.write(str(next))
    fp.flush()
    fp.close()


def replaceLogPart(value):
    if value is None:
        return ''
    else:
        value = value.replace(' ', '')
        value = value.replace('\n\r', '')
        value = value.replace('\n', '')
        value = value.replace('\t', '')
        return value


def isSelf(sUid, uid):
    if sUid == uid:
        return 'Y'
    else:
        return 'N'


def parseTime(ctime):
    timeArray = time.localtime(ctime)
    return time.strftime('%Y-%m-%d_%H:%M:%S', timeArray)


def writeThread(config, wsqThread):
    if config is None or wsqThread is None:
        return

    sId = config['sId']
    sUid = config['sUid']

    fileName = 't' + str(sId) + '.log'
    fp = codecs.open(fileName, 'a', 'utf-8')
    # fp = open(fileName, 'a')
    line = wsqThread.tId + '\t' + parseTime(int(wsqThread.createTime)) + '\t' + wsqThread.threadUrl + '\t' + wsqThread.authorUid + '(' + replaceLogPart(wsqThread.author) + ')' + '\t' + isSelf(sUid, wsqThread.authorUid) + '\t' + wsqThread.rCount + '\t' + replaceLogPart(wsqThread.content)
    fp.write(line + '\n')
    fp.flush()
    fp.close()