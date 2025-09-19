print('*** Sistema de empleados ***')

nombre_empleado = input('Nombre del empleado')
edad_empleado = int(input('Edad del empleado'))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('Es jefe departamento (si/no?)')

# convertir a bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# Imprimir los valores del empleado
print('\nDatos del Empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario:{salario_empleado:.2}')
print(f'Es jefe de departamento? {es_jefe_departamento}')