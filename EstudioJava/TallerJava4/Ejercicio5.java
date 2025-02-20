package EstudioJava.TallerJava4;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        try {
            
            // Creamos las variables //
            Scanner scan = new Scanner(System.in);
            int num = 0;
            int suma = 0;

            // Proceso //
            do {
                System.out.println("Ingrese un numero: ");
                num = Integer.parseInt(scan.nextLine());
                suma += num;
                
            } while (num != 0);

            // Damos la salida //
            System.out.println(suma);

            // Cerramos Scaner //
            scan.close();

        } catch (Exception e) {
            System.out.println("Error" + e.getMessage());
        }
    }
}
