package EstudioJava.TallerJava4;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {

        try {

            // Creamos las variables //
            Scanner scan = new Scanner(System.in);
            int num = 0;

            // Creamos el code //
            do {
                System.out.print("Ingrese un numero: ");
                num = Integer.parseInt(scan.nextLine());
                if (num > 0) {
                    System.out.println(Math.pow(num, 0.5));
                }else{
                    System.out.println("-Entrada Invalida-");
                }

            } while (num > 0);    

            // Cerramos scanner //
            scan.close();

        } catch (Exception e) {
            System.out.println("Erorr" + e.getMessage());
        }
    }
}
