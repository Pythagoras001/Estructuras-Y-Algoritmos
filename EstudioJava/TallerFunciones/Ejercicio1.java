package EstudioJava.TallerFunciones;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        
        // CREAMOS LAS VARIBLES //
        Scanner scan = new Scanner(System.in);

        int distX = 0;
        int distY = 0;

        int ambuX_1 = 0;
        int ambuY_1 = 0;

        int ambuX_2 = 0;
        int ambuY_2 = 0;

        int tarifa = 0;

        double ambuDist_1 = 0;
        double ambuDist_2 = 0;
        double ambuCost_1 = 0;
        double ambuCost_2 = 0;

        // RECIBIMOS LA ENTRADA //
        System.out.println("Ingrese la coordenada X: ");
        distX = Integer.parseInt(scan.nextLine());
        System.out.println("Ingrese la coordenada Y: ");
        distY = Integer.parseInt(scan.nextLine());

        System.out.println("Ingrese el valor del costo por metro: ");
        tarifa = Integer.parseInt(scan.nextLine());

        System.out.println("Ambulancia 1 - Coordenada X: ");
        ambuX_1 = Integer.parseInt(scan.nextLine());
        System.out.println("Ambulancia 1 - Coordenada Y: ");
        ambuY_1 = Integer.parseInt(scan.nextLine());

        System.out.println("Ambulancia 2 - Coordenada X: ");
        ambuX_2 = Integer.parseInt(scan.nextLine());
        System.out.println("Ambulancia 2 - Coordenada Y: ");
        ambuY_2 = Integer.parseInt(scan.nextLine());

        // CALCULAMOS LA DISTANCIA DE LA AMBULANCIA 1 //
        ambuDist_1 = calcularDistancia(ambuX_1, ambuY_1, distX, distY);

        // CALCULAMOS LA DISTANCIA DE LA AMBULANCIA 2 //
        ambuDist_2 = calcularDistancia(ambuX_2, ambuY_2, distX, distY);

        // CALCULAMOS EL PRRECIO POR AMBULANCIA 1 //
        ambuCost_1 = calcularCosto(ambuDist_1, tarifa);

        // CALCULAMOS EL PRRECIO POR AMBULANCIA 2 //
        ambuCost_2 = calcularCosto(ambuDist_2, tarifa);

        // DAMOS LA SALIDA //

        System.out.println("-Ambulancia 1-");
        System.out.println("Distancia: " + ambuDist_1 + "\nCosto: " + ambuCost_1);
        System.out.println("");
        System.out.println("-Ambulancia 2-");
        System.out.println("Distancia: " + ambuDist_2 + "\nCosto: " + ambuCost_2);
        
        if (ambuDist_1 <= ambuDist_2) {
            System.out.println("La ambulacia_1 es la mas cercana esta: " + ambuDist_1 + "M" + "\nTiene un costo de: " + "$" + ambuCost_1);
        }else{
            System.out.println("La ambulacia_1 es la mas cercana esta: " + ambuDist_2 + "M" + "\nTiene un costo de: " + "$" + ambuCost_2);
        }

        // CERRAMOS SCANNER //
        scan.close();

    }

    public static double calcularDistancia(int cordX, int cordY, int destinoX, int destinoY){
        double distTotal = 0;
        int potencia = 2;

        distTotal += Math.sqrt(Math.pow(destinoX - cordX, potencia) + Math.pow(destinoY - cordY, potencia));
        
        return Math.round(distTotal * 100.0) / 100.0;
    }
    
    public static double calcularCosto(double distancia, int tarifa){
        double costoTotal = 0;
        costoTotal += distancia * tarifa;
        return Math.round(costoTotal * 100.0) / 100.0;
    }


}
