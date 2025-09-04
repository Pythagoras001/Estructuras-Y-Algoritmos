using System;

//
// =============================================
// Ejemplo de HERENCIA con CLASES ABSTRACTAS en C#
// =============================================
// En este ejemplo:
// - Clase base ABSTRACTA: Vehiculo (atributos y métodos comunes)
// - Clases hijas: Coche y Moto (implementan lo abstracto y añaden lo propio)
// =============================================

namespace EjemploHerenciaAbstracta
{
    // ================================
    // Clase base abstracta (no se puede instanciar)
    // ================================
    public abstract class Vehiculo
    {
        // ---------------------------
        // ATRIBUTOS (encapsulados)
        // ---------------------------
        // Se usan "protected" para que las clases hijas puedan acceder directamente.
        protected string Marca { get; private set; }
        protected string Modelo { get; private set; }
        protected int Año { get; private set; }

        // ---------------------------
        // CONSTRUCTOR
        // ---------------------------
        protected Vehiculo(string marca, string modelo, int año)
        {
            Marca = marca;
            Modelo = modelo;
            Año = año;
        }

        // ---------------------------
        // MÉTODOS CONCRETOS (ya implementados)
        // ---------------------------
        public void Arrancar()
        {
            Console.WriteLine($"{Marca} {Modelo} está arrancando...");
        }

        // ---------------------------
        // MÉTODO ABSTRACTO
        // ---------------------------
        // Cada clase hija DEBE sobrescribir este método.
        public abstract void MostrarInformacion();
    }

    // ================================
    // Clase hija: Coche
    // ================================
    public class Coche : Vehiculo
    {
        // Atributo específico del coche
        public int NumeroPuertas { get; private set; }

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

        // Implementación obligatoria del método abstracto
        public override void MostrarInformacion()
        {
            Console.WriteLine($"Coche: Marca={Marca}, Modelo={Modelo}, Año={Año}, Puertas={NumeroPuertas}");
        }
    }

    // ================================
    // Clase hija: Moto
    // ================================
    public class Moto : Vehiculo
    {
        // Atributo específico de la moto
        public bool TieneSidecar { get; private set; }

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

        // Implementación obligatoria del método abstracto
        public override void MostrarInformacion()
        {
            string sidecarInfo = TieneSidecar ? "con sidecar" : "sin sidecar";
            Console.WriteLine($"Moto: Marca={Marca}, Modelo={Modelo}, Año={Año}, {sidecarInfo}");
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
            Vehiculo miCoche = new Coche("Toyota", "Corolla", 2020, 4);
            miCoche.Arrancar();         // Método heredado de Vehiculo
            ((Coche)miCoche).TocarBocina(); // Método propio del Coche (requiere casteo si uso variable base)
            miCoche.MostrarInformacion();   // Método implementado en Coche

            Console.WriteLine();

            // Crear una moto
            Vehiculo miMoto = new Moto("Honda", "CBR", 2021, false);
            miMoto.Arrancar();             // Método heredado de Vehiculo
            ((Moto)miMoto).HacerCaballito(); // Método propio de Moto
            miMoto.MostrarInformacion();     // Método implementado en Moto
        }
    }
}
