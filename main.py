palos = ["Picas", "Tréboles", "Diamantes", "Corazones"]

mazo = []


def convertir_carta(num):
    if num == 1:
        return "A"
    elif num == 11:
        return "J"
    elif num == 12:
        return "Q"
    elif num == 13:
        return "K"
    else:
        return str(num)

# valor chips
def valor_chips(carta):
    try:
        if carta == "A":
            return 11
        elif carta in ["J", "Q", "K"]:
            return 10
        else:
            return int(carta)
    except ValueError:

        return 0

# genero mazo
for palo in palos:
    for num in range(1, 14):
        carta = convertir_carta(num)
        mazo.append([carta, palo])

# valor total
valor_total = 0
for carta, palo in mazo:
    valor_total += valor_chips(carta)

# mazo y total chips
for carta, palo in mazo:
    print(f"{carta} de {palo}")

print("\nValor total de chips en el mazo:", valor_total)


