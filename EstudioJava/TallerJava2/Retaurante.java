package EstudioJava.TallerJava2;

import java.util.Arrays;
import java.util.Scanner;


public class Retaurante {

    // Agregamos colores //
    public static final String BLUE = "\u001B[34m";
    public static final String ROJO = "\033[31m";
    public static final String GREEN = "\u001B[32m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {

        try {

            // Creamos las variables y el objeto Scanner //
            Scanner scan = new Scanner(System.in);
            int postre = 10000;
            int vino = 100000;
            Short[] menu = {1, 2, 3};
            short opcion = 0;
            int cuenta = 0;

            // Solicitamos la entrada de la opcion //
            do {
                System.out.println(BLUE + "Ingrese el plato 1, 2, o 3: " + RESET);
                opcion = Short.parseShort(scan.nextLine());
                
                if (!Arrays.asList(menu).contains(opcion)){
                    System.out.println(ROJO + "Entrada Invalida");
                }
                   
            } while (!Arrays.asList(menu).contains(opcion));

            // Calculamos el costo //
            switch (opcion) {
                case 1:
                    System.out.println("Postre " + postre);
                    cuenta += postre;
                    break;
                case 2:
                    System.out.println("Vino " + vino + '$');
                    cuenta += vino;
                    break;
                case 3:
                    System.out.println("Postre Y Vino " + postre + vino + '$');
                    cuenta += vino + postre;
                    break;
                default:
                    break;
            }

            // Imprimimos la salida //
            System.out.println(GREEN + "Su Cuenta es de " + cuenta + '$' + RESET);
            
            // Cerramos Scaner //
            scan.close();

        } catch (Exception error) {
            System.out.println("Entrada Invelida: " + error.getMessage());
        }
    }
}
