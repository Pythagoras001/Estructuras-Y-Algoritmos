
package funciones;

import java.util.Scanner;

public class App {
    
    public static void main(String[] args) {

        try{

            Scanner sc = new Scanner(System.in);

            // Datos Entrada
            int valor_1 = 0;
            int valor_2 = 0;
            
            // Datos Salida
            int resultadoFuncionSuma = 0;

            // Variables Adicionales


            // Proceso

            System.out.print("Ingrese el primer valor a sumar: ");
            valor_1 = sc.nextInt();
            sc.nextLine();

            System.out.print("Ingrese el segundo valor a sumar: ");
            valor_2 = sc.nextInt();
            sc.nextLine();

            resultadoFuncionSuma = sumaValores(valor_1, valor_2);

            System.out.println("El resultado de la suma es: " + resultadoFuncionSuma);

            System.out.print("Ingrese el primer valor a sumar: ");
            valor_1 = sc.nextInt();
            sc.nextLine();

            System.out.print("Ingrese el segundo valor a sumar: ");
            valor_2 = sc.nextInt();
            sc.nextLine();

            resultadoFuncionSuma = sumaValores(valor_1, valor_2);

            System.out.println("El resultado de la suma es: " + resultadoFuncionSuma);

        }
        catch(Exception e){
            System.out.println("Error: " + e.getMessage());
        }
        
    }

    // Funciones

    public static int sumaValores(int valorA, int valorB){

        try {
            int resultadoSuma = valorA + valorB;

            return resultadoSuma;
        } 
        catch (Exception e) {
            return -1;
        }
        
    }

}
