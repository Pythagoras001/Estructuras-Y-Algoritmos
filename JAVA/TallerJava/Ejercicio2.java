package JAVA.TallerJava;
import java.util.Locale;
import java.util.Scanner;

/*
 * Solicitar al usuario ingresar una cantidad expresada
 * en centímetros cúbicos y devolver su cantidad en litros
*/

public class Ejercicio2 {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        scan.useLocale(Locale.US);

        try {
            System.out.println("Ingrese una cantidad en Cm3: ");
            double volumenCm = scan.nextDouble();
            double volumenLit = volumenCm / 1000;

            System.out.println("Su cantida en litros es: " + String.format("%.3f", volumenLit) + " L");

        } catch (Exception error) {
            System.out.println(error);
        }
        
        scan.close();
    }
}