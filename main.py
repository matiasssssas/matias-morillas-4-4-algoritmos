def ej1():

nombres = ["valentina","sebastian","matias","ignacio","jeremias","frick","alba","bruno","leonel"]


palabra_mas_larga = ""
for nombre in nombres:
   if len(nombre) > len(palabra_mas_larga):
       palabra_mas_larga = nombre


print("la palabra con mas caracteres es:", palabra_mas_larga)


ej1()


def ej2():

vocales = "aeiouAEIOU"
contador = 0


for nombre in nombres:
   for letra in nombre:
       if letra in vocales:
           contador += 1


print("Cantidad total de vocales",contador)


ej2()


def ej3():

numeros = [2,5,8,3,7,1,4,6,9,10]
factor = 3
nueva_lista = []


for numero in numeros:
   nueva_lista.append(numero * factor)


print("Lista multiplicada:",nueva_lista)


ej3()
