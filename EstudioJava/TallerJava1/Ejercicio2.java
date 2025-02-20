package EstudioJava.TallerJava1;
import java.util.Locale;
import java.util.Scanner;

/*
 * Solicitar al usuario ingresar una cantidad expresada
 * en centímetros cúbicos y devolver su cantidad en litros
*/

public class Ejercicio2 {
    
    public static void main(String[] args) {
    
        try {
            Scanner scan = new Scanner(System.in);
            scan.useLocale(Locale.US);

            double volumenCm = 0;
            double volumenLit = 0;

            System.out.println("Ingrese una cantidad en Cm3: ");
            volumenCm = scan.nextDouble();
            volumenLit = volumenCm / 1000;

            System.out.println("Su cantida en litros es: " + String.format("%.3f", volumenLit) + " L");

            scan.close();
            
        } catch (Exception error) {
            System.out.println(error);
        }
        
    }
}