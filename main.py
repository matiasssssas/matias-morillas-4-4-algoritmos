using System;
using System.Collections.Generic;

namespace PixelStore
{
// ESTRUCTURA BASE
struct Videojuego
{
public int Id;
public string Titulo;
public double Precio;
public int Stock;
}
// QUE HACE ESTA PARTE: Es el molde para agrupar los datos de un juego (Id, Titulo, Precio, Stock).

class Program
{
// VARIABLES GLOBALES
static Videojuego[] inventario = new Videojuego[3];
static string[,] gondolas = new string[2, 2];
static Queue<string> cola = new Queue<string>();
// QUE HACE ESTA PARTE: Crea el vector de juegos, la matriz de gondolas y la cola de clientes.

// FUNCION PRINCIPAL Y MENU
static void Main()
{
inventario[0] = new Videojuego { Id = 1, Titulo = "FIFA", Precio = 45000, Stock = 5 };
inventario[1] = new Videojuego { Id = 2, Titulo = "GTA", Precio = 30000, Stock = 2 };
inventario[2] = new Videojuego { Id = 3, Titulo = "Zelda", Precio = 50000, Stock = 0 };

gondolas[0, 0] = "FIFA";
gondolas[0, 1] = "Vacio";
gondolas[1, 0] = "GTA";
gondolas[1, 1] = "Zelda";

int opcion = 0;

do
{
Console.WriteLine("Menu PixelStore");
Console.WriteLine("1 Ver catalogo");
Console.WriteLine("2 Ver ubicacion en gondolas");
Console.WriteLine("3 Registrar cliente");
Console.WriteLine("4 Atender cliente");
Console.WriteLine("5 Salir");
Console.Write("Elegi una opcion: ");

int.TryParse(Console.ReadLine(), out opcion);

if (opcion == 1) MostrarCatalogo();
if (opcion == 2) ConsultarGondola();
if (opcion == 3) RegistrarCliente();
if (opcion == 4) AtenderCliente();

} while (opcion != 5);
}
// QUE HACE ESTA PARTE: Carga los datos iniciales y corre el menu principal en bucle.

// MODULO 1: CATALOGO
static void MostrarCatalogo()
{
for (int i = 0; i < inventario.Length; i++)
{
Console.WriteLine($"ID: {inventario[i].Id} | Titulo: {inventario[i].Titulo} | Stock: {inventario[i].Stock}");
}
}
// QUE HACE ESTA PARTE: Muestra la lista completa de videojuegos y su stock.

// MODULO 2: GONDOLAS
static void ConsultarGondola()
{
Console.Write("Ingresa la fila (0 o 1): ");
int fila = int.Parse(Console.ReadLine());

Console.Write("Ingresa la columna (0 o 1): ");
int columna = int.Parse(Console.ReadLine());

Console.WriteLine($"En esa posicion esta: {gondolas[fila, columna]}");
}
// QUE HACE ESTA PARTE: Busca qué juego hay en la matriz segun la fila y columna ingresadas.

// MODULO 3: COLA DE CLIENTES
static void RegistrarCliente()
{
Console.Write("Nombre del cliente: ");
string nombre = Console.ReadLine();
cola.Enqueue(nombre);
Console.WriteLine($"Cliente agregado. Hay {cola.Count} en fila.");
}
// QUE HACE ESTA PARTE: Agrega un cliente al final de la fila usando Enqueue().

// MODULO 4: VENTA Y ATENCION
static void AtenderCliente()
{
if (cola.Count > 0)
{
string actual = cola.Peek();
Console.WriteLine($"Siguiente en la fila: {actual}");

Console.Write("Ingresa el ID del juego que compra: ");
int id = int.Parse(Console.ReadLine());

for (int i = 0; i < inventario.Length; i++)
{
if (inventario[i].Id == id)
{
if (inventario[i].Stock > 0)
{
inventario[i].Stock--;
cola.Dequeue();
Console.WriteLine("Venta exitosa");
}
else
{
Console.WriteLine("No hay stock");
}
return;
}
}
Console.WriteLine("ID incorrecto");
}
else
{
Console.WriteLine("La fila esta vacia");
}
}
// QUE HACE ESTA PARTE: Procesa la venta, resta stock y saca al cliente de la cola con Dequeue().
}
}
