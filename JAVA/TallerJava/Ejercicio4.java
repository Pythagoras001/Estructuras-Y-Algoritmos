package JAVA.TallerJava;
import java.util.Locale;
import java.util.Scanner;

/*
Solicitar al usuario ingresar la temperatura en grados centígrados
y convertirla en grados Fahrenheit
 */

public class Ejercicio4 {

    // Ingresamos una gama de colores para la terminal 
    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {

        // Creamos el objeto scaner y configuramos en la region US
        Scanner scan = new Scanner(System.in);
        scan.useLocale(Locale.US);

        try {
            // Solicitamos el ingreso de la informacion y recibimos la entrada
            System.out.println(BLUE + "Ingrese la temperatura en C°: ");
            float temp = scan.nextFloat();

            // Convertimos la temperatura a Fahrenheit con (0 °C × 9/5) + 32 = 32 °F e imprimimos 
            float tempFahreng = temp*(9/5) + 32;
            System.out.println(YELLOW + "La temperatura en Fahrenheit es: \n" + tempFahreng + " F°" + RESET);

        } catch (Exception error) {
            System.out.println(error);

        }

        scan.close();
    }
    
}
