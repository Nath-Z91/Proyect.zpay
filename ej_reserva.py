print('** Sistema de Reserva **')

# Variables del hotel
tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

# Informacion usuario
nombre_cliente = input('Nombre del cliente: ')
dias_estadia = int(input('Dias de estadia: '))
vista_al_mar_txt = input('Con vista al mar (si/no)?')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

#Costo total 
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar
    
#Detalle de la reserva
print('\n ---- Detalles de la Reserva ----')
print(f'Cliente: {nombre_cliente}')
print(f'Dias de estadia: {dias_estadia}')
print(f'Costo total: ${costo_total:.2f}')
print(f'Habitacion con vista al mar: {'Si' if vista_al_mar else 'No'}')