package EstudioJava.TallerJava5;

import java.util.Random;
import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        // Creamos las variables //

        Scanner scan = new Scanner(System.in);
        int repeticiones = 0;

        // Solicitamos la entrada //

        System.out.println("Cuantas veces desea ejecutar la funcion: ");
        repeticiones = Integer.parseInt(scan.nextLine());

        // Activamos //

        for (int i = 0; i < repeticiones; i++) {
            System.out.println(raizRamdom());
        }

        // Cerramos Scanner //
        scan.close();
    }

    public static float raizRamdom(){

        Random rand = new Random();
        int aleatorio = rand.nextInt(355 - 2 + 1) + 2;

        return (float)Math.sqrt(aleatorio);

    }
}