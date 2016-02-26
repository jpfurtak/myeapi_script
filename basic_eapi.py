#!/usr/bin/python

#Test change#

from jsonrpclib import Server
from pprint import pprint as pp

switch = Server('http://jfurtak:arista123@192.168.56.10/command-api')
output = switch.runCmds(1, ['show version'])
pp(output[0]['systemMacAddress'])
result = switch.runCmds(1, ['enable',
                            'configure',
                            'interface Management1',
                            "description MAC: %s" % output[0]
['systemMacAddress']])
