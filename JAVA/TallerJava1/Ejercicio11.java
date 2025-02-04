package JAVA.TallerJava1;

import java.util.Scanner;

/*
.Se requiere un algoritmo para calcular el salario a pagar a un trabajador con los
siguientes datos ingresados por teclado:
- cantidad de horas normales laboradas
- cantidad de horas extras diurnas laboradas
- cantidad de horas extras nocturnas laboradas
- valor de la hora normal
El valor de las horas extras diurnas tiene un recargo adicional del 15% sobre la
hora normal.
El valor de las horas extras nocturnas tiene un recargo adicional del 35% sobre la
hora normal. 
*/

public class Ejercicio11 {

    public static final String BLUE = "\u001B[34m";
    public static final String PURPURA = "\u001B[35m";
    public static final String NARANJA = "\u001B[33m";
    public static final String RESET = "\u001B[0m";
    
    public static void main(String[] args) {
        
        try {

            Scanner scan = new Scanner(System.in);
            int horasNor = 0;
            int horasExtDia = 0;
            int horasExtNoche = 0;
            float costohora  = 0f;
            float salario = 0f;

            System.err.println(PURPURA + "Registre sus horas nomarles: ");
            horasNor = scan.nextInt();

            System.err.println("Registre sus horas extras diurnas; : ");
            horasExtDia = scan.nextInt();

            System.err.println("Registre sus horas extras nocturnas: ");
            horasExtNoche = scan.nextInt();

            System.err.println("Registre el costo por hora: ");
            costohora = scan.nextFloat();

            salario += costohora * ((horasExtDia * 1.15) + (horasExtNoche * 1.35) + (horasNor));

            System.err.println(NARANJA + "Su salario es de: " +  salario + RESET);

            scan.close();

        } catch (Exception error) {
            System.err.println(error);

        }
    }
}
