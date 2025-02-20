package EstudioJava.TallerJava1;

import java.util.Scanner;

/*
Solicitar al usuario la cantidad de días, horas, minutos y segundos 
y mostrar el tiempo total en segundos. 
*/

public class Ejercicio5 {

    // Ingresamos una gama de colores para la terminal 
    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String PURPURA = "\u001B[35m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {
       
        try {
            Scanner scan = new Scanner(System.in);


            System.out.println(BLUE + "Ingrese la hora en formato DD/HH/MM/SS: ");
            String[] timelist = scan.nextLine().split("/");
            int c = 0;

            c += Integer.parseInt(timelist[0])*86400;
            c += Integer.parseInt(timelist[1])*3600;
            c += Integer.parseInt(timelist[2])*60;
            c += Integer.parseInt(timelist[3]);

            System.out.println(PURPURA + "El tiempo en segudos es: " + c + " seg" + RESET);

            scan.close();
           
        } catch (Exception error) { 
            System.out.println(error);

        }
    }
}
