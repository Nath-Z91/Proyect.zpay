print('** Bienvenido a la casa de los espejos **')

edad = int(input('Cual es tu edad? '))
tienes_miedo_oscuridad = input('Tienes miedo a la oscuridadd (si/no)?')
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la casa')
else:
    print('No puedes entrar a la casa')
    