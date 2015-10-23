#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import importlib

__author__ = 'Magnus'


class HandlerManager:
    def __init__(self):
        self.handlers = dict()

    def load(self):
        names = os.listdir('handler')
        for name in names:
            modulename, extname = os.path.splitext(name)
            if extname == ".py":
                try:
                    idstr = modulename.split("_")[-1].split('x')[-1]
                    hid = int(idstr, 16)
                    print(hid)
                    self.handlers[hid] = importlib.import_module('handler.' + modulename)
                except ValueError:
                    print("Wrong handler:", name)
                    continue

handlerManager = HandlerManager()
