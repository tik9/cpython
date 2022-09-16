from os.path import join
from os import path
import socket
import sys
from fritzconnection import FritzConnection

args = sys.argv
change = False
change = True

if args[1:]:
    change = args[1]

ip = 'http://192.168.178.1'

# f=open('filename')
# lines=f.readlines()
with open(join(path.dirname(__file__), '.env'), 'r') as file_:
    boxpw = file_.readlines()[1].split('=')[1]
    
if socket.gethostname() == 't--pc':
    boxpw = boxpw[:-1]

fc = FritzConnection(password=boxpw, user='fritz3220')


def main():
    keys = ['WANIPConnection', 'GetInfo']
    keys = ['DeviceInfo', 'GetInfo']
    keys = ['WLANConfiguration', 'GetInfo', 'NewEnable']
    result = fbc(keys)

    print(1, result)
    # div(change)
    # print(2, result)
    # div(not result)
    # result = fbc(keys)
    # print(3, result)


def fbc(keys):
    state = fc.call_action(keys[0], keys[1])
    return state[keys[2]] if 0 <= 2 < len(keys) else state


def div(enable):
    result = fc.call_action('WLANConfiguration', 'SetEnable', NewEnable=enable)
    return result


if __name__ == '__main__':
    main()
