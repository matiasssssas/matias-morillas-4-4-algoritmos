def ej1():
    numeros = []
    for i in range(5):
        numero = int(input(f"ingrese el numero{i+1}:"))
        numeros.append(numero)

    print("Los numeros ingresados son:")
    for num in numeros:
        print(num)

ej1()

def ej2():
    Frutas = ("Manzana","Uva","Pera","Naranja","Banana")
    busqueda = input("Ingrese el nombre de una fruta:").lower()
    if busqueda in Frutas:
        print(f"la fruta 'busqueda' esta en la posicion {Frutas.index(busqueda)}.")

ej2()

def ej3():
    notas = (1,2,3,4,5,6,7,8,9,10)
    suma = sum(notas)
    promedio = suma / len(notas)
    print(f"suma total de notas: {suma}")
    print(f"Promedio: {promedio:.2f}")

ej3()

def ej4():
    temperaturas = [23, 17, 29, 21, 19, 30, 16]

    max_temp = temperaturas[0]
    min_temp = temperaturas[0]

    for temp in temperaturas:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp

    print("Temperatura máxima:", max_temp)
    print("Temperatura mínima:", min_temp)

ej4()

def ej5():
    numeros = [8, 3, 1, 7, 4, 10, 2]

    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]

    print("Lista ordenada:", numeros)

ej5()

def ej6():
    numeros = [12, 7, 9, 4, 6, 15, 18, 3, 10, 5, 2, 8, 11, 14, 1]

    pares = 0
    impares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)


