import random

# Lista de nombres ( aleatorio )
nombres = [
    "Juan", "Carlos", "Luis", "Miguel", "Pedro", "Diego", "Fernando", "Jorge",
    "Andrés", "Mario", "Sergio", "Alberto", "Raúl", "Ricardo", "Esteban",
    "Héctor", "José", "David", "Antonio", "Rafael", "Francisco", "Gustavo",
    "Alejandro", "Emilio", "Eduardo", "Martin", "Oscar", "Pablo", "Ricardo"
]

posiciones = ["Delantero", "Mediocampista", "Defensor", "Arquero"]

def generar_equipo():
    equipo = []
    usados = set()  # evitar nombres repetidos en un mismo equipo
    while len(equipo) < 23:
        nombre = random.choice(nombres)
        if nombre in usados:
            continue
        usados.add(nombre)
        valoracion = random.randint(50, 100)
        posicion = random.choice(posiciones)
        equipo.append([nombre, posicion, valoracion])
    return equipo

def valoracion_total(equipo):
    return sum(jugador[2] for jugador in equipo)

def imprimir_equipo(equipo, nombre_equipo):
    print(f"Equipo {nombre_equipo}:")
    print(f"{'Nombre':10} {'Posición':15} {'Valoración':10}")
    for j in equipo:
        print(f"{j[0]:10} {j[1]:15} {j[2]:10}")
    print(f"Valoración total: {valoracion_total(equipo)}\n")

# equipos
equipo1 = generar_equipo()
equipo2 = generar_equipo()

# equipos
imprimir_equipo(equipo1, "1")
imprimir_equipo(equipo2, "2")

# Comparar
total1 = valoracion_total(equipo1)
total2 = valoracion_total(equipo2)

if total1 > total2:
    print("El equipo 1 tiene más chances de ganar según su valoración.")
elif total2 > total1:
    print("El equipo 2 tiene más chances de ganar según su valoración.")
else:
    print("Ambos equipos tienen la misma valoración total, es un empate técnico.")