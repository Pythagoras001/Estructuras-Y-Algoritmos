package JAVA;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;


public class Listas {
    public static void main(String[] args) {
        
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(1, 2, 3));

        // Agregar elementos a la lista
        numeros.add(10);

        // Imprimir la lista completa
        System.out.println("Lista: " + numeros);

        // Acceder a un elemento por su índice
        System.out.println("Primer elemento: " + numeros.get(0));

        // Modificar un elemento
        numeros.set(1, 25);
        System.out.println("Lista modificada: " + numeros);

        // Eliminar un elemento
        numeros.remove(0);
        System.out.println("Lista después de eliminar: " + numeros);

        // Tamaño de la lista
        System.out.println("Tamaño de la lista: " + numeros.size());

        // Ordenar una lista de menor a mayor
        Collections.sort(numeros);

        // Mayor a menor
        Collections.sort(numeros, Collections.reverseOrder());
        
    }
    
}
