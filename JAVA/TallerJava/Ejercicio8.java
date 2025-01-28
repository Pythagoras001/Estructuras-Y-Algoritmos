package JAVA.TallerJava;

import java.util.Locale;
import java.util.Scanner;

public class Ejercicio8 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        scan.useLocale(Locale.US);

        try {
            System.out.println("Ingrese el valor de la comida: ");
            float comida = scan.nextFloat();

            System.out.println("Debe pagar: "+ comida*1.18);
            
        } catch (Exception error) {
            System.out.println(error);
        }

        scan.close();

    }   
}