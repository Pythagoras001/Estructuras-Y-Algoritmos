using System;
using System.IO;

namespace LecturaPorCaracteres
{
    class Program
    {
        static void Main()
        {
            // Ruta del archivo de texto a leer (puede ser relativo o absoluto)
            string rutaArchivo = "archivo.txt";

            // Tamaño del búfer (cantidad de caracteres que se leerán por bloque)
            char[] buffer = new char[1024]; // 1KB (1024 caracteres)
            int caracteresLeídos;

            try
            {
                // Abrimos el archivo para lectura de texto crudo
                using (StreamReader lector = new StreamReader(rutaArchivo))
                {
                    Console.WriteLine("=== Lectura por bloques de caracteres ===\n");
                    int bloque = 1;

                    // Leemos mientras haya caracteres disponibles
                    while ((caracteresLeídos = lector.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        Console.WriteLine($"--- Bloque #{bloque} ---");
                        // Creamos un string con solo los caracteres leídos
                        string texto = new string(buffer, 0, caracteresLeídos);
                        Console.WriteLine(texto);  // Puedes procesar texto aquí
                        Console.WriteLine($"(Caracteres en bloque: {caracteresLeídos})\n");
                        bloque++;
                    }
                }
            }
            catch (FileNotFoundException)
            {
                Console.WriteLine("⚠️ El archivo no fue encontrado.");
            }
            catch (IOException ex)
            {
                Console.WriteLine($"⚠️ Error de lectura: {ex.Message}");
            }
        }
    }
}
