package JAVA.TallerJava2;

import java.util.Scanner;

/*
Elabore un algoritmo que permita calcular el número
de semanas transcurridas entre dos años dados. Los
años deben estar entre 1900 y 2019.
Para efectos del ejercicio, pregunte al usuario si
quiere calcular los años con 52 semanas o con 52,1
semanas.
P L U S
Calcular el número de días
Calcular el número de minutos
*/

public class CantidadDeSemanas {

    // Agregamos colores //
    public static final String BLUE = "\u001B[34m";
    public static final String ROJO = "\033[31m";
    public static final String GREEN = "\u001B[32m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {
        
        try {
            
            // Creamos las variables y el objeto scaner //

            Scanner scan = new Scanner(System.in);
            int year1 = 0;
            int year2 = 0;
            float weekYear = 0f;
            float numWeek = 0f;
            float numDays = 0f;
            float minutes = 0f;

            // Solicitamos la entrada de los peridos //

            do {
                System.out.println(BLUE + "Ingrese la primera fecha entre los periodos 1900 y 2019: " + RESET);
                year1 = Integer.parseInt(scan.nextLine());

                if (year1 > 2019 || year1 < 1900){
                    System.out.println(ROJO + "Entrada Invalida Intente De Nuevo");
                }

            } while (year1 > 2019 || year1 < 1900);

            do {
                System.out.println(BLUE + "Ingrese la segunda fecha entre los periodos " + year1 + " y 2019: " + RESET);
                year2 = Integer.parseInt(scan.nextLine());

                if (year2 > 2019 || year2 < year1){
                    System.out.println(ROJO + "Entrada Invalida Intente De Nuevo");
                }

            } while (year2 > 2019 || year2 < year1);

            // Solicitamos la entrada de las equivalencias a semanas //

            do {
                System.out.println(BLUE + "Desea que el un año tenga 52 o 52.1 semanas?" + RESET);
                weekYear = Float.parseFloat(scan.nextLine());

                if (weekYear != 52 && weekYear != 52.1){
                    System.out.println(ROJO + "Entrada Invalida Intente De Nuevo");
                }

            } while (weekYear != 52 && weekYear != 52.1);

            // Procesamos la salida //

            numWeek = (year2 - year1) * weekYear;
            numDays = numWeek * 7;
            minutes = numDays * 1440;

            // Imprimimos la salida //

            System.out.println(GREEN + "El periodo entre años tiene: \n" 
            + String.format("%.1f",numWeek) + " Semanas \n" 
            + String.format("%.1f",numDays) + " Dias \n"
            + String.format("%.1f",minutes) + " Minutos " + RESET);

            // Cerramos Scaner //

            scan.close();

        } catch (Exception error) {
            System.out.println("Entrada Invalida: " + error.getMessage());

        }
    }
}

