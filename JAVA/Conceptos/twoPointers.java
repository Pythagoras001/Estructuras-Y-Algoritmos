package JAVA.Conceptos;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class twoPointers {
    public static void main(String[] args) {
        
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        Collections.sort(numeros);

        Integer iz = 0;
        Integer der = numeros.size()-1;
        Integer target = 5000;


        while (iz < der) {
            Integer ope = numeros.get(iz)+numeros.get(der);
            if (ope == target) {
                System.out.println(iz + " " + der);
                break;
            } else if (ope < target){
                iz++;
            } else{
                der--;
            }
            
            if (iz == der) {
                System.out.println("EL CONJUNTO DE NUMERO NO EXISTE");
            }

        }
    }
}
