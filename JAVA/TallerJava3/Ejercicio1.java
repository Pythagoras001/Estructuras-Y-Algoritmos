package JAVA.TallerJava3;

import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        try {

            // Creamos las variables //
            Scanner scan = new Scanner(System.in);
            int camas = 0;
            String ventilacion = "";

            // Solicitamos la informacion //
            while (true) {
                System.out.println("Ingrese el número de camas que necesita en la habitación:");
    
                if (scan.hasNextInt()) {
                    camas = scan.nextInt();
                    scan.nextLine();
                    break;
                } else {
                    System.out.println("Entrada inválida, intente de nuevo.");
                    scan.next();
                }
            }

            System.out.println("Ingrese el tipo de ventilacion VE-AA: ");
            ventilacion = scan.nextLine();

            // Buscamos las habitaciones disponibles //
            switch (ventilacion) {
                case "AA":

                    switch (camas) {
                        case 2:
                            System.out.println(
                            "-Habitacion disponible: 101-Primer Piso \n" +
                            "-Habitacion disponible: 301-Tercer Piso");
                            break;
                        case 3:
                            System.out.println(
                            "-Habitacion disponible: 201-Segundo Piso \n");
                            break;
                        default:
                            System.out.println("No hay habitaciones disponibles");
                            break;
                    }
                    break;
            
                case "VE":

                    switch (camas) {
                        case 1:
                            System.out.println("Habitacion disponible: 102-Primer Piso");
                            break;
                        case 2:
                            System.out.println("Habitacion disponible: 202-Segundo Piso");
                            break;
                        default:
                            System.out.println("No hay habitaciones disponibles");
                            break;
                    }
                    break;

                default:
                    break;
            }

            // Cerramos Scanner //
            scan.close();
            
        } catch (Exception error) {
            System.out.println("Error: " + error.getMessage());
        }
    }
}