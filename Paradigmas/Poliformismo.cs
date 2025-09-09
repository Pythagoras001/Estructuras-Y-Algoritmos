using System;

namespace ApuntePolimorfismo
{
    // Clase abstracta: no se puede instanciar
    abstract class Animal
    {
        public string Nombre { get; set; }

        // Método abstracto: obliga a las clases hijas a implementarlo
        public abstract void HacerSonido();

        // Método virtual: las hijas pueden sobrescribirlo con override (opcional)
        public virtual void Describir()
        {
            Console.WriteLine($"Soy un animal llamado {Nombre}.");
        }

        // Método normal (no virtual): no puede sobrescribirse
        public void Comer()
        {
            Console.WriteLine($"{Nombre} está comiendo.");
        }
    }

    class Perro : Animal
    {
        // Obligatorio implementar el abstract
        public override void HacerSonido()
        {
            Console.WriteLine($"{Nombre}: ¡Guau guau!");
        }

        // Sobrescribir el método virtual
        public override void Describir()
        {
            Console.WriteLine($"Soy un perro llamado {Nombre}, fiel amigo del hombre.");
        }
    }

    class Gato : Animal
    {
        public override void HacerSonido()
        {
            Console.WriteLine($"{Nombre}: ¡Miau!");
        }

        // Usar new para ocultar el método del padre (NO es polimorfismo real)
        public new void Comer()
        {
            Console.WriteLine($"{Nombre} está comiendo pescado.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Polimorfismo con referencia de tipo base
            Animal a1 = new Perro { Nombre = "Firulais" };
            Animal a2 = new Gato { Nombre = "Michi" };

            // Cada uno ejecuta su versión de HacerSonido()
            a1.HacerSonido();  // Firulais: ¡Guau guau!
            a2.HacerSonido();  // Michi: ¡Miau!

            // Describir() es virtual -> se respeta el override
            a1.Describir();    // versión de Perro
            a2.Describir();    // versión de Animal (porque Gato no sobrescribió)

            // Comer() no es virtual -> siempre llama al de Animal
            a1.Comer();        // Firulais está comiendo.
            a2.Comer();        // Michi está comiendo.

            // Pero si casteamos al tipo real (Gato), se ejecuta el ocultado con "new"
            Gato g = new Gato { Nombre = "Misu" };
            g.Comer();         // Misu está comiendo pescado.
        }
    }
}

///////////////////////////

class Padre
{
    public void Saludar()
    {
        Console.WriteLine("Hola, soy el padre.");
    }
}

class Hijo : Padre
{
    // Oculta el método del padre
    public new void Saludar()
    {
        Console.WriteLine("Hola, soy el hijo.");
    }
}

class Program
{
    static void Main()
    {
        Padre p = new Padre();
        p.Saludar();   // Hola, soy el padre.

        Hijo h = new Hijo();
        h.Saludar();   // Hola, soy el hijo.

        Padre refPadre = new Hijo();
        refPadre.Saludar(); // Hola, soy el padre. (NO usa el de Hijo)
    }
}
