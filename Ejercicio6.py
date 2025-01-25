# Ejercicio 6

def crearArreglo():
    n = int(input("Introduzca el num de elementos del arreglo: "))
    arreglo = []
    for i in range(n):
        elemento = int(input(f"Introduce el elemento n{i+1}: "))
        arreglo.append(elemento)
    return arreglo

def funPares(arreglo):
    pares = []
    for numero in arreglo:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def funImpares(arreglo):
    impares = []
    for numero in arreglo:
        if numero % 2 != 0:
            impares.append(numero)
    return impares

arreglo = crearArreglo()
pares = funPares(arreglo)
impares = funImpares(arreglo)
print("El arreglo es el siguiente: ", arreglo)
print("Números pares:", pares)
print("Números impares:", impares)