#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo()


#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
#  Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

saludar_usuario(input('Cuál es tu nombre? '))


#3. Crear una función llamada informacion_personal(nombre, apellido,
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



#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

hora = segundos_a_horas(int(input('Indicar segundos: ')))
print(f'La cantidad de segundos registrada, equivale a {hora} horas')




#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.


def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f'{numero} x {i}  = {i * numero}')


tabla_multiplicado = tabla_multiplicar(int(input('Ingresar un número: ')))
print(tabla_multiplicado)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
#restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


def operaciones_basicas(a, b):
    return (a + b, a- b, a * b, a / b)

ops_basicas = operaciones_basicas(1, 2)
print(ops_basicas)


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

imc = calcular_imc(float(input('Ingresar peso en kilogramos: ')), float(input('Ingresar altura en metros: ')))
print(f'Tu IMC es: {imc:.2f}')


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.


def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

fahrenheit = celsius_a_fahrenheit(float(input('Ingresar tempertura en Celsius: ')))
print(fahrenheit)


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.


def calcular_promedio(a, b, c): 
    return (a + b + c) / 3 


avg = calcular_promedio(float(input('Ingresar un número: ')), float(input('Ingresar un segundo número: ')), float(input('Ingresar un tercer número: ')))
print(avg)