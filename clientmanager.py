#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from client import Client
import json

__author__ = 'Magnus'


class ClientManager:
    def __init__(self):
        self.client_num = 0
        self.clients = dict()
        self.online_clients = dict()

    def add_client(self, session_no):
        _client = Client()
        _client.id = self.client_num + 1
        _client.sessionno = session_no
        # self.clients.append(_client)
        print(_client)

    def login(self, session_no, client_js):
        username = client_js["name"]
        password = client_js["password"]
        if username in self.clients:
            userclient = self.clients[username]
            if userclient.password == password:
                userclient.session_no = session_no
                userclient.online = True
                self.online_clients[session_no] = userclient;
                print("User " + username + " log in")
                return True
        else:
            newclient = Client()
            newclient.id = len(self.clients) + 1
            newclient.name = username
            newclient.password = password
            newclient.session_no = session_no
            newclient.online = True
            self.clients[username] = newclient
            self.online_clients[session_no] = newclient;
            print("User " + username + " registered")
            return True
        return False

    def check_online(self, session_no):
        return session_no in self.online_clients

    def logout(self, session_no):
        if session_no in self.online_clients:
            self.online_clients[session_no].online = False
            del self.online_clients[session_no]


clientManager = ClientManager()


