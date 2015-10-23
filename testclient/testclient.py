#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import socket
import json

__author__ = 'Magnus'


def conn_to_server():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 5201))
    protocol = dict()
    protocol["cmd"] = 1
    protocol["arg"] = {'name': 'test', 'password': '123321'}
    conn.send(json.dumps(protocol).encode())

    recv = conn.recv(1024)
    print(recv.decode())
    data = json.loads(recv.decode())
    if data['cmd'] == 1:
        print('Result:{0}'.format(data['result']))
    conn.close()


if __name__ == '__main__':
    conn_to_server()



