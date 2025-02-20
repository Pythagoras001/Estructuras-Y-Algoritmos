package EstudioJava.TallerJava3;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        
        try {
            
            // Creamos las variables //
            Scanner scan = new Scanner(System.in);
            double peso = 0;
            double altura = 0;
            double imc = 0;

            // Solicitamos la entrada //
            System.out.println("Ingrese su peso en kg: ");
            peso = Double.parseDouble(scan.nextLine());

            System.out.println("Ingrese su altura en Mts: ");
            altura = Double.parseDouble(scan.nextLine());

            // Calculamos su IMC //
            imc = peso / (altura * altura);

            if (imc < 18.5) {
                System.out.println("Bajo Peso");
            }else if(imc < 25){
                System.out.println("Peso Normal");
            }else if(imc < 30){
                System.out.println("Sobre Peso");
            } else {
                System.out.println("Obesidad");
            }

            // Cerramos Scanner //
            scan.close();

        } catch (Exception error) {
            System.out.println("Error: " + error.getMessage());
        }
    }
}
