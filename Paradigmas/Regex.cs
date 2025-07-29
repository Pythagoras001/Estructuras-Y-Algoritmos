using System;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        Console.WriteLine("✅ Validaciones usando Regex en C#");
        Console.WriteLine("----------------------------------");

        // ============================
        // 1. Validar un número del 0 al 4
        // ============================
        Validar("Número (0-4)", "3", @"^[0-4]$");

        // ============================
        // 2. Validar un número entero (positivo o negativo)
        // ============================
        Validar("Número entero", "-123", @"^-?\d+$");

        // ============================
        // 3. Validar número decimal
        // ============================
        Validar("Número decimal", "45.67", @"^-?\d+(\.\d+)?$");

        // ============================
        // 4. Validar solo letras (mayúsculas o minúsculas)
        // ============================
        Validar("Solo letras", "HolaMundo", @"^[A-Za-z]+$");

        // ============================
        // 5. Validar solo letras y espacios
        // ============================
        Validar("Letras y espacios", "Hola Mundo", @"^[A-Za-z ]+$");

        // ============================
        // 6. Validar nombre propio (inicial mayúscula)
        // ============================
        Validar("Nombre propio", "Carlos", @"^[A-Z][a-z]+$");

        // ============================
        // 7. Validar correo electrónico
        // ============================
        Validar("Email", "ejemplo@correo.com", @"^[\w\.-]+@[\w\.-]+\.\w{2,}$");

        // ============================
        // 8. Validar fecha dd/mm/yyyy
        // ============================
        Validar("Fecha", "29/07/2025", @"^\d{2}/\d{2}/\d{4}$");

        // ============================
        // 9. Validar cadena booleana (true/false)
        // ============================
        Validar("Booleano", "true", @"^(true|false)$");

        // ============================
        // 10. Validar cadena con caracteres especiales
        // ============================
        Validar("Contraseña con símbolos", "M1_contra#2025!", @"^[\w@#\$%\^&\*\-!\.]+$");

        Console.WriteLine("\n✔️ Validaciones completadas.");
    }

    /// <summary>
    /// Función auxiliar para validar entradas con un patrón Regex
    /// </summary>
    static void Validar(string tipo, string entrada, string patron)
    {
        bool esValido = Regex.IsMatch(entrada, patron);
        Console.WriteLine($"{tipo}: '{entrada}' => {(esValido ? "✅ Válido" : "❌ Inválido")}");
    }
}
