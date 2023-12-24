"""
fritzconnection.readthedocs.io/en/1.11.0/sources/getting_started.html
Access in the fbox: Network -> Network Settings
"""

from fritzconnection import FritzConnection
from fritzconnection.lib.fritzcall import FritzCall
import os
from dotenv import load_dotenv

load_dotenv()

fc = FritzConnection(password=os.getenv('fb'), user='fritz3220')
keys = ['WLANConfiguration1', 'GetInfo', 'NewEnable']


def main():
    '''main'''
    enable()
    # getInfo()
    # print(fc.call_action(keys[0], keys[1])[keys[2]])

def fritzcalls():
    fc = FritzCall(password=os.getenv('fb'))
    # calls = fc.get_missed_calls(days=1)
    # calls = fc.get_in_calls(days=2)
    for call in fc.get_out_calls(days=3):
        # for call in fc.get_calls(days=3):
        print(call)


def getInfo():
    # key = 'WANIPConnection'
    key = 'DeviceInfo'
    # key = keys[0]
    print(fc.call_action(key, 'GetInfo'))


def enable():

    print(fc.call_action(keys[0], keys[1])[keys[2]])

    fc.call_action(keys[0], 'SetEnable', NewEnable=not (
        fc.call_action(keys[0], keys[1]))[keys[2]])

    print(fc.call_action(keys[0], keys[1])[keys[2]])


if __name__ == '__main__':
    main()
