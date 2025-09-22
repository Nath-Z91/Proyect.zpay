#Operadores numericos

a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicacion:", a * b)
print("Divicion:", a / b)
print("Parte entera de la division:", a // b)
print("Potenciacion:", a ** b)
print("Modulo:", a % b)
a/= 2
print(a)
operation_1 = 2 + 3 * 4
operation_2 = (2 + 3) * 4
operation_3 = (2+3) * (4**2)/ 8 - 1
print(operation_1)
print(operation_2)
print(operation_3)

# O comparacion o Relacionales 

a,b = 7,5
print(f'vzlor inicial a: {a}, b: {b}')

# Operador de comprardor ==
resultado = a == b
print(f'Resultado a == b es: {resultado}')

# Operador diferente !=
resultado = a != b
print(f'Resultado a != b es: {resultado}')

# Operador menor que <
resultado = a < b
print(f'Resultado a < b es: {resultado}')
# Operador menor o igual <=
resultado = a <= b
print(f'Resultado a <= b')
# Operador mayor >
resultado = a > b
print(f'Resultado a > b es: {resultado}')

# Operador mayor o igual >=
resultado = a >= b
print(f'Resultado a>= b')

# Operador and ( si ambos valores son verdaderos)
condicion1 = True
condicion2 = True
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')

