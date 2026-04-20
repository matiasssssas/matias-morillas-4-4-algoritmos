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
    else if (x > 0 && y > 0) Console.WriteLine("Cuadrante I");
    else if (x < 0 && y > 0) Console.WriteLine("Cuadrante II");
    else if (x < 0 && y < 0) Console.WriteLine("Cuadrante III");
    else Console.WriteLine("Cuadrante IV");
}

static void Ejercicio4Aire()
{
    Console.WriteLine("Valor de aire:");
    int aire = int.Parse(Console.ReadLine());

    if (aire <= 50) Console.WriteLine("Buena");
    else if (aire <= 100) Console.WriteLine("Moderada");
    else if (aire <= 150) Console.WriteLine("Dañina para sensibles");
    else if (aire <= 200) Console.WriteLine("Dañina");
    else Console.WriteLine("Peligrosa");
}

static void Ejercicio5Bisiesto()
{
    Console.WriteLine("Año:");
    int anio = int.Parse(Console.ReadLine());

    if ((anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0)) Console.WriteLine("Es bisiesto");
    else Console.WriteLine("No es bisiesto");
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

static void Ejercicio6Collatz()
{
    Console.WriteLine("Ingresá un número para la conjetura de Collatz:");
    int n = int.Parse(Console.ReadLine());
    int pasos = 0;

    while (n > 1)
    {
        if (n % 2 == 0)
        {
            n = n / 2;
        }
        else
        {
            n = (n * 3) + 1;
        }
        pasos++;
    }

    Console.WriteLine("Llegó a 1 en " + pasos + " pasos.");
}

static void Ejercicio7RaizNewton()
{
    Console.WriteLine("Ingresá un número para calcular su raíz cuadrada:");
    double numero = double.Parse(Console.ReadLine());
    double x = numero;
    double raiz = 0;

    while (true)
    {
        raiz = 0.5 * (x + (numero / x));

        if ((x - raiz) < 0.0001 && (x - raiz) > -0.0001)
        {
            break;
        }
        x = raiz;
    }

    Console.WriteLine("La raíz cuadrada aproximada es: " + raiz);
}

static void Ejercicio8RomboHueco()
{
    Console.WriteLine("Ingresá el tamaño N para el rombo:");
    int n = int.Parse(Console.ReadLine());

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i; j++) Console.Write(" ");

        if (i == 1)
        {
            Console.WriteLine("*");
        }
        else
        {
            Console.Write("*");
            for (int j = 1; j <= 2 * i - 3; j++) Console.Write(" ");
            Console.WriteLine("*");
        }
    }

    for (int i = n - 1; i >= 1; i--)
    {
        for (int j = 1; j <= n - i; j++) Console.Write(" ");

        if (i == 1)
        {
            Console.WriteLine("*");
        }
        else
        {
            Console.Write("*");
            for (int j = 1; j <= 2 * i - 3; j++) Console.Write(" ");
            Console.WriteLine("*");
        }
    }
}

static void Ejercicio14PeajeInteligente()
{
    double totalRecaudado = 0;
    int totalVehiculos = 0;
    string tipoVehiculo = "";

    while (tipoVehiculo != "cierre")
    {
        Console.WriteLine("Ingresá tipo de vehículo (moto, auto, camion) o 'cierre' para terminar:");
        tipoVehiculo = Console.ReadLine();

        if (tipoVehiculo == "cierre")
        {
            break;
        }

        double costo = 0;

        if (tipoVehiculo == "moto")
        {
            costo = 5.00;
        }
        else if (tipoVehiculo == "auto")
        {
            costo = 10.00;
            Console.WriteLine("¿Cuántos pasajeros lleva?");
            int pasajeros = int.Parse(Console.ReadLine());

            if (pasajeros >= 3)
            {
                costo = costo * 0.50;
            }
        }
        else if (tipoVehiculo == "camion")
        {
            Console.WriteLine("¿Cuántos ejes tiene?");
            int ejes = int.Parse(Console.ReadLine());
            costo = 15.00 * ejes;
        }

        Console.WriteLine("¿A qué hora pasó? (Ingresá solo la hora, ej: 8 o 17):");
        int hora = int.Parse(Console.ReadLine());

        if ((hora >= 6 && hora <= 9) || (hora >= 17 && hora <= 20))
        {
            costo = costo + (costo * 0.20);
        }

        Console.WriteLine("Total a cobrar por este vehículo: $" + costo);
        totalRecaudado = totalRecaudado + costo;
        totalVehiculos++;
    }

    Console.WriteLine("Total recaudado: $" + totalRecaudado);

    if (totalVehiculos > 0)
    {
        Console.WriteLine("Promedio de cobro por vehículo: $" + (totalRecaudado / totalVehiculos));
    }
}

static void Ejercicio15SimulacionCredito()
{
    Console.WriteLine("Ingresá tu edad:");
    int edad = int.Parse(Console.ReadLine());

    if (edad < 18 || edad > 75)
    {
        Console.WriteLine("Crédito rechazado automáticamente por la edad.");
    }
    else
    {
        Console.WriteLine("Ingresá tus ingresos mensuales:");
        double ingresos = double.Parse(Console.ReadLine());

        Console.WriteLine("Ingresá tu puntaje crediticio (0 a 1000):");
        int puntaje = int.Parse(Console.ReadLine());

        Console.WriteLine("Ingresá el monto solicitado:");
        double monto = double.Parse(Console.ReadLine());

        double interes = 0;
        bool aprobado = true;

        if (puntaje > 800)
        {
            interes = 0.05;
        }
        else if (puntaje >= 600 && puntaje <= 800)
        {
            interes = 0.12;
        }
        else
        {
            Console.WriteLine("Su puntaje es menor a 600. ¿Tiene un aval? (si/no):");
            string aval = Console.ReadLine();
            if (aval == "si")
            {
                interes = 0.15;
            }
            else
            {
                aprobado = false;
            }
        }

        if (aprobado == false)
        {
            Console.WriteLine("Crédito rechazado por falta de aval.");
        }
        else
        {
            double deudaTotal = monto + (monto * interes);
            double topeCuota = ingresos * 0.30;

            Console.WriteLine("Ingresá en cuántas cuotas (plazo) querés pagar:");
            int plazo = int.Parse(Console.ReadLine());

            double cuotaMensual = deudaTotal / plazo;

            while (cuotaMensual > topeCuota)
            {
                Console.WriteLine("La cuota supera el 30% de su ingreso.");
                Console.WriteLine("Ingresá un plazo mayor para bajar la cuota o ingresá '0' para cancelar:");
                plazo = int.Parse(Console.ReadLine());

                if (plazo == 0)
                {
                    aprobado = false;
                    break;
                }

                cuotaMensual = deudaTotal / plazo;
            }

            if (aprobado == true)
            {
                Console.WriteLine("¡Solicitud Aprobada! Apta para su sueldo.");
                Console.WriteLine("Mes | Pago | Saldo Restante");

                double saldo = deudaTotal;

                for (int i = 1; i <= plazo; i++)
                {
                    saldo = saldo - cuotaMensual;
                    if (saldo < 0) saldo = 0;
                    Console.WriteLine(i + " | $" + cuotaMensual + " | $" + saldo);
                }
            }
            else
            {
                Console.WriteLine("Solicitud cancelada.");
            }
        }
    }
}
