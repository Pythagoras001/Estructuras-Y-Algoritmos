using System;
using System.Collections.Generic;
using System.Linq;

namespace ApunteFuncionesAnonimas
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("=== Funciones Anónimas y Expresiones Lambda ===\n");

            // ----------------------------------------
            // 1. FUNCIÓN ANÓNIMA CON DELEGADO
            // ----------------------------------------
            Func<int, int> cuadrado = delegate (int x)
            {
                return x * x;
            };

            Console.WriteLine("Cuadrado de 5 (función anónima): " + cuadrado(5)); // 25

            // ----------------------------------------
            // 2. EXPRESIÓN LAMBDA EQUIVALENTE
            // ----------------------------------------
            Func<int, int> cuadradoLambda = x => x * x;
            Console.WriteLine("Cuadrado de 6 (lambda): " + cuadradoLambda(6)); // 36

            // ----------------------------------------
            // 3. FUNC CON MÚLTIPLES PARÁMETROS
            // ----------------------------------------
            Func<int, int, int> suma = (a, b) => a + b;
            Console.WriteLine("Suma de 4 + 7: " + suma(4, 7)); // 11

            // ----------------------------------------
            // 4. ACTION: función que NO devuelve valor
            // ----------------------------------------
            Action<string> saludar = nombre => Console.WriteLine("Hola, " + nombre);
            saludar("Mundo");

            // ----------------------------------------
            // 5. PREDICATE: función que devuelve bool
            // ----------------------------------------
            Predicate<int> esPar = numero => numero % 2 == 0;
            Console.WriteLine("¿8 es par?: " + esPar(8)); // true

            // ----------------------------------------
            // 6. USO CON LISTAS Y LINQ
            // ----------------------------------------
            List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6 };

            // Filtrar con Where + lambda
            var pares = numeros.Where(n => n % 2 == 0);
            Console.WriteLine("\nNúmeros pares con LINQ:");
            foreach (var n in pares)
                Console.WriteLine(n);

            // Transformar con Select + lambda
            var alCuadrado = numeros.Select(n => n * n);
            Console.WriteLine("\nNúmeros al cuadrado:");
            foreach (var n in alCuadrado)
                Console.WriteLine(n);

            // Buscar con Find y Predicate
            int primerMayorQue3 = numeros.Find(n => n > 3);
            Console.WriteLine($"\nPrimer número mayor que 3: {primerMayorQue3}");

            // Ordenar con lambda
            var descendente = numeros.OrderByDescending(n => n);
            Console.WriteLine("\nOrden descendente:");
            foreach (var n in descendente)
                Console.WriteLine(n);
        }
    }
}

// Func<int, int>: entrada int, salida int
Func<int, int> doble = x => x * 2;

// Func<string, int>: entrada string, salida int
Func<string, int> contarLetras = palabra => palabra.Length;

// Action<string>: entrada string, sin retorno
Action<string> saluda = nombre => Console.WriteLine("Hola " + nombre);

// Predicate<int>: entrada int, salida bool
Predicate<int> esPar = x => x % 2 == 0;


using System;
using System.Collections.Generic;
using System.Linq;

class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    public string Ciudad { get; set; }
}

// PARA QUE SIRVEN
class Program
{
    static void Main()
    {
        List<Persona> personas = new List<Persona>
        {
            new Persona { Nombre = "Ana", Edad = 20, Ciudad = "Bogotá" },
            new Persona { Nombre = "Luis", Edad = 30, Ciudad = "Medellín" },
            new Persona { Nombre = "Carlos", Edad = 17, Ciudad = "Cali" },
            new Persona { Nombre = "Marta", Edad = 25, Ciudad = "Bogotá" },
            new Persona { Nombre = "Pepe", Edad = 15, Ciudad = "Medellín" }
        };

        // Funciones como variables (delegados/lambdas)
        Func<Persona, bool> esMayor = p => p.Edad >= 18;
        Func<Persona, bool> esDeBogota = p => p.Ciudad == "Bogotá";
        Func<Persona, string> formatear = p => $"{p.Nombre} - {p.Edad} años";

        // 🔁 COMBINACIÓN de filtros: personas mayores Y de Bogotá
        var filtradas = personas.Where(p => esMayor(p) && esDeBogota(p));

        // 🔁 Transformación: obtener solo los nombres formateados
        var resultado = filtradas.Select(formatear);

        // 📤 Mostrar resultados
        Console.WriteLine("Mayores de edad de Bogotá:");
        foreach (var item in resultado)
        {
            Console.WriteLine($"- {item}");
        }
    }
}
