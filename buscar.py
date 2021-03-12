
import routeros_api

connection = routeros_api.RouterOsApiPool('', username='', password='', plaintext_login=True, port=8728, use_ssl=False, ssl_verify=False, ssl_verify_hostname=False, ssl_context=None)
api = connection.get_api()
ruta_mikrotik = api.get_resource('/ip/firewall/address-list')
result = ruta_mikrotik.get(address="10.10.10.10")
print(len(result))
print(result)

connection.disconnect()
