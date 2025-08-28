def ej1():
   matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]


   for fila in matriz:
       print(fila)

ej1()

def ej2():
   matriz = [[10, 20, 30],
             [40, 50, 60],
             [70, 80, 90]]


   suma_total = 0
   for fila in matriz:
       suma_total += sum(fila)
   print("La suma de todos los números en la matriz es:", suma_total)



ej2()


def ej3():
   matriz = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]




   fila = int(input("Ingresa el índice de la fila 0 a 3: "))
   columna = int(input("Ingresa el índice de la columna 0 a 3: "))




   if 0 <= fila < 4 and 0 <= columna < 4:
       elemento = matriz[fila][columna]
       print(f"El elemento en la posición ({fila}, {columna}) es: {elemento}")
   else:
       print("Índice fuera de rango. Por favor ingresa valores entre 0 y 3.")


ej3()


def ej4():
    def encontrar_maximo():
        matriz = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

        maximo = matriz[0][0]
        for fila in matriz:
            for elemento in fila:
                if elemento > maximo:
                    maximo = elemento

        print("La matriz es:")
        for fila in matriz:
            print(fila)
        print(f"\nEl número más grande de la matriz es: {maximo}")
    encontrar_maximo()


ej4()