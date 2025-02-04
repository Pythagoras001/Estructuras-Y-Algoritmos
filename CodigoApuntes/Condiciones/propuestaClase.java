package Condiciones;

import java.util.Scanner;

public class propuestaClase {

    public static void main(String[] args) {
        
        try {

            Scanner sc = new Scanner(System.in);

            // Creacion de variables
            double ingresoMensual = 0;
            double montoPrestamo = 0;
            double valorCuota = 0;
            double porcentajeCuota = 0;
            int plazoMeses = 0;

            // Proceso

            System.out.print("Ingrese el ingreso mensual: ");
            ingresoMensual = sc.nextDouble();
            sc.nextLine();

            System.out.println("Ingrese el monto del prestamo: ");
            montoPrestamo = sc.nextDouble();
            sc.nextLine();

            System.out.println("Ingrese el plazo en meses: ");
            plazoMeses = sc.nextInt();
            sc.nextLine();

            valorCuota = montoPrestamo / plazoMeses;
            porcentajeCuota = (valorCuota * 100) / ingresoMensual;

            System.out.println("El valor de la cuota es: $" + valorCuota);

            System.out.println("El porcentaje del valor de la cuota frente a su ingreso es de: " + porcentajeCuota + "%");

            System.out.println((porcentajeCuota > 30 ? "No aprobado" : "Aprobado") );

            sc.close();
            
        } 
        catch (Exception e) {
            System.out.println("Error: " + e + "\n: " + e.getMessage());
        }

    }

}
