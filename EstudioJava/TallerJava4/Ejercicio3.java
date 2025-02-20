package EstudioJava.TallerJava4;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        try {
            
            // Creamos las varibales //
            int num = 0;
            Scanner scan = new Scanner(System.in);

            // Creamos el code //
            do {
                System.out.print("Ingrese un numero: ");
                num = Integer.parseInt(scan.nextLine());

                if (num == 0) {
                    System.out.println("-Fin del ciclo-");
                }

            } while (num != 0);

            // Cerramos Scanner //
            scan.close();

        } catch (Exception e) {
            System.out.println("Error" + e.getMessage());
        }
    }
}
