#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import json
import codecs

__author__ = 'Magnus'

configdict = dict()
configdict['port'] = 5201
configdict['handler'] = 'login_0x001.py'

json_output = json.dumps(configdict, sort_keys=True, indent=4)
file_object = codecs.open('config.json', 'w', 'utf-8')
file_object.write(json_output)
file_object.close()
