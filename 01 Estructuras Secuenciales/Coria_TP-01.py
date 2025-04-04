#1)
print("Hola Mundo!")


#2)
nombre = input("Indicame tu nombre, por favor: ")
print(f"Hola {nombre}!")


#3)
nombre = input("Indicame tu nombre, por favor: ")
apellido = input("Indicame tu apellido, por favor: ")
edad = int(input("Indicame tu edad, por favor: "))
residencia = input("Indicame tu lugar de residencia, por favor: ")
print(f"Soy {nombre}, tengo {edad} años y vivo en {residencia}")



#4)
radio = float(input("Ingresar, por favor, el radio del círculo: "))

pi = 3.1416

area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")



#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

 
segundos = float(input("Indicar, por favor, una cantidad de segundos: ")) 

horas = float(segundos / 3600)


print(f'{segundos} segundos equivale a {horas} horas')
 


 #6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.


numero = int(input("Indicar, por favor, un numero: ")) 

print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)




#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numero_1 = int(input("Indicar, por favor, un número distinto de 0: ")) 
numero_2 = int(input("Indicar, por favor, otro número distinto de 0: ")) 


suma = numero_1 + numero_2
resta = numero_1 - numero_2
division = numero_1 / numero_2
multiplicacion = numero_1 * numero_2

print(f'la suma del primer y segundo número da como resultado: {suma}')
print(f'la resta del primer y segundo número da como resultado: {resta}')
print(f'la división del primer y segundo número da como resultado: {division}')
print(f'la multiplicación del primer y segundo número da como resultado: {multiplicacion}')




#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

altura = float(input("Cual es tu altura?: ")) 

peso = float(input("Cual es tu peso?: ")) 


masa_corporal = peso / (altura ** 2)

print()
print(f'El indice de masa corporal es: {masa_corporal}')


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
# Tener en cuenta la siguiente equivalencia:
 
celsius = int(input("Indicar grados celsius: ")) 

fahrenheit  = 1.8 * celsius + 32
print(f'el equivalente en temperatura fahrenheit es: {fahrenheit}')

 

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.


numero_1 = int(input("Indicar primer numero: ")) 
numero_2 = int(input("Indicar segundo numero: ")) 
numero_3 = int(input("Indicar tercer numero: ")) 

promedio = (numero_1 + numero_2 + numero_3) / 3

print(f'el promedio es: {promedio}')