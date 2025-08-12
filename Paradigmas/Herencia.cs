using System;

//
// =============================================
// Ejemplo de HERENCIA en C#
// =============================================
// En este ejemplo:
// - Clase base: Vehiculo (atributos y métodos comunes)
// - Clases hijas: Coche y Moto (heredan y extienden la base)
// =============================================

namespace EjemploHerencia
{
    // ================================
    // Clase base (Padre o Superclase)
    // ================================
    public class Vehiculo
    {
        // Atributos comunes a todos los vehículos
        public string Marca { get; set; }
        public string Modelo { get; set; }
        public int Año { get; set; }

        // Constructor de la clase base
        public Vehiculo(string marca, string modelo, int año)
        {
            Marca = marca;
            Modelo = modelo;
            Año = año;
        }

        // Método común que todos los vehículos pueden usar
        public void Arrancar()
        {
            Console.WriteLine($"{Marca} {Modelo} está arrancando...");
        }

        // Método que puede ser sobrescrito por las clases hijas (polimorfismo)
        public virtual void MostrarInformacion()
        {
            Console.WriteLine($"Vehículo: {Marca} {Modelo}, Año: {Año}");
        }
    }

    // ================================
    // Clase hija: Coche
    // ================================
    public class Coche : Vehiculo
    {
        // Atributo específico del coche
        public int NumeroPuertas { get; set; }

        // Constructor de la clase hija que usa el constructor del padre
        public Coche(string marca, string modelo, int año, int numeroPuertas)
            : base(marca, modelo, año) // Llama al constructor de Vehiculo
        {
            NumeroPuertas = numeroPuertas;
        }

        // Método propio del coche
        public void TocarBocina()
        {
            Console.WriteLine("¡Beep beep!");
        }

        // Sobrescribimos el método del padre para agregar más información
        public override void MostrarInformacion()
        {
            Console.WriteLine($"Coche: {Marca} {Modelo}, Año: {Año}, Puertas: {NumeroPuertas}");
        }
    }

    // ================================
    // Clase hija: Moto
    // ================================
    public class Moto : Vehiculo
    {
        // Atributo específico de la moto
        public bool TieneSidecar { get; set; }

        // Constructor de la clase hija
        public Moto(string marca, string modelo, int año, bool tieneSidecar)
            : base(marca, modelo, año) // Llama al constructor de Vehiculo
        {
            TieneSidecar = tieneSidecar;
        }

        // Método propio de la moto
        public void HacerCaballito()
        {
            Console.WriteLine("¡La moto está haciendo un caballito!");
        }

        // Sobrescribimos el método del padre
        public override void MostrarInformacion()
        {
            string sidecarInfo = TieneSidecar ? "con sidecar" : "sin sidecar";
            Console.WriteLine($"Moto: {Marca} {Modelo}, Año: {Año}, {sidecarInfo}");
        }
    }

    // ================================
    // Programa principal
    // ================================
    class Program
    {
        static void Main(string[] args)
        {
            // Crear un coche
            Coche miCoche = new Coche("Toyota", "Corolla", 2020, 4);
            miCoche.Arrancar(); // Método heredado de Vehiculo
            miCoche.TocarBocina(); // Método propio de Coche
            miCoche.MostrarInformacion(); // Método sobrescrito

            Console.WriteLine();

            // Crear una moto
            Moto miMoto = new Moto("Honda", "CBR", 2021, false);
            miMoto.Arrancar(); // Método heredado de Vehiculo
            miMoto.HacerCaballito(); // Método propio de Moto
            miMoto.MostrarInformacion(); // Método sobrescrito
        }
    }
}
