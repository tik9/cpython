"""
fritzconnection.readthedocs.io/en/1.11.0/sources/getting_started.html
To use the TR-064 interface of the Fritz!Box, the settings for Allow access for applications and Transmit status information over UPnP in the Home Network -> Network -> Network Settings menu have to be activated.
"""

from os.path import join, dirname
import socket
from fritzconnection import FritzConnection

with open(join(dirname(__file__), '.env'), 'r', encoding='utf-8') as env:
    boxpw = env.readlines()[1].split('=')[1]

if socket.gethostname() == 't--pc':
    boxpw = boxpw[:-1]

fc = FritzConnection(password=boxpw, user='fritz3220')


def main():
    '''call action'''
    # keys = ['WANIPConnection', 'GetInfo']
    # keys = ['DeviceInfo', 'GetInfo']
    keys = ['WLANConfiguration1', 'GetInfo', 'NewEnable']
    result = fc.call_action(keys[0], keys[1])

    change(True)
    print(1, result)


def change(enable):
    '''change'''
    result = fc.call_action('WLANConfiguration', 'SetEnable', NewEnable=enable)
    return result


if __name__ == '__main__':
    main()
