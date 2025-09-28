print('** Aplicacion de cajero **')

saldo = 1000
salir = False
while not salir:
    print(f''' Operaciones que puedes realizar: 
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. salir''')
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print(f'Tu saldo actual es> ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresar valor a retirar: '))
        # validacion
        if retiro <= saldo:
            saldo -= retiro 
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente. Tu saldo es: ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el momto a depositar: '))
        saldo += deposito 
        print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
    elif opcion == 4:
        print(f'salir del cajero. Hasta pronto!') 
        salir = True   
        