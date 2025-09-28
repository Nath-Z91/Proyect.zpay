print('** Suma Acumulativa **')

#Suma los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

# valores
while numero <= MAXIMO:
    acumulador_suma += numero
    numero += 1
print(f'\nResultado suma acumulada: {acumulador_suma}')