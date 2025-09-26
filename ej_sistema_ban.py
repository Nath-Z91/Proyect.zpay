print(' ** Sistema Bancario **')

salir_sistema_txt = input('Desea salir del sistema (si/no)? ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuar dentro del sistema')
else:
    print('Salir del sistema')
    