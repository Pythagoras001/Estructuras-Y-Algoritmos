using System;

//
// =============================================
// Ejemplo de Constructores Sobrecargados con "this" en C#
// =============================================
// "this" en un constructor sirve para llamar a otro constructor
// de la misma clase, evitando duplicar código.
// =============================================

namespace EjemploConstructoresConThis
{
    public class Persona
    {
        // ======= Atributos =======
        public string Nombre { get; set; }
        public int Edad { get; set; }
        public string Ciudad { get; set; }

        // ======= Constructor 1 (por defecto) =======
        // Llama al constructor 4 enviando valores por defecto
        public Persona() : this("Desconocido", 0, "Sin ciudad")
        {
            Console.WriteLine("Constructor por defecto ejecutado.");
        }

        // ======= Constructor 2 =======
        // Recibe solo el nombre y envía los demás valores por defecto
        public Persona(string nombre) : this(nombre, 0, "Sin ciudad")
        {
            Console.WriteLine("Constructor con NOMBRE ejecutado.");
        }

        // ======= Constructor 3 =======
        // Recibe nombre y edad, ciudad por defecto
        public Persona(string nombre, int edad) : this(nombre, edad, "Sin ciudad")
        {
            Console.WriteLine("Constructor con NOMBRE y EDAD ejecutado.");
        }

        // ======= Constructor 4 (principal) =======
        // Este es el constructor "central" que inicializa todo
        public Persona(string nombre, int edad, string ciudad)
        {
            Nombre = nombre;
            Edad = edad;
            Ciudad = ciudad;
            Console.WriteLine("Constructor con NOMBRE, EDAD y CIUDAD ejecutado.");
        }

        // Método para mostrar información
        public void MostrarInfo()
        {
            Console.WriteLine($"Nombre: {Nombre}, Edad: {Edad}, Ciudad: {Ciudad}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Constructor por defecto
            Persona p1 = new Persona();
            p1.MostrarInfo();

            Console.WriteLine();

            // Constructor con solo nombre
            Persona p2 = new Persona("Carlos");
            p2.MostrarInfo();

            Console.WriteLine();

            // Constructor con nombre y edad
            Persona p3 = new Persona("Ana", 25);
            p3.MostrarInfo();

            Console.WriteLine();

            // Constructor con nombre, edad y ciudad
            Persona p4 = new Persona("Luis", 30, "Bogotá");
            p4.MostrarInfo();
        }
    }
}
