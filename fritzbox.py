# from os import path
from os.path import join
import requests
import re
import pprint
from os import path
import socket
from fritzconnection import FritzConnection

enable = True
enable = False

hostname = socket.gethostname()
script_folder = path.dirname(__file__)

boxuser = 'fritz3220'

ip = 'http://192.168.178.1'

with open(join(script_folder, 'env'), 'r') as file_:
    boxpw = file_.read()
if hostname == 't--pc':
    boxpw = boxpw[:-1]

fc = FritzConnection(password=boxpw, user=boxuser)
print(fc)


def main():
    pp = pprint.PrettyPrinter(indent=2)
    # keys = ['WANIPConnection', 'GetInfo']
    keys = ['DeviceInfo', 'GetInfo']
    keys = ['WLANConfiguration', 'GetInfo', 'NewEnable']
    # result = div()
    result = fbc(keys)
    pp.pprint(result)


def fbc(keys):
    state = fc.call_action(keys[0], keys[1])
    return state[keys[2]] if 0 <= 2 < len(keys) else state


def div():
    result = fc.call_action('WLANConfiguration', 'SetEnable', NewEnable=enable)
    return result


if __name__ == '__main__':
    main()
