package EstudioJava.TallerStringP2;

import java.util.Scanner;

public class ejercicio4 {

    // Creamos el alfabeto romano
    public static final String[] letrasRoma = {"I", "V", "X", "L", "C", "D", "M"}; 
    public static final Integer[] numerosRoma = {1, 5, 10, 50, 100, 500, 1000};
    
    public static void main(String[] args) {
        
        // Creamos las varibles
        Scanner scan = new Scanner(System.in);
        String num = "";
        int numAct = 0;

        String respuesta = "";
        int potencia = 0;

        // Solicitamos la entrada
        num = scan.nextLine();

        // Procesamos la entrada
        for (int i = num.length()-1; i > -1; i--) {
            
            potencia = (int)(Math.pow(10, num.length()-(i+1)));
            numAct = (num.charAt(i) - '0') * potencia;

            respuesta = ((num.charAt(i) == '4' || num.charAt(i) == '9') ? sustraerRoma(numAct) : sumarRoma(numAct)) + respuesta;

        }

        // Damos la salida
        System.out.println(respuesta);

        // Cerramos Scanner 
        scan.close();
    }

    // Creamos una funcion si toca restar al numero
    public static String sustraerRoma(int numero){
        int resta = 0;
        String respuesat = "";

        for (int i = letrasRoma.length-1; i > -1 ; i--) {

            if (numerosRoma[i] > numero && numerosRoma[i-1] < numero) {
                resta = numerosRoma[i];
                respuesat += letrasRoma[i];
            }

            if (resta - numerosRoma[i] == numero) respuesat = letrasRoma[i] + respuesat;
        }
        return respuesat;
    }

    // Creamos una funcion si toca sumar al numero
    public static String sumarRoma(int numero){
        String respuesat = "";
        int limite = 0;

        for (int i = letrasRoma.length-1; i > -1 ; i--) {

            if (numerosRoma[i] <= numero) {
                limite = numero / numerosRoma[i];
                numero -= limite * numerosRoma[i];

                for (int j = 0; j < limite ; j++) respuesat += letrasRoma[i];
            }
        }
        return respuesat;
    }
}