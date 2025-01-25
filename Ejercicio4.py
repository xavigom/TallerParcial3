# Ejercicio 4 

def crearArreglo():
    n = int(input("Introduzca el num de elementos del arreglo: "))
    arreglo = [0] * n
    for i in range(n):
        elemento = int(input(f"Introduce el elemento n{i+1}: "))
        arreglo[i] = elemento
    return arreglo

def imprimir(arreglo):
    print("El arreglo es:", end=" ")
    for elemento in arreglo:
        print(elemento, end=" ")
    print()

def contar(arreglo, num):
    contador = 0
    for elemento in arreglo:
        if elemento == num:
            contador += 1
    return contador

arreglo = crearArreglo()
imprimir(arreglo)
num = int(input("Introduce el número a buscar en el arreglo: "))
resultado = contar(arreglo, num)
print(f"El número {num} aparece {resultado} veces en el arreglo.")