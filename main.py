def ejercicio1():


   productos = [
       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]


   for producto in productos:
       print(producto["nombre"])




def ejercicio2():


   productos = [


       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]


   total = 0
   for producto in productos:
       total = total + producto["precio"]
   print("La suma total es:", total)




def ejercicio3():


   productos = [


       {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
       {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
       {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
       {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}
   ]
   productos.append("valorant")
   print(productos)




def ejercicio4():


   estudiantes = [
       {"nombre": "Ana", "edad": 21, "calificacion": 90},
       {"nombre": "Luis", "edad": 22, "calificacion": 95},
       {"nombre": "Marta", "edad": 20, "calificacion": 85}
   ]


   estudiantes[2]["edad"] = 1000
   print(estudiantes[2])




def ejercicio5():


   estudiantes = [
       {"nombre": "Ana", "edad": 21, "calificacion": 90},
       {"nombre": "Luis", "edad": 22, "calificacion": 95},
       {"nombre": "Marta", "edad": 20, "calificacion": 85}
   ]


   notamejor = estudiantes[0]
   for estudiante in estudiantes [1:]:
       if estudiante["calificacion"] > notamejor["calificacion"]:
           estudiantemejor = estudiante
       print("estudiante con la mejor calificacion", estudiantemejor)




def ejercicio6():


   libros = [
       {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
       {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
       {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
   ]


   titulos = []
   for libro in libros:
       titulos.append(libro["titulo"])


   print(titulos)




def ejercicio7():


   libros = [
       {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
       {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
       {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
   ]


   libros = [libro for libro in libros if libro["titulo"] != "Don Quijote"]


   libros.append({"titulo": "Don Quijote", "autor": "Miguel de Cervantes"})


   print(libros)




def ejercicio8():


   libros = [
       {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
       {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
       {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
   ]


   for libro in libros:
       libro["disponible"] = True


   print(libros)