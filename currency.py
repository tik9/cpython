'''convert currencies'''

import json
import sys
import urllib.request

if len(sys.argv) != 3:
    print("Usage: ./currencyrates.py lookup_currency base_currency. Example: ./currencyrates.py eur usd")
    sys.exit()

CU = sys.argv[1]
BASECU = sys.argv[2]

f = urllib.request.urlopen("http://freecurrencyrates.com/api/action.php?do=cvals&iso=" +
                           CU + "&f=" + BASECU + "&v=1&s=cbr")
obj = json.loads(f.read())
RES = "1 " + CU.upper() + " is "
RES += "{:,.2f}".format(1/obj[CU.upper()]) + \
    " " + BASECU.upper()

print(RES)
