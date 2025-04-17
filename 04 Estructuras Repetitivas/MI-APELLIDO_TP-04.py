#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


num = int(input("Ingresar número entero: "))
cantidad_digitos = len(str(num))

if num >= 0:
    print(f'El valor {num} tiene {cantidad_digitos} dígitos')
else:
    print(f'El valor {num} tiene {cantidad_digitos - 1} dígitos')


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores


inicio = int(input("Ingresar número entero de inicio: "))
final = int(input("Ingresar número entero para el final: "))
suma_final = 0

for i in range(inicio + 1, final):
    suma_final = i + suma_final

print(suma_final)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

num = int(input("Ingresar número entero (Ingresar 0 para finalizar): "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingresar número entero (Ingresar 0 para finalizar): "))

print(f'La suma total es: {suma}')




#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

numero_aleatorio = random.randint(0, 9)

num = int(input("Adivinar número entero (Ingresar valores entre 0 y 9 para no perder): "))
conteo = 0

if num >= 0 and num < 10:
    while num != numero_aleatorio:
        conteo += conteo + 1
        num = int(input("Adivinar número entero (Ingresar valores entre 0 y 9): "))
else:
    print("El número esta por fuera del rango. Fin del juego")
    
if num == numero_aleatorio:
    print(f"GANASTE. Fueron necesarios {conteo} intentos")
