package EstudioJava.TallerJava4;

import java.util.Random;
import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {
        
        try {

            // Creamos las variantes //
            Scanner scan = new Scanner(System.in);
            Random rand = new Random();

            int selec = rand.nextInt(30);
            int num = 0;

            // Calculamos //
            do {
                System.out.println("Ingrese el un numero: ");
                num = Integer.parseInt(scan.nextLine());

                if (num < selec) {
                    System.out.println("-El numero es mayor-");
                }else if(num != selec){
                    System.out.println("-El numero es menor-");
                }

            } while (num != selec);

            // Cerramos Scaneer //
            scan.close();
            
        } catch (Exception e) {
            System.out.println("Error" + e.getMessage());
        }
    }
}