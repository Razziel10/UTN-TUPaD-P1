#. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo()


#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
#  Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

saludar_usuario(input('Cuál es tu nombre? '))


#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#  Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido,edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

informacion_personal(input('Cuál es tu nombre? '), input('Cuál es tu apellido? '), int(input('Cuál es tu edad? ')), input('Cuál es tu residencia? '))


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como 
# parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
# funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = float(input('Indicar radio: '))

print(f'El radio {radio} tiene como area {calcular_area_circulo(radio)} y como perimetro {calcular_perimetro_circulo(radio)}')