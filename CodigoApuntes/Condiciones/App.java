package Condiciones;

import java.util.Scanner;

public class App {
    
    public static void main(String[] args) {
       
        try{

            Scanner sc = new Scanner(System.in);
            //sc.useLocale(Locale.US);

            int edadUsuario = 0;
            String nombreUsuario = ""; 
            float alturaUsuario = 0f;

            // Solicitar datos
            System.out.println("Ingrese su edad: ");

            edadUsuario = sc.nextInt();
            //Primera solucion para solicitar datos numericos y luego Strings
            sc.nextLine();
            //Segunda solucion: Hacer una conversion explicita de String al tipo de dato numerico
            //Integer.parseInt(sc.nextLine());

            System.out.print("Ingrese su nombre: ");

            nombreUsuario = sc.nextLine();

            System.out.println("El usuario: " + nombreUsuario + " tiene: " + edadUsuario + " años.");

            //para almacenar datos short
            //sc.nextShort();
            //para almacenar datos byte
            //sc.nextByte();
            //para almacenar datos long
            //sc.nextLong

            System.out.print("Ingrese su altura: ");
            
            alturaUsuario = sc.nextFloat();
            sc.nextLine();

            // Crear condiciones

            if(edadUsuario >= 18){
                System.out.println("Es mayor de edad, puede ingresar a Dulcinea");
            }
            else{
                System.out.println("Es menor de edad, llamar a la mama a que lo recoja");
            }

            // Crear condiciones multiples

            if(alturaUsuario < 1.4f){
                System.out.println("Estas un poco pequeño");
            }
            else if(alturaUsuario > 1.4f){
                System.out.println("Esta en el estandar");
            }
            else{
                System.out.println("Mides 1.4");
            }

            sc.close();

        }
        catch(Exception error){
            System.out.println("Error: " + error + "\n: " + error.getMessage());
        }        

    }

}
