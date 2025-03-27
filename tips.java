// if (cadena.matches("\\d+")) {
//     System.out.println("La cadena contiene solo números.");
// }

// if (cadena.matches("[a-zA-Z]+")) {
//     System.out.println("La cadena contiene solo letras.");
// }

// import java.util.regex.*;

// public class RegexExample {
//     public static void main(String[] args) {
//         // 1. Compilar una expresión regular
//         Pattern pattern = Pattern.compile("\\d+"); // Expresión regular para encontrar números
//         Matcher matcher = pattern.matcher("123 hola 456");

//         // 2. Verificar si una cadena coincide completamente
//         boolean resultado = Pattern.matches("\\d+", "12345"); // true
//         System.out.println("Coincidencia exacta: " + resultado);

//         // 3. Buscar coincidencias en una cadena
//         matcher = pattern.matcher("abc 123 def 456");
//         while (matcher.find()) {
//             System.out.println("Encontrado: " + matcher.group());
//         }

//         // 4. Obtener la posición de las coincidencias
//         matcher = pattern.matcher("abc 123 def 456");
//         while (matcher.find()) {
//             System.out.println("Encontrado: " + matcher.group() + " en posición " + matcher.start() + "-" + matcher.end());
//         }

//         // 5. Reemplazar texto con expresiones regulares
//         String texto = "Hola 123, adiós 456";
//         String resultadoReemplazo = texto.replaceAll("\\d+", "XXX");
//         System.out.println("Texto reemplazado: " + resultadoReemplazo);

//         // 6. Dividir una cadena usando una expresión regular
//         String[] partes = "uno, dos, tres".split(", ");
//         for (String parte : partes) {
//             System.out.println("Parte: " + parte);
//         }

//         // 7. Uso de grupos de captura
//         matcher = Pattern.compile("(\\d{3})-(\\d{2})-(\\d{4})").matcher("123-45-6789");
//         if (matcher.matches()) {
//             System.out.println("Grupo 1: " + matcher.group(1)); // 123
//             System.out.println("Grupo 2: " + matcher.group(2)); // 45
//             System.out.println("Grupo 3: " + matcher.group(3)); // 6789
//         }

//         // 8. Verificar si una cadena empieza o termina con un patrón
//         boolean empieza = "hola123".matches("^hola.*"); // true
//         boolean termina = "123hola".matches(".*hola$"); // true
//         System.out.println("Empieza con 'hola': " + empieza);
//         System.out.println("Termina con 'hola': " + termina);

//         // 9. Expresiones regulares útiles
//         System.out.println("Expresiones regulares útiles:");
//         System.out.println("\\d+ → Números");
//         System.out.println("\\w+ → Palabras");
//         System.out.println("\\s+ → Espacios en blanco");
//         System.out.println("[a-z]+ → Letras minúsculas");
//         System.out.println("[A-Z]+ → Letras mayúsculas");
//         System.out.println("[^a-zA-Z0-9] → Caracteres no alfanuméricos");
//     }
// }