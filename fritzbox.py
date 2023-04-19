"""
fritzconnection.readthedocs.io/en/1.11.0/sources/getting_started.html
To use the TR-064 interface of the Fritz!Box:
Allow access for applications and Transmit status information over UPnP in Home Network -> Network -> Network Settings
"""

from os.path import join, dirname
import socket
from fritzconnection import FritzConnection
import time
import os
from dotenv import load_dotenv

load_dotenv()

boxpw = os.getenv('fb')

if socket.gethostname() == 't--pc':
    boxpw = boxpw[:-1]

fc = FritzConnection(password=boxpw, user='fritz3220')


def main():
    '''call action'''
    # keys = ['WANIPConnection', 'GetInfo']
    # keys = ['DeviceInfo', 'GetInfo']
    keys = ['WLANConfiguration1', 'GetInfo', 'NewEnable']

    result = fc.call_action(keys[0], keys[1])
    # change(not result['NewEnable'])
    # time.sleep(2)
    print(result['NewEnable'])


def change(enable):
    '''change'''
    result = fc.call_action('WLANConfiguration', 'SetEnable', NewEnable=enable)
    return result


if __name__ == '__main__':
    main()
