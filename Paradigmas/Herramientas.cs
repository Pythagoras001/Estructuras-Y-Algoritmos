using System;
using System.Collections.Generic;
using System.Linq;

namespace ApunteLINQ
{
    class Persona
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }
    }

    class Program
    {
        static void Main()
        {
            List<Persona> personas = new List<Persona>
            {
                new Persona { Nombre = "Ana", Edad = 20 },
                new Persona { Nombre = "Luis", Edad = 30 },
                new Persona { Nombre = "Carlos", Edad = 17 },
                new Persona { Nombre = "Marta", Edad = 25 }
            };

            // -------------------------
            // LINQ con expresiones lambda
            // -------------------------

            // WHERE: filtra los elementos que cumplen la condición
            var mayores = personas.Where(p => p.Edad >= 18);

            // SELECT: proyecta o transforma cada elemento
            var nombres = personas.Select(p => p.Nombre);

            // ORDERBY: ordena ascendentemente por una propiedad
            var ordenadosAsc = personas.OrderBy(p => p.Edad);

            // ORDERBYDESCENDING: ordena descendentemente por una propiedad
            var ordenadosDesc = personas.OrderByDescending(p => p.Edad);

            // FIRSTORDEFAULT: devuelve el primer elemento que cumple la condición (o null si no existe)
            var primerMayor = personas.FirstOrDefault(p => p.Edad >= 18);

            // ANY: devuelve true si al menos uno cumple la condición
            bool hayMenores = personas.Any(p => p.Edad < 18);

            // ALL: devuelve true si todos cumplen la condición
            bool todosMayores = personas.All(p => p.Edad >= 18);

            // COUNT: cuenta cuántos cumplen la condición
            int cantidadMayores = personas.Count(p => p.Edad >= 18);

            // MAX: devuelve el valor máximo de una propiedad
            int maxEdad = personas.Max(p => p.Edad);

            // MIN: devuelve el valor mínimo de una propiedad
            int minEdad = personas.Min(p => p.Edad);

            // AVERAGE: calcula el promedio de una propiedad numérica
            double promedioEdad = personas.Average(p => p.Edad);

            // SUM: suma los valores de una propiedad numérica
            int sumaEdades = personas.Sum(p => p.Edad);

            // TOLIST: convierte el resultado a una lista
            var listaDeNombres = personas.Select(p => p.Nombre).ToList();

            // Imprimir ejemplos
            Console.WriteLine("Personas mayores de edad:");
            foreach (var p in mayores)
            {
                Console.WriteLine($"- {p.Nombre} ({p.Edad} años)");
            }

            Console.WriteLine($"\n¿Hay menores?: {hayMenores}");
            Console.WriteLine($"¿Todos son mayores?: {todosMayores}");
            Console.WriteLine($"Mayor edad: {maxEdad}");
            Console.WriteLine($"Edad promedio: {promedioEdad}");

            // S E L E C T //
            // Seleccionar solo los nombres en mayúsculas
            var nombresMayuscula = personas.Select(p => p.Nombre.ToUpper());

            // Seleccionar objetos anónimos con solo Nombre y Edad al cuadrado
            var datosAnonimos = personas.Select(p => new { p.Nombre, EdadAlCuadrado = p.Edad * p.Edad });

            // Seleccionar una cadena personalizada por persona
            var descripciones = personas.Select(p => $"{p.Nombre} tiene {p.Edad} años");

            // Seleccionar la primera letra del nombre
            var iniciales = personas.Select(p => p.Nombre[0]);

            // Transformar la lista de personas en una lista de booleans (¿mayor de edad?)
            var esMayorDeEdad = personas.Select(p => p.Edad >= 18);

            // Seleccionar un índice junto con el elemento (usando overload con índice)
            var conIndice = personas.Select((p, i) => new { Indice = i, Nombre = p.Nombre });

        }
    }
}


