import mysql.connector
import datetime

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="farmacity"
    )


def agregar_medicamento(nombre, categoria, precio, stock):
    db = conectar()
    cursor = db.cursor()

    sql = "INSERT INTO medicamentos (nombre, categoria, precio, stock) VALUES (%s,%s,%s,%s)"
    valores = (nombre, categoria, precio, stock)

    cursor.execute(sql, valores)
    db.commit()

    print("Medicamento agregado correctamente")
    db.close()


def mostrar_medicamento(id_med):
    db = conectar()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM medicamentos WHERE id = %s", (id_med,))
    resultado = cursor.fetchone()

    if resultado:
        print("Medicamento:", resultado)
    else:
        print("No existe ese medicamento")

    db.close()


def registrar_venta(id_medicamento, cantidad):
    db = conectar()
    cursor = db.cursor()

    fecha = datetime.date.today()

    cursor.execute(
        "INSERT INTO ventas (id_medicamento, fecha, cantidad) VALUES (%s,%s,%s)",
        (id_medicamento, fecha, cantidad)
    )

    cursor.execute(
        "UPDATE medicamentos SET stock = stock - %s WHERE id = %s",
        (cantidad, id_medicamento)
    )

    db.commit()
    print("Venta registrada")
    db.close()


def mostrar_venta(id_venta):
    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
        SELECT v.id, m.nombre, v.fecha, v.cantidad
        FROM ventas v
        JOIN medicamentos m ON v.id_medicamento = m.id
        WHERE v.id = %s
    """, (id_venta,))

    resultado = cursor.fetchone()

    if resultado:
        print("Venta:", resultado)
    else:
        print("No existe esa venta")

    db.close()


def stock_critico():
    db = conectar()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM medicamentos WHERE stock < 10")
    resultados = cursor.fetchall()

    print("Medicamentos con stock crítico:")
    for r in resultados:
        print(r)

    db.close()


opcion = ""

while opcion != "5":
    print("\n--- FARMACITY ---")
    print("1- Agregar medicamento")
    print("2- Registrar venta")
    print("3- Mostrar medicamento")
    print("4- Stock crítico")
    print("5- Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        agregar_medicamento(nombre, categoria, precio, stock)

    elif opcion == "2":
        id_med = int(input("ID medicamento: "))
        cantidad = int(input("Cantidad vendida: "))
        registrar_venta(id_med, cantidad)

    elif opcion == "3":
        id_med = int(input("ID medicamento: "))
        mostrar_medicamento(id_med)

    elif opcion == "4":
        stock_critico()

    elif opcion == "5":
        print("Programa finalizado")

    else:
        print("Opción inválida")
