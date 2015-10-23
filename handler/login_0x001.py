#!/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'Magnus'


def handle(client_manager, session_no, arg):
    # print("handler ok")
    msg = dict()
    msg["cmd"] = 1
    if client_manager.login(session_no, arg):
        msg["result"] = 0
    else:
        msg["result"] = 1
    return msg

