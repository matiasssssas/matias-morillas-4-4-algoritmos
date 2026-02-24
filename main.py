def calculadora1():

    precio = float(input("Ingrese el precio del producto: "))

    descuento = 0

    if precio >= 100:
        descuento = precio * 0.15

    elif precio >= 50:
        descuento = precio * 0.10

    precio_final = precio - descuento

    print("Descuento:", descuento)
    print("Precio final:", precio_final)



def adivinar2():
    numero = int(input("Ingrese el numero del producto: "))

    numero_secreto = 7

    while numero != numero_secreto:
        if numero > numero_secreto:
            print("El numero es menor.")
        else:
            print("El numero es mayor.")

        numero = int(input("Intente otra vez:"))

    print("felicidades adivinaste el numero secreto ")

def vocales3():
    frase = input("Ingrese una frase: ")
    contador = 0

    for letra in frase:
        if letra in "aeiouAEIOU":
            contador += 1

    print("La frase tiene", contador, "vocales.")

def multiplicar4():
    numero = int(input("Ingrese un numero entero: "))
    for x in range(1,11):
        resultado = numero * x
        print(numero, "x", x, "=" , resultado)


def entero5():
    suma = 0

    numero = int(input("Ingrese un numero entero: "))

    while numero != 0:

        if numero % 2 == 0:
            suma += numero

        numero = int(input("Ingrese otro vez un numero:"))

    print("La suma de los numeros pares es:", suma)

def temperatura6():
    temperaturas = [22, 26, 18, 30, 24]

    suma = 0
    contador = 0
    mayor = temperaturas[0]
    menor = temperaturas[0]

    for temp in temperaturas:
        suma += temp

        if temp > 25:
            contador += 1

        if temp > mayor:
            mayor = temp

        if temp < menor:
            menor = temp

    promedio = suma / len(temperaturas)

    print("Promedio:", promedio)
    print("Días mayores a 25°:", contador)
    print("Día más caluroso:", mayor)
    print("Día más frío:", menor)
