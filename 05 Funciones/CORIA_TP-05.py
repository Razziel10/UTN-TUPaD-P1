#Práctico 5: Listas


#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista = []

for i in range(1,101):
    if i % 4 == 0:
        lista.append(i)
        
print(lista)



#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se 
# muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista = [1,2,3,4,5]

print(lista[-2])



#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []


lista_vacia = []

lista_vacia.append("auto")
lista_vacia.append("moto")
lista_vacia.append("perro")

print(lista_vacia)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)



#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#RESPUESTA: Elimina el valor de mayor valor de la lista; Exactamente, el número 22


