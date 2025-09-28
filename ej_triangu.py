print('** Dibujar triangulo **')

numero_filas = int(input('Indica numero de filas: '))

#filas del triangulo
for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2* fila - 1)
    print(f'{espacios_blanco}{asteriscos}')