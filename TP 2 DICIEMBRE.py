import random

def ejercicio1():

    frutas = ['banana', 'apple', 'mango']
    print(frutas)
    print(frutas[1])


def ejercicio2():

    animales = ['gato', 'perro', 'elefante']
    animales.append('jirafa')
    animales.remove('gato')
    print(animales)
    return animales


def ejercicio3():
    lista1 = [5,1,8]
    lista2 = [3,9,2]

    ValorTotal = 0

    lista_combinada = lista1+lista2

    for n in lista_combinada:
        ValorTotal = ValorTotal + n
        print(ValorTotal)
    return ValorTotal


def ejercicio4():
    lista1 = [5,1,8]
    lista2 = [3,9,2]

    lista_combinada = lista1+lista2

    print(lista_combinada)


def ejercicio5():
    nombres = ("Pepe", "Juana", "Santiago", "Ignacio", "Federico", "Gabriel", "Sofia")

    notas = (1 ,2, 3, 4, 5, 6, 7, 8, 9, 10)

    alumno = []

    alumno.append(random.choice(nombres))
    alumno.append(random.choice(notas))
    print(alumno)
    return alumno


def ejercicio6():

    Alumno1 = ejercicio5()
    Alumno2 = ejercicio5()
    Alumno3 = ejercicio5()
    NotasCurso = [Alumno1[1], Alumno2[1], Alumno3[1]]
    Promedio = 0
    for x in range(0, len(NotasCurso)):
        Promedio = Promedio + NotasCurso[x]
    print(Alumno1, Alumno2, Alumno3)
    Promedio = Promedio / 3
    return Promedio


def ejercicio7():
    PromediosEscuela = 0

    for x in range(3):
        opcion = int(input("1 = Generar curso: / 2 = Salir:"))

        while opcion != 1 and opcion != 2:
            print("Numero incorrecto")
            opcion = int(input("1 = Generar curso: / 2 = Salir:"))

        if opcion == 2:
            print("Salir")
            break

        Alumno1 = int(input("Nota del alumno 1: "))

        Alumno2 = int(input("Nota del alumno 2: "))

        Alumno3 = int(input("Nota del alumno 3: "))

        PromedioEscuela


