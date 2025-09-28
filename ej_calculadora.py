print('** Calculadora **')

Operando1 = operando2 = resultado = 0
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
          1. Suma
          2. Resta
          3. Multiplicacion
          4. Divicion
          5. Salir''')
    opcion = int(input('Escoje una opcion: '))
    # valor de los operandos
    if 1 <= opcion <= 4:
        Operando1 = float(input('Dame el valor 1: '))
        operando2 = float(input('Dame en valor 2: '))
    # Operacion a realizar 
    if opcion == 1: 
        resultado = Operando1 + operando2
        print(f' resultado de la suma: {resultado:.2f}\n')
    if opcion == 2:
        resultado = Operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    if opcion == 3:
        resultado = Operando1 * operando2
        print(f'El resultado de la multiplicacion es: {resultado:.2f}\n')
    if opcion == 4:
        resultado = Operando1 / operando2
        print(f'El resultado de la divicion es: {resultado:.2f}\n')
    elif opcion == 5:
        print(f'saliendo del programa. Hasta luego!')
        salir = True
    else:
        print(f'Opcion errada, seleccione otra opcion\n')    
        