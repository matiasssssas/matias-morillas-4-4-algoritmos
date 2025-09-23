import random

nombres = [ "Sofía", "Mateo", "Valentina", "Sebastián", "Isabella", "Alejandro",
            "Camila", "Santiago", "Luciana", "Nicolás", "Martina", "Benjamín", "Valeria",
            "Joaquín", "Victoria", "Gabriel", "Emilia", "Samuel", "Julieta", "Daniel", "Antonella",
            "Diego", "Rafaela", "Felipe", "Mariana", "Emmanuel", "Catalina", "Lucas", "Agostina", "Andrés",
            "Constanza", "Ezequiel", "Bianca", "Ignacio", "Delfina", "Agustín", "Florencia", "Gastón",
            "Guadalupe", "Hernán", "Julia", "Javier", "Laura", "Leonardo", "Magdalena", "Martín", "Micaela",
            "Patricio", "Paulina", "Ramiro" ]


apellidos = [ "García", "Rodríguez", "González", "Fernández", "López", "Martínez",
              "Sánchez", "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz",
              "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres",
              "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina", "Castro",
              "Suárez", "Ortega", "Rubio", "Delgado", "Morales", "Ortiz", "Marín", "Iglesias", "Núñez",
              "Medina", "Cortés", "Cano", "Flores", "Herrera", "Gallego", "Vega", "Castillo", "Santos",
              "Reyes" ]

clientes = []
for i in range(len(nombres)):
    cliente = {
        "id": i + 1,
        "nombre": nombres[i],
        "apellido": apellidos[i],
        "saldo": random.randint(500, 1500)
    }
    clientes.append(cliente)


def mostrar_clientes():
    for c in clientes:
        print(f"ID:{c['id']} - {c['nombre']} {c['apellido']} - Saldo:${c['saldo']}")


def buscar_cliente(id_buscar):
    for c in clientes:
        if c["id"] == id_buscar:
            print(f"Cliente encontrado: {c['nombre']} {c['apellido']} - Saldo:${c['saldo']}")
            return
    print("Cliente no encontrado.")


def depositar(id_cliente, monto):
    for c in clientes:
        if c["id"] == id_cliente:
            c["saldo"] += monto
            print(f"Nuevo saldo de {c['nombre']}: ${c['saldo']}")
            return


def retirar(id_cliente, monto):
    for c in clientes:
        if c["id"] == id_cliente:
            if c["saldo"] >= monto:
                c["saldo"] -= monto
                print(f"Nuevo saldo de {c['nombre']}: ${c['saldo']}")
            else:
                print("Saldo insuficiente.")
            return


print("LISTA INICIAL DE CLIENTES:")
mostrar_clientes()

print("\nBUSCAR CLIENTE CON ID 2:")
buscar_cliente(2)

print("\nDEPOSITAR 200 A CLIENTE 1:")
depositar(1, 200)

print("\nRETIRAR 100 DE CLIENTE 1:")
retirar(1, 100)

print("\nLISTA FINAL DE CLIENTES:")
mostrar_clientes()



