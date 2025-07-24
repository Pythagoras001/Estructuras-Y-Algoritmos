using System;
using System.Collections.Generic;
using System.Linq;

namespace ApunteSelectLINQ
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
            // Lista base de objetos Persona
            List<Persona> personas = new List<Persona>
            {
                new Persona { Nombre = "Ana", Edad = 20 },
                new Persona { Nombre = "Luis", Edad = 30 },
                new Persona { Nombre = "Carlos", Edad = 17 },
                new Persona { Nombre = "Marta", Edad = 25 }
            };

            // ----------------------------
            // SELECT en LINQ
            // ----------------------------
            // Select permite proyectar o transformar los elementos de una lista

            // 1. Seleccionar solo los nombres (IEnumerable<string>)
            var nombres = personas.Select(p => p.Nombre);
            Console.WriteLine("Nombres:");
            foreach (var nombre in nombres)
                Console.WriteLine(nombre);

            // 2. Seleccionar nombres en mayúsculas
            var nombresMayus = personas.Select(p => p.Nombre.ToUpper());
            Console.WriteLine("\nNombres en mayúsculas:");
            foreach (var nombre in nombresMayus)
                Console.WriteLine(nombre);

            // 3. Crear objetos anónimos con nombre y edad al cuadrado
            var datosAnonimos = personas.Select(p => new { p.Nombre, EdadAlCuadrado = p.Edad * p.Edad });
            Console.WriteLine("\nNombre y Edad^2:");
            foreach (var d in datosAnonimos)
                Console.WriteLine($"{d.Nombre}: {d.EdadAlCuadrado}");

            // 4. Transformar en cadenas personalizadas
            var descripciones = personas.Select(p => $"{p.Nombre} tiene {p.Edad} años");
            Console.WriteLine("\nDescripciones:");
            foreach (var desc in descripciones)
                Console.WriteLine(desc);

            // 5. Obtener la inicial del nombre
            var iniciales = personas.Select(p => p.Nombre[0]);
            Console.WriteLine("\nIniciales:");
            foreach (var letra in iniciales)
                Console.WriteLine(letra);

            // 6. Proyección booleana: ¿es mayor de edad?
            var mayoresEdad = personas.Select(p => p.Edad >= 18);
            Console.WriteLine("\n¿Es mayor de edad?");
            foreach (var b in mayoresEdad)
                Console.WriteLine(b);

            // 7. Usar el índice del elemento con overload de Select
            var conIndice = personas.Select((p, i) => new { Indice = i, Nombre = p.Nombre });
            Console.WriteLine("\nPersonas con índice:");
            foreach (var item in conIndice)
                Console.WriteLine($"{item.Indice}: {item.Nombre}");

            // 8. Convertir a lista con ToList()
            var listaNombres = personas.Select(p => p.Nombre).ToList();
            Console.WriteLine("\nLista de nombres (como List<string>):");
            Console.WriteLine($"Tipo: {listaNombres.GetType()}");
        }
    }
}
