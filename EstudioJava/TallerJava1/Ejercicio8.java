package EstudioJava.TallerJava1;

import java.util.Locale;
import java.util.Scanner;

public class Ejercicio8 {

    public static void main(String[] args) {
        
        try {

            Scanner scan = new Scanner(System.in);
            scan.useLocale(Locale.US);

            float comida = 0f;

            System.out.println("Ingrese el valor de la comida: ");
            comida = scan.nextFloat();

            System.out.println("Debe pagar: "+ comida*1.18);

            scan.close();
            
        } catch (Exception error) {
            System.out.println(error);
        }

    }   
}