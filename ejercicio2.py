# Descripción: Escribe una función que reciba una matriz y retorne el número más grande y el más pequeño.
# Debe tener la función para crear la matriz e imprimirlo.
# No se pueden usar funciones propias de listas
def crear_matriz(filas, columnas):
    filas = int(input(f"Ingrese el numero de filas de la matriz: "))
    columnas = int(input(f"Ingrese el numero de columnas de la matriz: "))
    print("")
    matriz = [[int(input(f"Ingrese el valor en la posición {i},{j}: ")) for j in range(columnas)] for i in range(filas)]
    return matriz

def encontrar_min_max(matriz):
    min = matriz[0][0]
    max = matriz[0][0]

    for fila in matriz:
        for valor in fila:
            if valor < min:
                min = valor
            if valor > max:
                max = valor
    return min, max

def imprimir_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print(valor, end=" ")
        print()

ejecutar = True
if ejecutar:
    filas = int(input("Ingresa el número de filas de la matriz: "))
    columnas = int(input("Ingresa el número de columnas de la matriz: "))

    print("\nIngresa los valores de la matriz:")
    matriz = crear_matriz(filas, columnas)

    print("\nLa matriz ingresada es:")
    imprimir_matriz(matriz)

    min, max = encontrar_min_max(matriz)
    print(f"\nEl número más pequeño es: {min}")
    print(f"El número más grande es: {max}")
