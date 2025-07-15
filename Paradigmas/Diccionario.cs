using System;
using System.Collections.Generic;

namespace ApunteDiccionario
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear un diccionario con clave tipo string y valor tipo int
            Dictionary<string, int> edades = new Dictionary<string, int>();

            // ----------------------------
            // AGREGAR ELEMENTOS
            // ----------------------------

            edades.Add("Ana", 25);
            edades.Add("Luis", 30);
            edades.Add("Carlos", 20);

            // También se puede usar la sintaxis con corchetes
            edades["Marta"] = 22; // Si no existe, la agrega; si existe, la reemplaza

            // ----------------------------
            // ACCEDER A VALORES
            // ----------------------------

            Console.WriteLine($"Edad de Ana: {edades["Ana"]}");

            // ----------------------------
            // VERIFICAR EXISTENCIA
            // ----------------------------

            if (edades.ContainsKey("Luis"))
            {
                Console.WriteLine("Luis está en el diccionario.");
            }

            if (edades.ContainsValue(22))
            {
                Console.WriteLine("Alguien tiene 22 años.");
            }

            // ----------------------------
            // OBTENER VALOR SEGURO
            // ----------------------------

            if (edades.TryGetValue("Carlos", out int edadCarlos))
            {
                Console.WriteLine($"Edad de Carlos: {edadCarlos}");
            }

            // ----------------------------
            // MODIFICAR VALORES
            // ----------------------------

            edades["Luis"] = 31; // Reemplazar valor

            // ----------------------------
            // ELIMINAR ELEMENTOS
            // ----------------------------

            edades.Remove("Ana");

            // ----------------------------
            // RECORRER EL DICCIONARIO
            // ----------------------------

            Console.WriteLine("\nListado completo:");
            foreach (KeyValuePair<string, int> par in edades)
            {
                Console.WriteLine($"Nombre: {par.Key}, Edad: {par.Value}");
            }

            // ----------------------------
            // OBTENER SOLO CLAVES O VALORES
            // ----------------------------

            Console.WriteLine("\nSolo nombres:");
            foreach (string clave in edades.Keys)
            {
                Console.WriteLine("- " + clave);
            }

            Console.WriteLine("\nSolo edades:");
            foreach (int valor in edades.Values)
            {
                Console.WriteLine("- " + valor);
            }

            // ----------------------------
            // LIMPIAR TODO EL DICCIONARIO
            // ----------------------------

            edades.Clear();
            Console.WriteLine($"\n¿Diccionario vacío?: {edades.Count == 0}");
        }
    }
}
