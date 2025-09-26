print(' ** Sitema de envios** ')

# Tarifa de envio por kg
TARIFA_NACIONAL = 10
TARRIFA_INTERNACIONAL = 20

#Valores de destino y peso al usuario
destino = input('Ingresa el destino del paquete (nacional/internacional): ')
peso = float(input('Ingresa e; peso del paquete (en kg):'))

#Envio del paquete
costo_envio = None
destino = destino.strip().lower()
if destino == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino == "internacional":
    costo_envio = peso * TARRIFA_INTERNACIONAL
else:
    print('Destino no valido. Ingresa el valor  nacional o internacional')

# Costos de envio 
if costo_envio is not None:
    print(f'El costo de envio del paquete es: ${costo_envio:.2f}')
