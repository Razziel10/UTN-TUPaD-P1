#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario


def factorial(num):
    if num == 1:
        return 1
    else:
       return num * factorial(num - 1)
  

prueba = factorial(5)
print(prueba)



#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.
 

def fibonacci_recursivo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2)


print(fibonacci_recursivo(5))




#3)Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1)
#. Prueba esta función en un algoritmo general.


def calcular_potencia_recursivo(n, m):
    if m == 0:
        return 1
    else:
        return n * calcular_potencia_recursivo(n, m - 1)


print(calcular_potencia_recursivo(2, 3))



#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

#Convertir el número 10 a binario:
#10 ÷ 2 = 5 resto: 0
#5 ÷ 2 = 2 resto: 1
#2 ÷ 2 = 1 resto: 0
#1 ÷ 2 = 0 resto: 1
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".


def binario_rec(num):
    if num == 0:
        return ""
    else:
        return binario_rec(num // 2) + str(num % 2)


print(binario_rec(10))  # "1010"



#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:  
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    


palabra = es_palindromo(input("Insertar palabra sin espacios ni tildes: "))

print(palabra)