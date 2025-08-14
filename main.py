def ej1():
    saldo = 1000
    while True:
        print(f"\nSaldo actual: ${saldo}")
        print("Opciones: 1) Depositar  2) Retirar  3) Salir")
        opcion = input("Elegí una opción: ")

        try:
            if opcion == "1":
                monto = float(input("¿Cuánto querés depositar? "))
                if monto < 0:
                    print("No podés depositar un monto negativo.")
                else:
                    saldo += monto
            elif opcion == "2":
                monto = float(input("¿Cuánto querés retirar? "))
                if monto < 0:
                    print("No podés retirar un monto negativo.")
                elif monto > saldo:
                    print("No tenés suficiente saldo.")
                else:
                    saldo -= monto
            elif opcion == "3":
                print("¡Gracias por usar el simulador bancario!")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida. Usá números.")

ej1()

def ej2():
    try:
        peso = float(input("Ingresá tu peso en kg: "))
        altura = float(input("Ingresá tu altura en metros: "))
        imc = peso / (altura ** 2)
        print(f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
            print("Categoría: Bajo peso")
        elif imc < 25:
            print("Categoría: Normal")
        elif imc < 30:
            print("Categoría: Sobrepeso")
        else:
            print("Categoría: Obesidad")
    except ValueError:
        print("Entrada inválida. Usá números.")
    except ZeroDivisionError:
        print("La altura no puede ser cero.")

ej2()

def ej3():
    vocales = "aeiou"

    while True:
        frase = input("Ingresá una frase (o 'agusfortnite2008' para salir): ")
        if frase == "agusfortnite2008":
            print("¡Programa finalizado!")
            break

        for v in vocales:
            nueva = ""
            for letra in frase:
                if letra.lower() in "aeiou":
                    nueva += v
                else:
                    nueva += letra
            print(nueva)

ej3()

def ej4():
    frase = input("Ingresá una frase: ")
    palabras = frase.split()
    invertidas = [palabra[::-1] for palabra in palabras]
    print("Frase con palabras invertidas:")
    print(" ".join(invertidas))

ej4()

def ej5():
    nombres = []

    while True:
        print("\nMenú:")
        print("1) Agregar nombre")
        print("2) Ver nombre por posición")
        print("3) Salir")
        opcion = input("Elegí una opción: ")

        try:
            if opcion == "1":
                nombre = input("Ingresá un nombre: ")
                nombres.append(nombre)
            elif opcion == "2":
                if not nombres:
                    print("La lista está vacía.")
                else:
                    pos = int(input(f"Ingresá una posición (1 a {len(nombres)}): "))
                    print(f"Nombre en posición {pos}: {nombres[pos - 1]}")
            elif opcion == "3":
                print("¡Programa finalizado!")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida. Usá números.")
        except IndexError:
            print("Posición fuera de rango.")

ej5()
