import routeros_api

connection = routeros_api.RouterOsApiPool('', username='', password='', plaintext_login=True, port=8728, use_ssl=False, ssl_verify=False, ssl_verify_hostname=False, ssl_context=None)
api = connection.get_api()
ruta_mikrotik =  api.get_resource('/log')
logs_mikro = ruta_mikrotik.get()

# Imprimir datos 1 x 1
for log un logs_mikro
  print(log)

connection.disconnect()