#!/usr/bin/env python

import sys, os 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import BoschShcPy

ACCESS_CERT = 'keystore/aps-cert.pem'
ACCESS_KEY = 'keystore/aps-key.pem'

SMART_PLUG_ID = "hdm:HomeMaticIP:3014F711A0000496D858ACC5"
IP_SHC = '192.168.1.6'
PORT_SHC = '8444'


try:
    # Create a BoschSHC client with the specified ACCESS_CERT and ACCESS_KEY.
    client = BoschShcPy.Client(IP_SHC, PORT_SHC, ACCESS_CERT, ACCESS_KEY)
    
    shc_info = client.shc_information()
    print('  version        : %s' % shc_info.version)
    print('  updateState    : %s' % shc_info.updateState)
    
    #   device = client.device(SMART_PLUG_ID)
    #   print(device)
    # 
    
    print("Accessing a dummy device...")
    smart_plug = BoschShcPy.SmartPlug(client, BoschShcPy.Device(), SMART_PLUG_ID, "Dummy")
    smart_plug.update()
    print(smart_plug)
    
    print("Setting state of dummy device...")
    smart_plug.set_state(False)
    print(smart_plug)

#     # Fetch the smart plug object.
#     smart_plug = client.smart_plug(SMART_PLUG_ID, "Dummy")
#     #   smart_plug_services = client.smart_plug_services(SMART_PLUG_ID)
#     #   print(smart_plug_services)
#     #   for item in smart_plug_services.items:
#     #       print (item)

    print("Accessing all smart plug devices...")
    smart_plugs = BoschShcPy.smart_plug.initialize_smart_plugs(client, client.device_list())
    for item in smart_plugs:
        print (item)

except BoschShcPy.client.ErrorException as e:
    print('\nAn error occured while requesting a SmartPlug object:\n')

    for error in e.errors:
        print('  code        : %d' % error.code)
        print('  description : %s' % error.description)
        print('  parameter   : %s\n' % error.parameter)
