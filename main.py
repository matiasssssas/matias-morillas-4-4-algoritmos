static void Ejercicio1Triangulos()
{
    Console.WriteLine("Lado A:");
    double a = double.Parse(Console.ReadLine());
    Console.WriteLine("Lado B:");
    double b = double.Parse(Console.ReadLine());
    Console.WriteLine("Lado C:");
    double c = double.Parse(Console.ReadLine());

    if (a + b > c && a + c > b && b + c > a)
    {
        if (a == b && b == c) Console.WriteLine("Equilátero");
        else if (a != b && a != c && b != c) Console.WriteLine("Escaleno");
        else Console.WriteLine("Isósceles");

        if ((a * a) + (b * b) == (c * c) || (a * a) + (c * c) == (b * b) || (b * b) + (c * c) == (a * a))
        {
            Console.WriteLine("También es rectángulo");
        }
    }
    else
    {
        Console.WriteLine("No es válido");
    }
}

static void Ejercicio2Impuestos()
{
    Console.WriteLine("Sueldo:");
    double sueldo = double.Parse(Console.ReadLine());
    double impuesto = 0;

    if (sueldo > 60000) impuesto = (20000 * 0.15) + (30000 * 0.25) + ((sueldo - 60000) * 0.35);
    else if (sueldo > 30000) impuesto = (20000 * 0.15) + ((sueldo - 30000) * 0.25);
    else if (sueldo > 10000) impuesto = (sueldo - 10000) * 0.15;

    Console.WriteLine("Impuesto a pagar: " + impuesto);
}

static void Ejercicio3Cuadrante()
{
    Console.WriteLine("X:");
    double x = double.Parse(Console.ReadLine());
    Console.WriteLine("Y:");
    double y = double.Parse(Console.ReadLine());

    if (x == 0 && y == 0) Console.WriteLine("Origen");
    else if (x == 0) Console.WriteLine("Eje Y");
    else if (y == 0) Console.WriteLine("Eje X");
    else if (x > 0 && y > 0) Console.WriteLine("Cuadrante 1");
    else if (x < 0 && y > 0) Console.WriteLine("Cuadrante 2");
    else if (x < 0 && y < 0) Console.WriteLine("Cuadrante 3");
    else Console.WriteLine("Cuadrante 4");
}

static void Ejercicio4Aire()
{
    Console.WriteLine("Valor de aire:");
    int aire = int.Parse(Console.ReadLine());

    if (aire <= 50) Console.WriteLine("Buena");
    else if (aire <= 100) Console.WriteLine("Moderada");
    else if (aire <= 150) Console.WriteLine("Dañina para nenes");
    else if (aire <= 200) Console.WriteLine("Dañina");
    else Console.WriteLine("Peligrosa");
}

static void Ejercicio5Biciesto()
{
    Console.WriteLine("Año:");
    int año = int.Parse(Console.ReadLine());

    if ((año % 4 == 0 && año % 100 != 0) || (año % 400 == 0)) Console.WriteLine("Es biciesto");
    else Console.WriteLine("No es biciesto");
}

static void Ejercicio2Parte2Fibonacci()
{
    Console.WriteLine("Límite para Fibonacci:");
    int limite = int.Parse(Console.ReadLine());
    int fib1 = 0, fib2 = 1, fib3 = 0;

    while (fib1 < limite)
    {
        Console.Write(fib1 + " ");
        fib3 = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib3;
    }
    Console.WriteLine();
}

static void Ejercicio3Parte2Primos()
{
    Console.WriteLine("Número para saber si es primo:");
    int numPrimo = int.Parse(Console.ReadLine());
    int divisores = 0;

    for (int i = 1; i <= numPrimo; i++)
    {
        if (numPrimo % i == 0) divisores++;
    }

    if (divisores == 2) Console.WriteLine("Es primo");
    else Console.WriteLine("No es primo");
}

static void Ejercicio4Parte2Factores()
{
    Console.WriteLine("Número para factorizar:");
    int numFact = int.Parse(Console.ReadLine());
    int div = 2;

    while (numFact > 1)
    {
        if (numFact % div == 0)
        {
            Console.Write(div + " ");
            numFact = numFact / div;
        }
        else div++;
    }
    Console.WriteLine();
}

static void Ejercicio5Parte2Binario()
{
    Console.WriteLine("Número para pasar a binario:");
    int numDec = int.Parse(Console.ReadLine());
    string binario = "";

    if (numDec == 0) binario = "0";
    while (numDec > 0)
    {
        binario = (numDec % 2) + binario;
        numDec = numDec / 2;
    }
    Console.WriteLine("Binario: " + binario);
}
