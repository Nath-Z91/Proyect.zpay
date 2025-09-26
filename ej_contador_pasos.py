print('** Contador de pasos **')

# Constantes
META_PASOS_DIARIOS =  1000
CALORIAS_POR_PASO = 0.04 

# Datos del usuario
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

#calculo de pasos
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

#Calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostrar informacion 
print(f'\nUsuario:{nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diarios alzandos: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos')