import mysql.connector

nombres = []
DNI = []

while True:
    print("1 Agregar")
    print("2 Mostrar")
    print("3 Buscar")
    print("4 Guardar en MySQL")
    print("5 Salir")

    op = input("Opcion: ")

    if op == "1":
        n = input("Nombre: ")
        t = input("DNI: ")
        nombres.append(n)
        DNI.append(t)

    elif op == "2":
        for i in range(len(nombres)):
            print(i, nombres[i], DNI[i])

    elif op == "3":
        b = input("Nombre a buscar: ")
        if b in nombres:
            i = nombres.index(b)
            print("Telefono:", DNI[i])
        else:
            print("No existe")

    elif op == "4":
        for i in range(len(nombres)):
            print(i, nombres[i], DNI[i])

        x = int(input("ID a guardar: "))

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="agenda"
        )

        cur = con.cursor()
        cur.execute(
            "INSERT INTO contacto (Numero, Telefono) VALUES (%s, %s)",
            (nombres[x], DNI[x])
        )

        con.commit()
        con.close()

        print("Guardado")

    elif op == "5":
        break

    else:
        print("Opcion incorrecta")