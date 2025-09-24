print('*** Sistema descuento***')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy?'))
tiene_membresia = input('Tiene la membresia de la tienda (si/no)?')

es_elegible_descuento = cantidad_productos >= NO_PRODUCTOS_DESCUENTO and tiene_membresia.strip().lower() == 'si'
