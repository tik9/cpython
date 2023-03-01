'''convert currencies'''

import json
import sys
import urllib.request

if len(sys.argv) != 3:
    print("Usage: Val lookup_currency base_currency. Example: ./" +
          "currencyrates.py 100 eur usd")
    # sys.exit()

# print(len(sys.argv))
# sys.exit()
VAL = 1
CU = 'eur'
BASE = 'gbp'
# BASECU = 'chf'
# BASECU = 'usd'

if len(sys.argv) > 1:
    VAL = int(sys.argv[1])


if len(sys.argv) > 2:
    CU = sys.argv[2]

if len(sys.argv) > 3:
    BASE = sys.argv[3]


def main():
    '''main'''
    print(curr())


def curr():
    '''currency'''
    # pylint: disable=line-too-long
    api = urllib.request.urlopen(
        "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + CU + "&f=" + BASE + "&v=1&s=cbr")
    obj = json.loads(api.read())
    res = f'{VAL} {CU} is '
    res += f'{VAL/obj[CU.upper()]:.2f} {BASE.upper()}'
    return res


if __name__ == '__main__':
    main()
