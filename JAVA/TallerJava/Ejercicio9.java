package JAVA.TallerJava;

import java.util.Locale;
import java.util.Scanner;

/*
Elaborar un algoritmo que, dadas 5 notas y los
5 porcentajes para una materia, calcule la nota final.
*/

public class Ejercicio9 {

    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String PURPURA = "\u001B[35m";
    public static final String NARANJA = "\u001B[33m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {

        try{

            Scanner scan = new Scanner(System.in);
            scan.useLocale(Locale.US);

            float acumulado = 0;

            for (int i = 0; i < 5; i++) {

                System.out.println(NARANJA + "Ingrese la nota y el porcentaje NOTA-PORCENTAJE: " + BLUE);
                String[] nota = scan.nextLine().split("-");

                acumulado += Float.parseFloat(nota[0]) * (Float.parseFloat(nota[1]) / 100);

            }
            
            System.err.println(PURPURA + "Tu promedio es de: " + String.format("%.1f", acumulado) + RESET);
            scan.close();

        } catch(Exception error){
            System.err.println(error);
        }
    }
}
