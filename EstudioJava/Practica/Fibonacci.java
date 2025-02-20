package EstudioJava.Practica;

import java.util.HashMap;
import java.util.Scanner;

public class Fibonacci {

    public static void main(String[] args) {
        
        try {

            // Creamos las variables //
            Scanner scan = new Scanner(System.in);
            int num = 0;
            HashMap<Integer, Integer> memo = new HashMap<>();
            
            // Solicictamos la entrada //
            System.out.println("Ingrese el numero");
            num = Integer.parseInt(scan.nextLine());

            // Procesamos la salida //
            System.out.println("El numero correspondiente en la serie es: " + fibo(num, memo));

            // Cerramos Scanner //
            scan.close();
            
        } catch (Exception e) {
            System.out.println("Error" + e.getMessage());
        }
    }

    // Cremos la funcion fibo //
    public static int fibo(int x, HashMap<Integer, Integer> memo){

        try {
            int respuesta = 0;

            if (x == 1 || x == 2){
                return 1;
            }

            if(memo.containsKey(x)){
                return memo.get(x);
            }

            respuesta = fibo(x-1, memo) + fibo(x-2, memo);
            memo.put(x, respuesta);

            return respuesta;

        } catch (Exception e) {
            return -1;
        }
    }

}
