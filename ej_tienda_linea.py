print(' ** Sistema Tienda en linea ** ')

# Condiciones 
Monto_compra_Desc = 1000

monto_compra = float(input('Cual fue el monto de tu compra? '))
es_miembro = input('Eres miembro de la tienda (si/no)? ')

descuento = 0
# Verificar cada caso, con los datos proporcionados
if monto_compra >= Monto_compra_Desc and es_miembro.strip().lower() == 'si': descuento = 0.1
elif es_miembro.strip().lower() == 'si': descuento = .05
elif monto_compra >= Monto_compra_Desc: descuento = .03
else:
    descuento = 0
    
# Calculos para respuesta al usuario
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\nFelicidades, has obtenido un descuento del {descuento * 100:,0f}%')
    print(f'Monto de la compra: {monto_compra:.2f}')
    print(f'Monto del descuento: {monto_descuento:2.f}')
    print(f'Monto final de la compra con descuento: ${monto_final:.2f}')
else:
    print('\nNo obtuvieste ningun descuento')
    print(' Se miembro de la tienda')
    print(f'Monto final de la compra:{monto_compra:.2f}')