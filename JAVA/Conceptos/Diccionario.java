package JAVA.Conceptos;

import java.util.HashMap;

public class Diccionario {
    public static void main(String[] args) {
        // Crear un diccionario (HashMap)
        HashMap<String, Integer> edades = new HashMap<>();

        // Agregar elementos (clave, valor)
        edades.put("Juan", 25);
        edades.put("Maria", 30);
        edades.put("Pedro", 22);

        // Acceder a un valor usando una clave
        System.out.println("Edad de Juan: " + edades.get("Juan"));

        // Verificar si una clave existe
        if (edades.containsKey("Maria")) {
            System.out.println("María está en el diccionario.");
        }

        // Recorrer el diccionario
        for (String nombre : edades.keySet()) {
            System.out.println(nombre + " tiene " + edades.get(nombre) + " años.");
        }

        // Eliminar un elemento
        edades.remove("Pedro");

        // Ver el tamaño del diccionario
        System.out.println("Número de elementos: " + edades.size());
    }
}
