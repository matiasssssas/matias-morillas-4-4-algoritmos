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
    cursor.execute(
        "INSERT INTO medicamentos (nombre, categoria, precio, stock) VALUES (%s,%s,%s,%s)",
        (nombre, categoria, precio, stock)
    )
    db.commit()
    print("Medicamento agregado")
    db.close()

def mostrar_medicamento(id_med):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicamentos WHERE id=%s", (id_med,))
    dato = cursor.fetchone()
    if dato:
        print(dato)
    else:
        print("No existe")
    db.close()

def borrar_medicamento(id_med):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM medicamentos WHERE id=%s", (id_med,))
    db.commit()
    print("Medicamento borrado")
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
        "UPDATE medicamentos SET stock = stock - %s WHERE id=%s",
        (cantidad, id_medicamento)
    )
    db.commit()
    print("Venta registrada")
    db.close()

def mostrar_venta(id_venta):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("""
        SELECT v.id, m.nombre, m.categoria, v.fecha, v.cantidad
        FROM ventas v
        JOIN medicamentos m ON v.id_medicamento = m.id
        WHERE v.id = %s
    """, (id_venta,))
    dato = cursor.fetchone()
    if dato:
        print(dato)
    else:
        print("No existe")
    db.close()

def borrar_venta(id_venta):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM ventas WHERE id=%s", (id_venta,))
    db.commit()
    print("Venta borrada")
    db.close()

def stock_critico():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicamentos WHERE stock < 10")
    datos = cursor.fetchall()
    for d in datos:
        print(d)
    db.close()

def top_5_mas_vendidos():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("""
        SELECT m.nombre, SUM(v.cantidad) total
        FROM ventas v
        JOIN medicamentos m ON v.id_medicamento = m.id
        GROUP BY m.nombre
        ORDER BY total DESC
        LIMIT 5
    """)
    datos = cursor.fetchall()
    for d in datos:
        print(d)
    db.close()

def mas_vendidos_ultimo_mes():
    db = conectar()
    cursor = db.cursor()
    hoy = datetime.date.today()
    cursor.execute("""
        SELECT m.nombre, SUM(v.cantidad) total
        FROM ventas v
        JOIN medicamentos m ON v.id_medicamento = m.id
        WHERE MONTH(v.fecha)=%s AND YEAR(v.fecha)=%s
        GROUP BY m.nombre
        HAVING total > 5
    """, (hoy.month, hoy.year))
    datos = cursor.fetchall()
    for d in datos:
        print(d)
    db.close()

def calcular_total_ventas():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ventas")
    lista_ventas = cursor.fetchall()
    cursor.execute("SELECT * FROM medicamentos")
    lista_medicamentos = cursor.fetchall()

    total = 0

    for venta in lista_ventas:
        id_med = venta[1]
        cantidad = venta[3]
        for med in lista_medicamentos:
            if med[0] == id_med:
                precio = med[3]
                total += cantidad * precio

    print("Total:", total)
    db.close()


opcion = ""

while opcion != "11":
    print("\n1 Agregar medicamento")
    print("2 Registrar venta")
    print("3 Mostrar medicamento")
    print("4 Mostrar venta")
    print("5 Stock critico")
    print("6 Top 5 mas vendidos")
    print("7 Mas vendidos ultimo mes")
    print("8 Borrar medicamento")
    print("9 Borrar venta")
    print("10 Calcular total ventas")
    print("11 Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        agregar_medicamento(nombre, categoria, precio, stock)

    elif opcion == "2":
        id_med = int(input("ID medicamento: "))
        cantidad = int(input("Cantidad: "))
        registrar_venta(id_med, cantidad)

    elif opcion == "3":
        id_med = int(input("ID medicamento: "))
        mostrar_medicamento(id_med)

    elif opcion == "4":
        id_venta = int(input("ID venta: "))
        mostrar_venta(id_venta)

    elif opcion == "5":
        stock_critico()

    elif opcion == "6":
        top_5_mas_vendidos()

    elif opcion == "7":
        mas_vendidos_ultimo_mes()

    elif opcion == "8":
        id_med = int(input("ID medicamento: "))
        borrar_medicamento(id_med)

    elif opcion == "9":
        id_venta = int(input("ID venta: "))
        borrar_venta(id_venta)

    elif opcion == "10":
        calcular_total_ventas()

    elif opcion == "11":
        print("Fin")

    else:
        print("Opcion invalida")
