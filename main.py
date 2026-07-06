public static int busquedaL(int[] arreglo, int numero)
{
 
    for (int i = 0; i < arreglo.Length; i++)
    {
       
        if (arreglo[i] == numero)
        {
            return i;
        }
    }


    public static int productoEscalar(int[] A, int[] B)
{
    int resultado = 0;

 
   
    for (int i = 0; i < A.Length; i++)
    {
       
        resultado += A[i] * B[i];
    }

   
    return resultado;
}

    public static int[] ordenar(int[] arreglo)
{
    int n = arreglo.Length;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {

            if (arreglo[j] > arreglo[j + 1])
            {
                int temp = arreglo[j];
                arreglo[j] = arreglo[j + 1];
                arreglo[j + 1] = temp;
            }
        }
    }
   
    return arreglo;

}

public static int EncontrarFilaMaximoElemento(int[,] matriz)
{
    int filas = matriz.GetLength(0);
    int columnas = matriz.GetLength(1);
    
    int maximo = matriz[0, 0];
    int filaMaximo = 0;

    for (int i = 0; i < filas; i++)
    {
        for (int j = 0; j < columnas; j++)
        {
            if (matriz[i, j] > maximo)
            {
                maximo = matriz[i, j];
                filaMaximo = i;
            }
        }
    }

    return filaMaximo;
}

public static int[] BuscarPosicion(int[,] matriz, int valor)
{
    int filas = matriz.GetLength(0);
    int columnas = matriz.GetLength(1);

    for (int i = 0; i < filas; i++)
    {
        for (int j = 0; j < columnas; j++)
        {
            if (matriz[i, j] == valor)
            {
                return new int[] { i, j };
            }
        }
    }

    return new int[] { -1, -1 };
}

