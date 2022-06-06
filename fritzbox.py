from os.path import join
import pprint
from os import path
import socket
import sys
from fritzconnection import FritzConnection

args = sys.argv
change = True

if args[1:]:
    change = True
# if args[2:]:
    # enable = args[2]
pp = pprint.PrettyPrinter(indent=2)

hostname = socket.gethostname()
script_folder = path.dirname(__file__)

boxuser = 'fritz3220'

ip = 'http://192.168.178.1'

with open(join(script_folder, 'env_fritzbox'), 'r') as file_:
    boxpw = file_.readline()
if hostname == 't--pc':
    boxpw = boxpw[:-1]

fc = FritzConnection(password=boxpw, user=boxuser)


def main():
    keys = ['WANIPConnection', 'GetInfo']
    keys = ['DeviceInfo', 'GetInfo']
    keys = ['WLANConfiguration', 'GetInfo', 'NewEnable']
    result = fbc(keys)
    if change:
        result = div(not result)
    result = fbc(keys)
    print(1, result)


def fbc(keys):
    state = fc.call_action(keys[0], keys[1])
    return state[keys[2]] if 0 <= 2 < len(keys) else state


def div(enable):
    result = fc.call_action('WLANConfiguration', 'SetEnable', NewEnable=enable)
    return result


if __name__ == '__main__':
    main()
