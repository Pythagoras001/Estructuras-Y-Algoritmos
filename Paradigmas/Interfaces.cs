using System;

namespace ApunteInterfaces
{
    // 🔹 Una interfaz solo define contratos (qué debe hacerse, no cómo)
    interface IAnimal
    {
        string Nombre { get; set; }

        void HacerSonido(); // Método sin implementación
    }

    // 🔹 Herencia entre interfaces (IAnimal -> IMascota)
    interface IMascota : IAnimal
    {
        void Jugar();
    }

    // 🔹 Otra interfaz independiente
    interface ICuidador
    {
        void Alimentar();
    }

    // 🔹 Clase Perro implementa IMascota (y por herencia también IAnimal)
    class Perro : IMascota
    {
        public string Nombre { get; set; }

        public void HacerSonido()
        {
            Console.WriteLine($"{Nombre}: ¡Guau guau!");
        }

        public void Jugar()
        {
            Console.WriteLine($"{Nombre} está jugando a traer la pelota.");
        }
    }

    // 🔹 Clase Gato implementa IMascota y además ICuidador
    class Gato : IMascota, ICuidador
    {
        public string Nombre { get; set; }

        public void HacerSonido()
        {
            Console.WriteLine($"{Nombre}: ¡Miau!");
        }

        public void Jugar()
        {
            Console.WriteLine($"{Nombre} juega con una caja.");
        }

        // Implementación de la otra interfaz
        public void Alimentar()
        {
            Console.WriteLine($"{Nombre} está alimentando a sus gatitos.");
        }
    }

    // 🔹 Ejemplo de clase que solo implementa ICuidador
    class Humano : ICuidador
    {
        public void Alimentar()
        {
            Console.WriteLine("El humano alimenta a sus mascotas.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // IMascota puede apuntar a Perro o Gato
            IMascota m1 = new Perro { Nombre = "Firulais" };
            IMascota m2 = new Gato { Nombre = "Michi" };

            m1.HacerSonido(); // Guau
            m1.Jugar();

            m2.HacerSonido(); // Miau
            m2.Jugar();

            // Uso de ICuidador
            ICuidador cuidador = new Gato { Nombre = "Luna" };
            cuidador.Alimentar(); // Luna está alimentando a sus gatitos.

            cuidador = new Humano();
            cuidador.Alimentar(); // El humano alimenta a sus mascotas.
        }
    }
}
