'''fritzbox connect'''

from os.path import join,dirname
import socket
import sys
from fritzconnection import FritzConnection

change = False
change = True

ip = 'http://192.168.178.1'

with open(join(dirname(__file__), '.env'), 'r',encoding='utf-8') as file_:
    boxpw = file_.readlines()[1].split('=')[1]

if socket.gethostname() == 't--pc':
    boxpw = boxpw[:-1]

print(boxpw)
fc = FritzConnection(password=boxpw, user='fritz3220')
fc=FritzConnection()
# print(fc)
# sys.exit()

def main():
    '''call functions'''
    keys = ['WANIPConnection', 'GetInfo']
    # keys = ['DeviceInfo', 'GetInfo']
    # keys = ['WLANConfiguration', 'GetInfo', 'NewEnable']
    result = fbc(keys)

    print(1, result)
    # div(change)
    # print(2, result)
    # div(not result)
    # result = fbc(keys)
    # print(3, result)


def fbc(keys):
    '''state'''
    state = fc.call_action(keys[0], keys[1])
    return state
    # return state[keys[2]] if 0 <= 2 < len(keys) else state


def div(enable):
    '''change'''
    result = fc.call_action('WLANConfiguration', 'SetEnable', NewEnable=enable)
    return result


if __name__ == '__main__':
     main()
