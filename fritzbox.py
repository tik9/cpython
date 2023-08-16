"""
fritzconnection.readthedocs.io/en/1.11.0/sources/getting_started.html
To use the TR-064 interface of the Fritz!Box:
Allow access for applications and Transmit status information over UPnP in Home Network -> Network -> Network Settings
"""

from fritzconnection import FritzConnection
import os
from dotenv import load_dotenv

load_dotenv()

fc = FritzConnection(password=os.getenv('fb'), user='fritz3220')


def main():
    '''call action'''
    # keys = ['WANIPConnection', 'GetInfo']
    # keys = ['DeviceInfo', 'GetInfo']
    keys = ['WLANConfiguration1', 'GetInfo', 'NewEnable']

    print(fc.call_action(keys[0], keys[1])[keys[2]])

    fc.call_action(keys[0], 'SetEnable', NewEnable=not (
        fc.call_action(keys[0], keys[1]))[keys[2]])

    print(fc.call_action(keys[0], keys[1])[keys[2]])


if __name__ == '__main__':
    main()
