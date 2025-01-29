package JAVA.Conceptos;

import java.util.ArrayList;
import java.util.Arrays;

public class Bucles {
    public static void main(String[] args) {
        
        ArrayList<String> nombres = new ArrayList<>(Arrays.asList("pedro", "juan"));

        // De esta manera iteramos sobre los elmentos de una lista
        for (String string : nombres) {
            System.out.println(string);
        }

        // Aqui tenemos un for anidado
        for (int i = 0; i < 5; i++) {
            for (int j = i; j < 5; j++) {
                System.out.println(j);
                
            }
        }

        // Aqui usamos un while para encontrar el primer numero Impar
        boolean k = true;
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(2, 4, 6, 5));
        Integer n = 0;

        while (k) {
            if (numeros.get(n) % 2 == 1) {
                System.out.println(numeros.get(n));
                k = false;
            }
            n++;
        }

    }
}
