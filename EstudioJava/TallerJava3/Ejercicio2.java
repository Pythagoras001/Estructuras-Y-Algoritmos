package EstudioJava.TallerJava3;

import java.util.Scanner;

public class Ejercicio2 {
    
    public static void main(String[] args) {
        

        try {

            // Creamos las varibles //
            Scanner scan = new Scanner(System.in);
            int modelo = 0;
            int avaluo = 0;
            float impRoda = 0f;
            float impSegu = 0f;

            // Solicitamos la entrada //
            System.out.println("Ingrese el modelo:");
            modelo = Integer.parseInt(scan.nextLine());
            
            System.out.println("Ingrese el avaluo:");
            avaluo = Integer.parseInt(scan.nextLine());
            
            // Calcular los Impuestos //
            switch (modelo) {
                case 70:
                    impSegu = avaluo*(0.876f/100f);
                    impRoda = avaluo*(3.76f/100f);
                    break;
                case 80:
                    impSegu = avaluo*(0.854f/100f);
                    impRoda = avaluo*(3.98f/100f);
                    break;
                case 90:
                    impSegu = avaluo*(0.816f/100f);
                    impRoda = avaluo*(4.09f/100f);
                    break;
                case 00:
                    impSegu = avaluo*(0.798f/100f);
                    impRoda = avaluo*(4.34f/100f);
                    break;
                case 10:
                    impSegu = avaluo*(0.712f/100f);
                    impRoda = avaluo*(4.93f/100f);
                    break;
                case 20:
                    impSegu = avaluo*(0.699f/100f);
                    impRoda = avaluo*(5.680f/100f);
                    break;

                default:
                    impSegu = avaluo*(0.9f/100f);
                    impRoda = avaluo*(6f/100f);
                    break;
            }
        
        // Damos la salido //
        System.out.println(
            "El valor del avaluo es: "+ avaluo + "$\n" + 
            "El valor del impuesto de rodamiento es: "+ String.format("%.2f", impRoda) + "$\n" + 
            "El valor del impuesto del seguro es "+ String.format("%.2f", impSegu) + "$\n" +
            "El costo total es: "+ String.format("%.2f", (impRoda + impSegu)) + "$\n" 
        );

        // Cerramos Scanner //
        scan.close();

        } catch (Exception error) {
            System.out.println("Error: " + error.getMessage());
        }
    }
}
