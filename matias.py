


def ejercicio1():

    x = ("10")

    for x in range(0,11):
        print(x)



def ejercicio2():


    for x in range(0,5):

        print("Hola mundo")


def ejercicio3():


    for x in range(0,20):

        print("2,4,6,8,10,12,14,16,18,20")


def ejercicio4():


    for x in range(0,75,7):
        print(x)


def ejercicio5():

    chechon = 1+2+3+4+5

    for x in range(sum(chechon)):
        print(chechon)

    totalchechon = sum(chechon)




def ejercicio7():


    edad = int(input("Ingrese su edad:"))

    if edad >= 18:
        print("Bienvenido a la fiesta")

    else:
        print("Lo siento, eres muy joven")


def ejercicio8():

    c = input("ingrese una contraseña:")

    if c == "python123":
        print("¡Contraseña correcta! Acceso concedido.")

    else:
        print("¡Contraseña incorrecta, Autodestrucción en 5 minutos!")


def ejercicio9():

    Entero = int(input("Ingrese un numero entero:"))

    if Entero % 2 == 0:
        print("El numero es par: ")

    else:
        print("El numero es impar:")


def ejercicio10():

    Edad = int(input("Ingrese su edad:"))

    if Edad >= 65:
        print("Felicidades Tienes entrada gratuita al cine")

    else:
        print("Compra la entrada o raja de aca")



def ejercicio11():

    x = 6

    while x >= 1:
        x = x - 1
        print(x)
        if x == 0:
            print("¡Despegue!")


def ejercicio12():

    adivina  = int(input("Adivina el numero:"))

    while adivina !=  7:
     adivina = int(input("Ese no es el numero correcto, Intentalo de nuevo."))

    print("Adivinaste el numero correcto")
ejercicio12()



















