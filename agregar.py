#!/usr/bin/python
#from pprint import pprint
import routeros_api

connection = routeros_api.RouterOsApiPool('', username='', password='', port=8728, plaintext_login=True)
api = connection.get_api()
ruta_mikrotik =  api.get_resource('/ip/firewall/address-list')
lineas = ruta_mikrotik.add(address="10.10.10.10", list="address-list")
print(lineas)
connection.disconnect()
