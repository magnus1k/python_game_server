#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from clientmanager import clientManager
import json
import sys
import os


print(sys.platform)
if sys.platform == "linux":
    from twisted.internet import epollreactor
    epollreactor.install()

__author__ = 'Magnus'


class GameSocket(Protocol):
    #有新用户连接至服务器
    def connectionMade(self):
        # clientManager.add_client(self.transport.sessionno)
        print("Client connected:".format(self.transport.sessionno))

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


def load_config():
    conf_file = open('conf/config.json', encoding='utf-8')
    config_dict = json.loads(conf_file.read())
    return config_dict['port'], config_dict['handler']


def load_handler():
    names = os.listdir('handler')



if __name__ == '__main__':
    f = Factory()
    f.protocol = GameSocket
    port, handler = load_config()
    reactor.listenTCP(port, f)


    handler_name = "handler/login_0x001.py"

    print('server started...')
    reactor.run()
