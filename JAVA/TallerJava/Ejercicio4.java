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

        try {
            Scanner scan = new Scanner(System.in);
            scan.useLocale(Locale.US);

            float temp = 0f;
            float tempFahreng = 0f;

            System.out.println(BLUE + "Ingrese la temperatura en C°: ");
            temp = scan.nextFloat();

            tempFahreng = temp*(9/5) + 32;
            System.out.println(YELLOW + "La temperatura en Fahrenheit es: \n" + tempFahreng + " F°" + RESET);

            scan.close();

        } catch (Exception error) {
            System.out.println(error);

        }
    }
}
