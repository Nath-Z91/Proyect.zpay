print(' *** Sistema de Autenticacion *** ')

Usuario_valido = 'admin'
Password_valido = '123'

usuario_ingresado = input('Cual es tu usuario? ')
Password_ingresado = input('Cual es tu password? ')

son_datos_correctos = (usuario_ingresado.strip() == Usuario_valido and Password_ingresado.strip() == Password_valido)

print(f'Datos son correctos? {son_datos_correctos}')