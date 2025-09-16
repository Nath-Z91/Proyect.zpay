# Buscar subcadenas

cadena = 'Hola, mundo!'
indice = cadena.find('mundo')
print(f'Indice de la subcadena mundo:{indice}')

#Obtener el indice de la subcadema Hola
indice = cadena.find('Hola')
print(f'Indice de la subcadena Hola:{indice}')

#Obtener el indice de la subcadema hola, si el caracter no lo 
# encuentra arrojara -1, ya que en este caso la cadena aparece
# Hola y no hola.
indice = cadena.find('hola')
print(f'Indice de la subcadena hola:{indice}')