#-*- coding: utf-8 -*-
__author__ = 'wangqiang'


from Tools import *
import time

if __name__ == '__main__':

    config = configparser.getConfig('config.ini')

    print config
    start = int(config['start'])

    while True:
        #sleep some time
        time.sleep(int(config['interval']))
        response = httpexecutor.callWsqAndParse(config, start)
        if response is None or not response.has_key('errCode'):
            print 'response is None'
            continue
        else:
            if str(response.get('errCode', '-1')) != '0':
                continue
            next = response['next']
            total = response['total']
            print '>> finish get threads: sId=%s,next=%d,total=%d' % (config['sId'], next, total)

            #record next
            if next <= start:
                next = start + 10
            start = next
            writefile.writeFinished(config['sId'], next)

            if response.has_key('threads'):
                wsqThreads = response['threads']
                if wsqThreads is not None and len(wsqThreads) > 0:
                    #record thread
                    for wsqThread in wsqThreads:
                        print vars(wsqThread)
                        writefile.writeThread(config, wsqThread)

            if int(config['isdev']) == 1 or next >= total:
                break


