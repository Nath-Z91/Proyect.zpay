print('** Valor dentro de rango **')

MINIMO = 0 
MAXIMO = 5

# Solicitamos un valor entre 0 y 5
dato = int(input(f'Proporciona un dato entre {MINIMO} Y {MAXIMO}: '))

# Verificamos si el dato se encuentra dentro de rango
#esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO
esta_dentro_rango = MINIMO <= dato <= MAXIMO
print(f'valor esta dentro de rango? {esta_dentro_rango}')