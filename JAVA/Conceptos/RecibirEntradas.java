package JAVA.Conceptos;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class RecibirEntradas {
    public static void main(String[] args) {
        
        // HACER UNA LISTA DE LISTAS
        List<List<Integer>> listaPrincipal = Collections.nCopies(5, new ArrayList<>());
        System.out.println(listaPrincipal);

        // RECIBIR UNA LISTA
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese números separados por espacios:");
        String entrada = scanner.nextLine(); // Leer la línea completa

        
        List<Integer> lista = new ArrayList<>(); // Crear una lista y dividir la entrada en números

        for (String num : entrada.split(" ")) {
            lista.add(Integer.parseInt(num)); // Convertir y agregar a la lista
        }
        System.out.println(lista);

        scanner.close();

    }
    
}
