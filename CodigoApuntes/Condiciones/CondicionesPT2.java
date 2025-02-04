package Condiciones;

import java.util.Scanner;

public class CondicionesPT2 {
    
    public static void main(String[] args) {
        
        try {

            Scanner cr7 = new Scanner(System.in);

            short caraDado = 0;

            System.out.println("Ingrese la cara del dado: ");
            caraDado = cr7.nextShort();
            cr7.nextLine();

            switch (caraDado){

                case 1:
                    System.out.println("La contrario es 6");
                    break;
                case 2:
                    System.out.println("La contraria es 5");
                    break;
                case 3:
                    System.out.println("La contraria es 4");
                    break;
                case 4:
                    System.out.println("La contraria es 3");
                    break;
                case 5:
                    System.out.println("La contraria es 2");
                    break;
                case 6:
                    System.out.println("La contraria es 1");
                    break;
                default:
                    System.out.println("Valor invalido");
                    break;

            }
            cr7.close();
            
        } 


        catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

    }

}
