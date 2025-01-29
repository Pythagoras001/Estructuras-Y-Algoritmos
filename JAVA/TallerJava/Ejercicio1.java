package JAVA.TallerJava;
import java.util.Scanner;

/*
 * Diseñe un algoritmo para saludar al usuario: Hola usuario.
 * El nombre del usuario es ingresado por teclado
*/

public class Ejercicio1 {

    public static void main(String[] args) {
    
        try {
            Scanner scan = new Scanner(System.in);

            String nombre = "";

            System.out.println("Ingrese su nombre: ");
            nombre = scan.nextLine();

            System.out.println("Buenos dias, "+nombre);

            scan.close();

        } catch (Exception error) {
            System.out.println(error);
        }
        
    }
}