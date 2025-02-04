// package JAVA.TallerJava2;

// import java.util.Scanner;
// import java.lang.Math;

// /*
// Cree un programa que calcule el monto final de una inversión a lo
// largo de un periodo determinado, utilizando interés compuesto.
// Solicite:
// -Monto inicial de la inversión.
// -Tasa de interés anual (en porcentaje: 0.1 , 0.25 , 0.13).
// -Número de años de la inversión.
// Use la fórmula del interés compuesto:
// */

// public class CalculadoraDeInteres {

//     // Agregamos colores //
//     public static final String BLUE = "\u001B[34m";
//     public static final String ROJO = "\033[31m";
//     public static final String GREEN = "\u001B[32m";
//     public static final String RESET = "\u001B[0m";
    
//     public static void main(String[] args) {

//         try {

//             // Creamos las variables y el objeto Scanner //
//             Scanner scan = new Scanner(System.in);
//             float montoInicial = 0f;
//             float montoFinal = 0f;
//             float tasa = 0;
//             int years = 0;
            
//             // Solicitamos la entrada //
//             do {
//                 System.out.println(BLUE + "Ingrese el monto inicial $: " + RESET);
//                 montoInicial = Float.parseFloat(scan.nextLine());

//                 if (montoInicial < 0){
//                     System.out.println(ROJO + "Entrada Invalida Ingrese de nuevo");
//                 }

//             } while (montoInicial < 0);

//             do {
//                 System.out.println(BLUE + "Ingrese La Tasa De Interes %: " + RESET);
//                 tasa = Float.parseFloat(scan.nextLine())/100;

//                 if (tasa < 0){
//                     System.out.println(ROJO + "Entrada Invalida Ingrese de nuevo");
//                 }

//             } while (tasa < 0);

//             do {
//                 System.out.println(BLUE + "Ingrese el timpo en años: " + RESET);
//                 years = Integer.parseInt(scan.nextLine());

//                 if (years < 0){
//                     System.out.println(ROJO + "Entrada Invalida Ingrese de nuevo");
//                 }

//             } while (years < 0);

//             // Procesamos la salida //
//             montoFinal = montoInicial * (float)Math.pow(1 + tasa, years);
            
//             // Imprimimos la salida //
//             System.out.println(GREEN + "El Rendimiento Final Es: " + String.format("%.1f", montoFinal) +'$'+ RESET);

//             // Cerramos Scaner //
//             scan.close();

//         } catch (Exception error) {
//             System.out.println("Error de entrada: " + error.getMessage());
//         }
//     }
// }

package JAVA.TallerJava2;

import java.util.Scanner;
import java.lang.Math;

public class CalculadoraDeInteres {

    // Agregamos colores //
    public static final String BLUE = "\u001B[34m";
    public static final String ROJO = "\033[31m";
    public static final String GREEN = "\u001B[32m";
    public static final String RESET = "\u001B[0m";
    
    // Función para pedir un valor positivo
    private static float valorPositivo(String mensaje, Scanner scan) {
        float numero;
        do {
            System.out.println(BLUE + mensaje + RESET);
            numero = Float.parseFloat(scan.nextLine());
            if (numero < 0) {
                System.out.println(ROJO + "Entrada inválida. Ingrese de nuevo.");
            }
        } while (numero < 0);
        return numero;
    }

    public static void main(String[] args) {

        try {

            // Creamos las variables y el objeto Scanner //
            Scanner scan = new Scanner(System.in);
            float montoInicial = 0f;
            float montoFinal = 0f;
            float tasa = 0;
            int years = 0;

            // Usamos la función para obtener entradas válidas //
            montoInicial = valorPositivo("Ingrese el monto inicial $: ", scan);
            tasa = valorPositivo("Ingrese la tasa de interés %: ", scan) / 100;
            years = (int) valorPositivo("Ingrese el tiempo en años: ", scan);

            // Procesamos la salida //
            montoFinal = montoInicial * (float)Math.pow(1 + tasa, years);
            
            // Imprimimos la salida //
            System.out.println(GREEN + "El Rendimiento Final Es: " + String.format("%.1f", montoFinal) + "$" + RESET);

            // Cerramos el Scanner //
            scan.close();

        } catch (Exception error) {
            System.out.println("Error de entrada: " + error.getMessage());
        }
    }
}
