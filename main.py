import random


palabras = ["programacion", "python", "computadora", "teclado", "pantalla", "raton", "internet"]
palabra = random.choice(palabras)
estado = ["_"] * len(palabra)
letras = set()
intentos = 7


print("Adivina la palabra:", " ".join(estado))


while intentos > 0 and "_" in estado:
   letra = input("Letra: ").lower()
   if len(letra) != 1 or not letra.isalpha():
       print("Ingresa solo una letra.")
       continue
   if letra in letras:
       print("Ya intentaste esa letra.")
       continue
   letras.add(letra)
   if letra in palabra:
       for i, c in enumerate(palabra):
           if c == letra:
               estado[i] = letra
   else:
       intentos -= 1
       print(f"Letra incorrecta. Te quedan {intentos} intentos.")
   print(" ".join(estado))


if "_" not in estado:
   print(f"¡Ganaste! La palabra es {palabra}")
else:
   print(f"Perdiste. La palabra era {palabra}

