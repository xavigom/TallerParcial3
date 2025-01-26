def crear_arreglo():
    n = int(input("¿Cuántos elementos tendrá el arreglo? "))
    arreglo = [0] * n
    for i in range(n):
        arreglo[i] = int(input(f"Ingrese el número {i + 1}: "))
    return arreglo

def imprimir_arreglo(arreglo):
    print("Arreglo:", end=" ")
    for num in arreglo:
        print(num, end=" ")
    print()

def invertir_arreglo(arreglo):
    arreglo_invertido = [0] * len(arreglo)
    for i in range(len(arreglo)):
        arreglo_invertido[len(arreglo) - 1 - i] = arreglo[i]
    return arreglo_invertido

ejecutar = True
if ejecutar:
    arreglo = crear_arreglo()
    print("Arreglo original:")
    imprimir_arreglo(arreglo)

    arreglo_invertido = invertir_arreglo(arreglo)
    print("Arreglo invertido:")
    imprimir_arreglo(arreglo_invertido)
