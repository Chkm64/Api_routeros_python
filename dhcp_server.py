"""
El Leases del DHCP Server no admite que se repitan las MAC ni las IPS dentro del mismo Router
Lo que indica que este parametro tiene que ser unico por Router, motivo por el cual lo primero
haremos es buscar la ip dentro de esta zona y si encuentra alguna ip devolver un mensaje e incrementar
un contador que al final no nos dejará agregar el registro, de igual forma lo haremos con la MAC.
"""
import routeros_api

connection = routeros_api.RouterOsApiPool('', username='', password='', plaintext_login=True, port=8728, use_ssl=False, ssl_verify=False, ssl_verify_hostname=False, ssl_context=None)
api = connection.get_api()
ruta_mikrotik = api.get_resource('/ip/dhcp-server/lease')
result = ruta_mikrotik.get(address='10.10.10.10')
contador = 0
if len(result) > 0:
	contador += 1
	print("Ya existe la IP")
result = ruta_mikrotik.get(mac_address='01:02:03:04:05:06')
if len(result) > 0:
	contador += 1
	print("Ya existe la MAC")

if contador == 0:
	print("Agregando IP y MAC")
	result = ruta_mikrotik.add(address="10.10.10.10", mac_address="01:02:03:04:05:06", comment="Comentario")

connection.disconnect()