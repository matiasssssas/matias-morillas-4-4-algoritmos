import mysql.connector
from mysql.connector import errorcode

cursor = None
cnx = None

def ConectarBase():
    global cnx, cursor

    try:
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="telefono")
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('El numero o telefono incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)


nombres = ["Matias,chechon,brunito"]
numeros = [1123361112,1120435676,1109504040]

while True:
        print("--- Menú ---")
        print("1) Añadir contacto")
        print("2) Mostrar contactos")
        print("3) Buscar contacto por nombre")
        print("4) Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            numero = input("Número: ")
            nombres.append(nombre)
            numeros.append(numero)
            print("Contacto añadido!")



