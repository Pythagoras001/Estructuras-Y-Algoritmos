package JAVA.TallerJava;
import java.util.Scanner;

/*
 * Diseñe un algoritmo para saludar al usuario: Hola usuario.
 * El nombre del usuario es ingresado por teclado
*/

public class Ejercicio1 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
    
        try {
            System.out.println("Ingrese su nombre: ");
            String nombre = scan.nextLine();

            System.out.println("Buenos dias, "+nombre);

        } catch (Exception error) {
            System.out.println(error);
        }
        scan.close();
    }
}