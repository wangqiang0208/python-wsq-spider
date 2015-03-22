#-*- coding: utf=8 -*-
__author__ = 'wangqiang'


import ConfigParser
from optparse import OptionParser
import sys
import os

def getConfig(configFilePath):
    config = parseConfig(configFilePath)

    option_config = parseOption()
    if option_config.id is not None:
        config['sId'] = option_config.id
    if option_config.name is not None:
        config['sName'] = option_config.name
    if option_config.uid is not None:
        config['sUid'] = option_config.uid
    if option_config.start > 0:
        config['start'] = option_config.start
    if option_config.isdev == 1:
        config['isdev'] = 1

    start = parseFinishedFile(config['sId'])
    if start > 0:
        config['start'] = start
    return config


def parseConfig(filepath):
    """
    u解析文件配置
    :param filepath:
    :return:配置字典
    """
    cp = ConfigParser.ConfigParser()
    fp = open(filepath, 'r')
    cp.readfp(fp)

    config = {}
    config['urlPrefix'] = cp.get('common', 'urlPrefix')
    config['appToken'] = cp.get('common', 'appToken')
    config['sort'] = cp.get('common', 'sort')
    config['interval'] = cp.get('common', 'interval')
    config['timeout'] = cp.get('common', 'timeout')
    config['isdev'] = cp.get('common', 'isdev')

    config['sId'] = cp.get('site', 'sId')
    config['sName'] = cp.get('site', 'sName')
    config['sUid'] = cp.get('site', 'sUid')
    config['start'] = cp.get('site', 'start')

    fp.close()
    return config


def parseOption():
    """
    解析命令行参数
    :return:返回解析的参数字典
    """
    parser = OptionParser()
    parser.add_option('-s', '--id', dest='id', type='int', help='give the site id', metavar='12345')
    parser.add_option('-n', '--name', dest='name', type='string', help='give the site name', metavar='测试站点')
    parser.add_option('-u', '--uid', dest='uid', type='string', help='give the site uid', metavar='u123')
    parser.add_option('-f', '--start', dest='start', type='int', help='give the job start', metavar='0', default=0)
    parser.add_option('-d', '--isdev', dest='isdev', type='int', help='give the isdev', metavar='0', default=0)

    (options, sys.argv[1:]) = parser.parse_args()

    return options


def parseFinishedFile(sId):
    """
    解析临时文件配置
    :return:主要读取start位置
    """
    filename = 's' + str(sId) + '.finished'
    if not os.path.exists(filename):
        return 0
    else:
        #try:
        fp = open(filename, 'r')
        result = 0
        content = fp.read()
        if content is None or len(content) == '':
            result = 0
        else:
            result = int(content)
        fp.close()
        return result
        # except Exception:
        #     print Exception.message
        #     return 0