// 1- Nivel "Básicos"1.1 Suma y Promedio:
int[] nums = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 };
int suma = 0;

foreach (int n in nums)
{
    suma += n;
}

double prom = (double)suma / nums.Length;

// Este código lo que hace es armar una lista de números, los recorre con un bucle
// para sumarlos todos en una variable y al final divide ese total por la cantidad
// de elementos para sacar el promedio.


// 1.2 Buscar el Mayor y el Menor:
int[] unArr = { 45, 12, 78, 3, 99, 21, 56, 8 };

int max = unArr[0];
int min = unArr[0];
int posMax = 0;
int posMin = 0;

for (int i = 1; i < unArr.Length; i++)
{
    if (unArr[i] > max)
    {
        max = unArr[i];
        posMax = i;
    }
    if (unArr[i] < min)
    {
        min = unArr[i];
        posMin = i;
    }
}

// Este código lo que hace es arrancar diciendo que el primer número es el más grande
// y el más chico a la vez. Después revisa los demás y, si encuentra uno mayor o menor,
// actualiza el valor y guarda en qué posición lo encontró.


// 2- Nivel "Intermedios"2.1-Invertir un Arreglo:
string[] nombres = { "Ana", "Juan", "Pedro", "Maria", "Luis" };

int i = 0;
int j = nombres.Length - 1;

while (i < j)
{
    string aux = nombres[i];
    nombres[i] = nombres[j];
    nombres[j] = aux;
    i++;
    j--;
}

// Este código lo que hace es agarrar la lista de nombres y darla vuelta en el lugar.
// Usa dos variables una al principio y otra al final que van cambiando los textos de posición
// hacia el centro usando un aux para no perder los datos






// 2.2-Filtrar y Copiar (Números Primos):
int[] arregloOriginal = new int[15];
Random generador = new Random();

for (int indice = 0; indice < arregloOriginal.Length; indice++)
{
    arregloOriginal[indice] = generador.Next(1, 51);
}

bool EsNumeroPrimo(int numero)
{
    if (numero < 2) return false;

    for (int divisor = 2; divisor < numero; divisor++)
    {
        if (numero % divisor == 0) return false;
    }
    return true;
}

int cantidadPrimos = 0;
foreach (int numero in arregloOriginal)
{
    if (EsNumeroPrimo(numero)) cantidadPrimos++;
}

int[] arregloPrimos = new int[cantidadPrimos];
int posicionPrimo = 0;
foreach (int numero in arregloOriginal)
{
    if (EsNumeroPrimo(numero))
    {
        arregloPrimos[posicionPrimo] = numero;
        posicionPrimo++;
    }
}

// Este código genera 15 números aleatorios entre 1 y 50,
// revisa cuáles son primos y los copia a un nuevo arreglo
// que tiene el tamaño para guardarlos sin dejar espacios vacíos.


// 2.3-Frecuencia de Elementos:
char[] arregloCaracteres = { 'a', 'b', 'a', 'c', 'b', 'a', 'd', 'c', 'c', 'e' };

for (int indiceExterior = 0; indiceExterior < arregloCaracteres.Length; indiceExterior++)
{
    int contador = 0;
    bool yaFueContado = false;

    for (int indiceInterior = 0; indiceInterior < indiceExterior; indiceInterior++)
    {
        if (arregloCaracteres[indiceInterior] == arregloCaracteres[indiceExterior])
        {
            yaFueContado = true;
            break;
        }
    }

    if (!yaFueContado)
    {


        for (int indiceConteo = 0; indiceConteo < arregloCaracteres.Length; indiceConteo++)
        {
            if (arregloCaracteres[indiceConteo] == arregloCaracteres[indiceExterior]) contador++;
        }
        Console.WriteLine($"El carácter '{arregloCaracteres[indiceExterior]}' aparece {contador} veces.");
    }
}

// Este código recorre el arreglo de caracteres y cuenta cuántas veces aparece cada uno,
// evitando repetir el conteo de los que ya fueron revisados.


// 3- Nivel "Avanzados"3.1-Rotación de Elementos:
int[] arregloNumeros = { 1, 2, 3, 4, 5 };
int cantidadRotaciones = 2;

cantidadRotaciones = cantidadRotaciones % arregloNumeros.Length;

int[] arregloResultado = new int[arregloNumeros.Length];

for (int indice = 0; indice < arregloNumeros.Length; indice++)
{
    int nuevaPosicion = (indice + cantidadRotaciones) % arregloNumeros.Length;
    arregloResultado[nuevaPosicion] = arregloNumeros[indice];
}

// el código rota los elementos del arreglo hacia la derecha la cantidad indicada.
// Si el número de rotaciones es mayor que el tamaño del arreglo, usa el operador % para optimizar.
