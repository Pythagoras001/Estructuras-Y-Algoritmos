package JAVA.TallerJava;

import java.util.Scanner;

/*
Diseñe un algoritmo que calcule el tiempo necesario para alcanzar un destino el
usuario ingresará la velocidad promedio en kilómetros/hora y la distancia en
kilómetros
*/

public class Ejercicio6 {

    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String PURPURA = "\u001B[35m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        try {
            System.out.println(BLUE + "Ingrese su velocidad Km/h: ");
            float speed = scan.nextFloat();

            System.out.println(YELLOW + "Ingrese la distancia Km: ");
            float distand = scan.nextFloat();

            System.out.println(PURPURA + "Se tardara " + String.format("%.2f", distand/speed)+ " Horas" + RESET);
            
        } catch (Exception error) {
            System.out.println(error);
        }

        scan.close();
    }
}

