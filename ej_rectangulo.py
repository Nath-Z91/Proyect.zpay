print('** Calculo area y perimetro de un Rectangulo **')

base = float(input('Ingresa la base del rectangulo: '))
altura = float(input('Ingresa la altura del rectangulo: '))

# Calculos

area = base * altura
perimetro = 2 *(base + altura)

print(f'El area del rectangulo es: {area}')
print(f'El perimetro del rectangulo es: {perimetro}')
