def crear_arreglo():
    arreglo = []
    while True:
        numero = input("Introduce un número entero (o 'fin' para terminar): ")
        if numero.lower() == 'fin':
            break
        if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()):
            arreglo = arreglo + [int(numero)]
        else:
            print("Error: Por favor ingresa un número entero válido.")
    return arreglo

def imprimir_arreglo(arreglo):
    print("Arreglo:", arreglo)

def sumar_elementos(arreglo):
    suma = 0
    for numero in arreglo:
        suma += numero
    return suma

arreglo = crear_arreglo()
imprimir_arreglo(arreglo)
suma = sumar_elementos(arreglo)
if arreglo:
    print("La suma de los elementos es:", suma)
else:
    print("El arreglo está vacío.")
