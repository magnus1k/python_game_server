#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
import sys
print(sys.platform)
if sys.platform == "linux":
    from twisted.internet import epollreactor
    epollreactor.install()

__author__ = 'Magnus'


class GameSocket(Protocol):
    #有新用户连接至服务器
    def connectionMade(self):
        print('New Client')

    #客户端断开连接
    def connectionLost(self, reason):
        print('Lost Client')

    #收到客户端发送数据
    def dataReceived(self, data):
        try:
            incomedata = data.decode()
        except UnicodeDecodeError:
            return
        print('Get data:' + incomedata)
        #向该客户端发送数据
        outputdata = ('发送消息:' + incomedata).encode('utf-8')
        self.transport.write(outputdata)


if __name__ == '__main__':
    f = Factory()
    f.protocol = GameSocket
    reactor.listenTCP(5200, f)
    print('server started...')
    reactor.run()
