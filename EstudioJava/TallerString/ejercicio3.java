// public class ejercicio3 {
//     public static void main(String[] args) {
//         for (int i = 1; i <= 10; i++) {
//             System.out.printf("%2d x %2d = %3d%n", i, i, i * i);
//         }
//     }
// }


public class ejercicio3 {
    public static void main(String[] args) {
        int max = 10; // Número máximo para la tabla

        // Calcula el ancho necesario para los números
        int anchoNumero = String.valueOf(max).length();
        int anchoResultado = String.valueOf(max * max).length();

        // Construye el formato dinámico
        String formato = "%" + anchoNumero + "d x %" + anchoNumero + "d = %-"+ anchoResultado +"d%n";

        // Imprime la tabla
        for (int i = 1; i <= max; i++) {
            System.out.printf(formato, i, i, i * i);
        }
    }
}

// public class EjemplosPrintf {
//     public static void main(String[] args) {
//         int numero = 42;
        
//         // Alineación a la derecha (por defecto)
//         System.out.printf("'%5d'%n", numero);  // Resultado: '   42'

//         // Alineación a la izquierda
//         System.out.printf("'%-5d'%n", numero); // Resultado: '42   '

//         // Ancho dinámico
//         int max = 100;
//         String formato = "%" + String.valueOf(max).length() + "d";
//         System.out.printf(formato + "%n", numero); // Resultado: ' 42'

//         // Texto alineado a la derecha con ancho 10
//         System.out.printf("'%10s'%n", "Hola");  // Resultado: '      Hola'

//         // Texto alineado a la izquierda con ancho 10
//         System.out.printf("'%-10s'%n", "Hola"); // Resultado: 'Hola      '
//     }
// }

