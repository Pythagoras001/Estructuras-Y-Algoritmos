package Funciones;

import java.util.Scanner;

public class propuestaClase {

    public static void main(String[] args) {
        
        try {

            Scanner entrada = new Scanner(System.in);

            // DE
            double temperatura = 0;
            String opcionConvertir = "";

            // DS
            double tempConversion = 0;


            // Var Adicionales


            // Proceso

            System.out.print("Ingrese la temperatura a convertir: ");
            temperatura = entrada.nextDouble();
            entrada.nextLine();

            System.out.print("Seleccione la opción (C: Celisus | F: Farenheit):  ");
            opcionConvertir = entrada.nextLine();

            tempConversion = conversorTemperatura((float)temperatura, opcionConvertir);

            System.out.println("La conversion es de: " + tempConversion + (opcionConvertir.equals("C") ? "°C" : "°F"));
            
            entrada.close();
        } 
        catch (Exception e) {
            System.out.println("Error: " + e + "\n" + e.getMessage());
        }

    }

    // Funciones
    public static double conversorTemperatura(float temp, String opcion){

        try {
            double resultadoConversion = 0;
            float constanteDivision = 9f / 5f;
            float constanteIndependiente = 32;

            if(opcion.equals("C")){
                resultadoConversion = (temp - (constanteIndependiente)) / constanteDivision;
            }
            else if(opcion.equals("F")){
                resultadoConversion = (temp * (constanteDivision)) + constanteIndependiente;
            }
            else{
                resultadoConversion = -999;
            }

            /*switch (opcion) {
                case "C":
                    return (temp * (constanteDivision)) + constanteIndependiente;
                case "F":
                    return (temp - (constanteIndependiente)) / constanteDivision ;
                default:
                    return -999;
            }*/
            
            return resultadoConversion;
        } 
        catch (Exception e) {
            return -999;
        }

    }


}
