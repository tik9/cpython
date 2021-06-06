from fritzconnection import FritzConnection
import pprint

pp = pprint.PrettyPrinter(indent=2)
fc=FritzConnection(address='192.168.178.1', use_tls=True)

#switch guest WIFI off and on again - this works
state = fc.call_action('WLANConfiguration:3', 'GetInfo')
pp.pprint(state)
print("Disable WLAN")
# fc.call_action('WLANConfiguration3','SetEnable',arguments={'NewEnable':0})
state = fc.call_action('WLANConfiguration:3', 'GetInfo')
pp.pprint(state)
# input("Press Enter to continue...")
print("Enable WLAN")
# fc.call_action('WLANConfiguration3','SetEnable',arguments=NewEnable=1)
state = fc.call_action('WLANConfiguration:3', 'GetInfo')
pp.pprint(state)