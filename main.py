import mysql.connector
from datetime import date

# ---------- CONEXIÓN ---------- LO PUSE YO ESTO NO ES CHATGPT GAGA
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="farmacia"
    )

# ---------- MEDICAMENTOS ---------- LO PUSE YO ESTO NO ES CHATGPT GAGA
def agregar_medicamento(nombre, categoria, precio, stock):
    db = conectar()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO medicamentos (nombre, categoria, precio, stock) VALUES (%s,%s,%s,%s)",
        (nombre, categoria, precio, stock)
    )
    db.commit()
    db.close()

def borrar_medicamento(id_med):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM medicamentos WHERE id=%s", (id_med,))
    db.commit()
    db.close()

def mostrar_medicamento(id_med):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicamentos WHERE id=%s", (id_med,))
    print(cursor.fetchone())
    db.close()

# ---------- VENTAS ---------- LO PUSE YO ESTO NO ES CHATGPT GAGA
def registrar_venta(id_medicamento, cantidad):
    db = conectar()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO ventas (id_medicamento, fecha, cantidad) VALUES (%s,%s,%s)",
        (id_medicamento, date.today(), cantidad)
    )

    cursor.execute(
        "UPDATE medicamentos SET stock = stock - %s WHERE id = %s",
        (cantidad, id_medicamento)
    )

    db.commit()
    db.close()

def borrar_venta(id_venta):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM ventas WHERE id=%s", (id_venta,))
    db.commit()
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
    print(cursor.fetchone())
    db.close()

# ---------- REPORTES ---------- LO PUSE YO ESTO NO ES CHATGPT GAGA
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
    print(cursor.fetchall())
    db.close()

def stock_critico():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicamentos WHERE stock < 10")
    print(cursor.fetchall())
    db.close()

def mas_vendidos_mes():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("""
        SELECT m.nombre, COUNT(v.id)
        FROM ventas v
        JOIN medicamentos m ON v.id_medicamento = m.id
        WHERE MONTH(v.fecha) = MONTH(CURDATE())
        GROUP BY m.nombre
        HAVING COUNT(v.id) > 5
    """)
    print(cursor.fetchall())
    db.close()

# ---------- LISTAS + TOTAL ---------- LO PUSE YO ESTO NO ES CHATGPT GAGA
def calcular_total_ventas():
    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
        SELECT v.cantidad, m.precio
        FROM ventas v
        JOIN medicamentos m ON v.id_medicamento = m.id
    """)
    datos = cursor.fetchall()

    total = 0
    for cantidad, precio in datos:
        total += cantidad * precio

    print("Total de ventas: $", total)
    db.close()

# ---------- PRUEBA ---------- LO PUSE YO ESTO NO ES CHATGPT GAGA
if __name__ == "__main__":
    agregar_medicamento("Paracetamol", "Analgésico", 1200, 50)
    registrar_venta(1, 3)

    mostrar_medicamento(1)
    mostrar_venta(1)

    top_5_mas_vendidos()
    stock_critico()
    mas_vendidos_mes()
    calcular_total_ventas()
