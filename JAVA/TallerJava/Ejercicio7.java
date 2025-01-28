package JAVA.TallerJava;

import java.util.Locale;
import java.util.Scanner;

/*
Un avión necesita cargar combustible para cubrir sus rutas programadas en el día.

-Cada 0.2 toneladas de combustible puede recorrer 60.8 Km.
-En el despegue el avión consume 1.2 toneladas de combustible.
-En el aterrizaje consume 0.4 toneladas.

El piloto desea un algoritmo que, ingresando 4 rutas, y el kilometraje de cada ruta,
obtenga la cantidad de combustible que debe tanquear en el avión.
 */

public class Ejercicio7 {

    public static final String PURPURA = "\u001B[35m";
    public static final String YELLOW = "\u001B[33m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        scan.useLocale(Locale.US);

        try {
            float fuel = 0;

            for (int i = 1; i < 5; i++) {
                System.out.println(YELLOW + "Ingrese la ruta Numero " + i);
                float lengh = scan.nextFloat();
    
                fuel += ((lengh * 0.2)/60.8) + 1.6;
            }
    
            System.out.println(PURPURA + "El combustible necesario es: " + String.format("%.2f", fuel) + " Toneladas" + RESET);
    
        } catch (Exception error) {
            System.out.println(error);
        }


        scan.close();

    }
}
