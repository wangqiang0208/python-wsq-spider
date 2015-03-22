__author__ = 'wangqiang'

import time

class WsqReply():
    def __init__(self, dict):
        self.tId = self.__assign__(dict, 'tId')
        self.pId = self.__assign__(dict, 'pId')
        self.content = self.__assign__(dict, 'content')
        self.author = self.__assign__(dict, 'author')
        self.authorUid = self.__assign__(dict, 'authorUid')
        self.createTime = self.__assign__(dict, 'createTime')
        self.replys = None

    def __assign__(self, dict, key):
        if dict is not None and key is not None and dict.has_key(key):
            return str(dict.get(key))
        else:
            return ''

    def setReplys(self, replyList):
        self.replys = replyList


class WsqThread():
    def __init__(self, dict):
        self.sId = self.__assign__(dict, 'sId')
        self.tId = self.__assign__(dict, 'tId')
        self.threadUrl = self.__assign__(dict, 'threadUrl')
        self.content = self.__assign__(dict, 'content')
        self.author = self.__assign__(dict, 'author')
        self.authorUid = self.__assign__(dict, 'authorUid')
        self.rCount = self.__assign__(dict, 'rCount')
        self.createTime = self.__assign__(dict, 'createTime')
        self.hasPic = self.__assign__(dict, 'hasPic')
        self.picNum = self.__assign__(dict, 'picNum')

    def __assign__(self, dict, key):
        if dict is not None and key is not None and dict.has_key(key):
            if isinstance(dict.get(key), unicode):
                return dict.get(key)
            else:
                return str(dict.get(key))
        else:
            return ''


if __name__ == '__main__':

    timeArray = time.localtime(1426477157)
    print time.strftime('%Y-%m-%d_%H:%M:%S', timeArray)