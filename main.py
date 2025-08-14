def ej1():
   try:
       num1 = float(input("Ingresa el primer numero:"))
       num2 = float(input("Ingresa el segundo numero:"))
       resultado = num1 / num2
       print(f"El resultado de la divison es: {resultado}")
   except ZeroDivisionError:
       print("No se puede divir por cero")
   except ValueError:
       print("Porfavor, ingresa solo numeros.")
   finally:
       print("Fin del intento de division.")


ej1()


def ej2():
   while True:
       try:
           edad = int(input("Ingrese tu edad"))
           print(f"Tu edad es: {edad}")
           break
       except ValueError:
           print("Eso no parece un numero entero. Intenta con otro.")
       finally:
           print("intento de entrar completado.")


ej2()


def ej3():
   nombres = ["Ana", "Pedro", "Sofía"]


   try:
       indice = int(input("ingrese un indice (0 a 2): "))
       print(f"el nombre en la posicion {indice} es: {nombres[indice]}")
   except IndexError:
       print("Ese indice esta  fuera del rango de la lista.")
   except ValueError:
       print("Debes ingresar un numero entero.")


ej3()


def ej4():
   try:
       num1 = int(input("ingrese el primer numero: "))
       num2 = int(input("ingrese el segundo numero: "))
       print(f"La suma es: {num1 + num2}")
   except ValueError:
       print("Uno o ambos valores no son numeros enteros.")


ej4()


def ej5():
   try:
       a = float(input("Ingresa el dividendo:"))
       b = float(input("Ingresa el divisor:"))
       resultado = a / b
       print(f"El resultado de la division es: {resultado}")
   except ZeroDivisionError:
       print("No se puede dividir por cero")
   except ValueError:
       print("Ingresaste un valor no numerico")
   finally:
       print("Fin del programa del calculo")


ej5()