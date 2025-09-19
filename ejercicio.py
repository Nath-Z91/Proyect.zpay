# Ejercicio Generar Email
print('*** Generar Email***')

# Nombre completo del Usuario
nombre_completo = ' Zoe Gutierrez Pinilla '
print(f'Nombre usuario: {nombre_completo}')
# Procesar o normalizar el nombre del usuario
# Limpiamos los espacios en blanco al inicio y fin
nombre_normalizado = nombre_completo.strip()
# Reemplazar los espacios por puntos
nombre_normalizado = nombre_normalizado.replace(' ','.').lower()
#comvertir a minusculas
print(f'Nombre usuario normalizado: {nombre_normalizado}')

# Datos de la empresa
nombre_empresa = ' Nathz space '
print(f'\nNombre empresa: {nombre_empresa}')
extencion_dominio = '.com.co'
print(f'Extencion del dominio: {extencion_dominio}')
#Quitamos los espacios en blanco y se pasa a minusculas
nombre_empresa_normalizado = nombre_empresa.replace(' ','').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extencion_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')
# Completamos el email
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')
