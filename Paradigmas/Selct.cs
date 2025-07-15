using System;
using System.Collections.Generic;
using System.Linq;

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
        };

        // Usamos Select para obtener solo los nombres
        var nombres = personas.Select(p => p.Nombre);

        Console.WriteLine("Nombres:");
        foreach (var nombre in nombres)
        {
            Console.WriteLine("- " + nombre);
        }

        // También puedes proyectar a un tipo nuevo o anónimo
        var resumen = personas.Select(p => new { p.Nombre, MayorEdad = p.Edad >= 18 });

        Console.WriteLine("\nResumen:");
        foreach (var item in resumen)
        {
            Console.WriteLine($"{item.Nombre} - {(item.MayorEdad ? "Adulto" : "Menor")}");
        }
    }
}
