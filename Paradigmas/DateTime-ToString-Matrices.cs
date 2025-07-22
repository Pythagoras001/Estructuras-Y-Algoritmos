using System;

class ApuntesProgramacion
{
    static void Main()
    {
        // -------------------- DateTime --------------------
        // Obtener la fecha y hora actual
        DateTime ahora = DateTime.Now;
        Console.WriteLine("Fecha y hora actual: " + ahora);

        // Crear una fecha específica (año, mes, día)
        DateTime fechaNacimiento = new DateTime(2000, 5, 15);
        Console.WriteLine("Fecha de nacimiento: " + fechaNacimiento);

        // Sumar días, meses o años
        DateTime enDiezDias = ahora.AddDays(10);
        DateTime enTresMeses = ahora.AddMonths(3);
        Console.WriteLine("En 10 días: " + enDiezDias);
        Console.WriteLine("En 3 meses: " + enTresMeses);

        // Calcular diferencia entre fechas
        TimeSpan diferencia = ahora - fechaNacimiento;
        Console.WriteLine("Días vividos: " + diferencia.TotalDays);

        // -------------------- ToString --------------------
        // ToString() de DateTime con formatos personalizados
        Console.WriteLine("Formato corto: " + ahora.ToString("d"));         // Solo fecha
        Console.WriteLine("Formato largo: " + ahora.ToString("D"));        // Fecha larga
        Console.WriteLine("Hora (24h): " + ahora.ToString("HH:mm"));       // Hora 24h
        Console.WriteLine("Hora (12h): " + ahora.ToString("hh:mm tt"));    // Hora 12h con AM/PM

        // ToString() con interpolación y formato numérico
        double numero = 1234.56789;
        Console.WriteLine("Número con 2 decimales: " + numero.ToString("F2"));      // 1234.57
        Console.WriteLine("Formato moneda: " + numero.ToString("C"));              // $1,234.57 (depende de región)
        Console.WriteLine($"Número en notación científica: {numero:E2}");          // 1.23E+003

        // -------------------- Matrices --------------------
        // Declaración de matriz de una dimensión
        int[] edades = new int[] { 18, 25, 30, 40 };
        Console.WriteLine("\nMatriz unidimensional:");
        for (int i = 0; i < edades.Length; i++)
        {
            Console.WriteLine($"Edad[{i}] = {edades[i]}");
        }

        // Modificar un valor
        edades[1] = 26;

        // Matriz bidimensional (filas x columnas)
        int[,] matriz = new int[2, 3] {
            { 1, 2, 3 },
            { 4, 5, 6 }
        };
        Console.WriteLine("\nMatriz bidimensional:");
        for (int fila = 0; fila < matriz.GetLength(0); fila++)
        {
            for (int col = 0; col < matriz.GetLength(1); col++)
            {
                Console.Write(matriz[fila, col] + "\t");
            }
            Console.WriteLine();
        }

        // Acceso y modificación
        matriz[1, 2] = 99;

        // Matriz de 3 dimensiones (opcional para clases más avanzadas)
        int[,,] cubo = new int[2, 2, 2]
        {
            { {1, 2}, {3, 4} },
            { {5, 6}, {7, 8} }
        };
        Console.WriteLine("\nElemento cubo[1,1,1] = " + cubo[1,1,1]); // 8
    }
}
