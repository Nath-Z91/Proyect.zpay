print('--Manejo de listas--')

mi_lista = [1,2,3,4,5]
print(f'{mi_lista}-> Lista original')

# largo de una lista
print(f'Largo de la lista:{len(mi_lista)}')

# acceder a los elementos indicados
print(f'Accedemos al ultimo indice de la lista {mi_lista[-1]}')

# Modificar los elementos de la lista
mi_lista[1] = 10
print(f'Modificar el valor del indice 1: {mi_lista}')

#Agregar un elemento final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agrego el elemneto 6')

#adicionarl un elemento en un indice especial
mi_lista.insert(2,15)
print(f'{mi_lista}-> Se adiciono el valor de 15 en el indice 2')

#Eliminar elementos de una lista con remove
mi_lista.remove(5)
print(f'{mi_lista} -> Se removio el valor 5')
#Removemos por indice con pop
mi_lista.pop(1) # se elimina el 1
print(f'{mi_lista} -> se elimino el indice 1')
#Eliminar usando del
del mi_lista[2]
print(f'{mi_lista} -> se elimino el indice 2')

#Obtener sublistas
sublista = mi_lista[1:3] # genera una sublista del indice 1 al 2 ( no incluye 3)
print(f'sublista [1:3]')