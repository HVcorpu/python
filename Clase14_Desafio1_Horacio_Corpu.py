'''
Clase 14: 
Desafío 1
Escribe un programa que solicite al usuario ingresar su nombre, apellido, año 
de nacimiento y ciudad de residencia. Utiliza f-strings y funciones de cadena 
para dar formato a la salida. La tarjeta debe incluir los siguientes datos:
● Apellido en mayúsculas y nombre: formato "APELLIDO, Nombre".
● Año de nacimiento.
● Correo electrónico: primera letra del nombre en minúsculas, seguido 
del apellido en minúsculas, un punto y el año de nacimiento, seguido de 
"@empresa.com.ar".
● Ciudad de residencia en mayúsculas.
● Edad aproximada: diferencia entre año actual y año de nacimiento.
La tarjeta debe incluir un marco superior e inferior de líneas para mejorar la 
presentación
Autor: Horacio Javier Corpu
Fecha:01/05/2024
Revisión: 00
'''
# Ingreso de datos y asignación de variables
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nacimiento = input("Ingrese su año de nacimiento: ")
ciudad = input("Ingrese su ciudad de residencia: ")

# formatos para las variables
primera_nombre = nombre[0] # filtra la primera letra del nombre
primera_nombre = primera_nombre.lower() # convierte en minúscula a la letra
minuscula_apellido = apellido.lower() # convierte en minuscula al apellido
nombre = nombre.title() # convierte a mayúscula la primera letra de cada cadena
apellido = apellido.upper() # convierte en mayúscula al apellido
ciudad = ciudad.upper() # convierte en mayúscula a la ciudad
cadena = "DATOS PERSONALES" # cadena de encabezado

# Cálculo de la edad

num_nacimiento = int(nacimiento) # convierte en entero a la cadena nacimiento y la almacena 
edad = 2024 - num_nacimiento

# Visualización por consola
print()
print(cadena.center(50,"*")) 
print("-"*50)
print(f'| Apellido y nombre: {apellido}, {nombre}')
print(f'| Año de nacimiento: {nacimiento}')
print(f'| Correo electrónico: {primera_nombre}{minuscula_apellido}.{nacimiento}@empresa.com.ar')
print(f'| Ciudad {ciudad}')
print(f'| Edad aproximada: {edad}')
print("-"*50)
