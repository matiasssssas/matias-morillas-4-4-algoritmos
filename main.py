def ejercicio1():

    informacion_personal = {

       "nombre": "Matias",
       "edad": 100,
       "ciudad": "Buenos aires",
       "Profesion": "Tecnico"

    }

    print(informacion_personal)



def ejercicio2():

    informacion_personal = {

        "ciudad": "Cordoba",
        "Profesion": "mecanico",
        "telefono": 1136221134,

    }

    print(informacion_personal)



def ejercicio3():

    calificaciones = {

        "Matematicas": 10,
        "Lengua": 10,
        "Ciencias": 10,

    }

    print(calificaciones["Matematicas"])



def ejercicio4():

    calificaciones = {

        "Matematicas": 2,
        "Lengua": 3,
        "Ciencias": 5

    }

    promedio = sum(calificaciones.values())
    len(calificaciones)
    print("El promedio es:", promedio)



def ejercicio5():

    Paises = {

        "Argentina": "La plata",
        "Uruguay": "Montevideo",
        "Chile":  "Santiago del chile",

    }

    pais = input("Ingrese un pais: ")
    if pais in Paises:
        print("La capital de", pais, " es: ", Paises[pais])
    else:
        print("Ese pais no esta en el diccionario")



def ejercicio6():

    precios = {

        "Carne": 2000,
        "Durazno": 1000,
        "Yogurt": 500,

    }

    producto = input("Ingrese un producto:")
    cantidad = print(input("Ingrese la cantidad:"))

    if producto in precios:
        total = precios[producto] * cantidad
        print("El costo total es:", total)
    else:
        print("Ese producto no existe")



def ejercicio7():

    informacion_personal = {

        "ciudad": "Cordoba",
        "Profesion": "mecanico",
        "telefono": 1136221134,

    }

    del informacion_personal["telefono"]
    print(informacion_personal)



def ejercicio8():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    print(dic.get("a") )
    print(dic.get("z"))



def ejercicio9():
    dic = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    dic2 = {
        "d": 4,
        "f": 5,
        "g": 3
    }

    dic3 = dic|dic2

    print(dic3)
























