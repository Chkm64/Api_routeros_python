
import routeros_api

connection = routeros_api.RouterOsApiPool('45.231.168.170', username='amendez', password='/**S1st3m4s**/', plaintext_login=True, port=50001)
api = connection.get_api()
ruta_mikrotik = api.get_resource('/ip/firewall/address-list')
result = ruta_mikrotik.get(address="10.10.10.10")
print(len(result))
print(result)

connection.disconnect()
