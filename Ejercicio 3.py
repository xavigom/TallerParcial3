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

def calcular_promedio(arreglo):
    if not arreglo:
        return 0
    suma = 0
    contador = 0
    for numero in arreglo:
        suma += numero
        contador += 1
    promedio = suma / contador
    return promedio

arreglo = crear_arreglo()
imprimir_arreglo(arreglo)
promedio = calcular_promedio(arreglo)
if arreglo:
    print("El promedio de los elementos es:", promedio)
else:
    print("El arreglo está vacío.")