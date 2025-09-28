print('** Sistema de administracion de cuentas **')

salir = False
while not salir:
    print(f'''Menu: 
    1. Crear cuenta, 
    2. Eliminar cuenta, 
    3. salir''')
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema...\n')
        salir = True
    else:
        print('Opcion invalida, proporciona otra opcion...\n')