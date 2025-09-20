from random import randint

print('*** Sistema Generador de ID ***')

nombre = input('Cual es tu nombre')
apellido = input('Cual es tu apellido')
fecha_nacimiento = input('Cual es tu fecha de nacimiento (yyyy)')  


# Normalizacion de valores 
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
fecha_nacimiento_2 = fecha_nacimiento.strip()[2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el ID
id_unico = f'{nombre_2}{apellido_2}{fecha_nacimiento_2}{aleatorio}'

print(f'''\nHola {nombre},
      Tu nuevo numero ID es: {id_unico}
      Felicidades!''')
