

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

