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

    result = fc.call_action(keys[0], keys[1])
    print(result['NewEnable'])
    fc.call_action('WLANConfiguration', 'SetEnable',
                   NewEnable=not result['NewEnable'])
    result = fc.call_action(keys[0], keys[1])
    print(result['NewEnable'])


if __name__ == '__main__':
    main()
