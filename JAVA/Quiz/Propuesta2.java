package JAVA.Quiz;

import java.util.HashMap;
import java.util.Scanner;

public class Propuesta2 {

    public static void main(String[] args) {
        
        try {
            
            //  CREAMOS LAS VARIBLES //
            Scanner scan = new Scanner(System.in);
            String tipVehiculo = "";
            int tiempoHora = 0;

            int costoIncremento = 0;
            int descuento = 0;
            int tiempoExtra = 0;
            boolean esEstudiante = false;

            float cuentaTotal = 0f;
            float cuentaDescuento = 0f;

            //  RECIBIMOS LA ENTRADA //
            System.out.println("""
                    - Costo por Hora -
                    Carro: $5.000
                    Moto: $5.000
                    Bicicleta: $5.000
                    """);
            
            System.out.println("Ingrese el tipo de vehiculo estacionado:");
            tipVehiculo = scan.nextLine();

            System.out.println("Cual fue su tiempo de estacionamiento en Horas: ");
            tiempoHora = Integer.parseInt(scan.nextLine());

            System.out.println("Es usted estudiate \nYes: Y \nNo: N ");
            esEstudiante = (scan.nextLine().equals("Y")) ? true : false;

            // CALCULAMOS EL COSTO DEL INCREMENTO DEACUERDO CON EL TIEMPO //
            costoIncremento = calcularIncremento(tiempoHora);

            // CALCULAMOS EL TIEMPO EXTRA EN EL ESTACIONAMIENTO //
            tiempoExtra = calcularHorasExtras(tiempoHora);

            // CALCULAMOS CUAL ES EL DESCUENTO TODAL SEGUN LAS EL TIEMPO Y SI ES ESTUDIANTE //
            descuento = calcularDescuento(tiempoHora, esEstudiante);
       
            // CALCULAMOS EL COSTO TOTAL SIN DESCUENTO //
            cuentaTotal = calcularCostoTotal(tiempoHora, tipVehiculo, costoIncremento, tiempoExtra);

            // CALCULAMOS EL COSTO TOTAL TENIENDO EN CUENTA EL COSTO TOTAL E IVA //
            cuentaDescuento = calcularCostoDescuento(cuentaTotal, descuento);

            // IMPRIMIMOS EL RECIBO //
            System.out.printf("""
                    Su tipo de vehiculo es: %s
                    El tiempo total estacionado es: %d
                    El valor total antes de los descuentos es: %f
                    Su descueto total es: %d 
                    El valor a pagar es: %f
                    """, tipVehiculo, tiempoHora, cuentaTotal, descuento, cuentaDescuento);

            // CERRAMOS SCANNER //
            scan.close();

        } catch (Exception error) {
            System.out.println("Error: " + error.getMessage());
        }

    }

    // CREAMOS UNA FUNCION PARA CALCULAR EL INCREMENTO COSTO-HORA SEGUN EL TIEMPO //
    public static int calcularIncremento(int tiempo){
        try {

            int incremento = 0;
            if(tiempo > 3){
                incremento = 2000;
            }
            return incremento;

        } catch (Exception e) {
            return -1;
        }
    }

    // CREAMOS UNA FUNCION PARA CALCULAR LAS HORAS EXTRAS EN EL PARQUEADERO SEGUN EL TIEMPO //
    public static int calcularHorasExtras(int tiempo){
        try {

            int horaExtra = 0;
            if(tiempo > 3){
                horaExtra += tiempo-3;
            }
            return horaExtra;
            
        } catch (Exception e) {
            return -2;
        }
    }

    // CREAMOS UNA FUNCIOM PARA CALCULAR EL DESCUETNO TOTAL SEGUN TIEMPO-ES ESTUDIANTE //
    public static int calcularDescuento(int tiempo, boolean esEstudiante){
        try {

            int totalDescuento = 0;
            totalDescuento += (tiempo > 4) ? 30 : 0;
            totalDescuento += (esEstudiante) ? 5 : 0;
            return totalDescuento;

        } catch (Exception e) {
            return -3;
        }
    }

    // CALCULAMOS EL COSTO TOTAL DE LA PARQUEDA //
    public static float calcularCostoTotal(int tiempo, String tipoVehiculo, int incremento, int horasExtra){
        try {
            
            float costoTotal = 0f;
            float iva = 1.19f;

            HashMap<String, Integer> costosVehiculos = new HashMap<String, Integer>();
            costosVehiculos.put("Carro", 5000);
            costosVehiculos.put("Moto", 3000);
            costosVehiculos.put("Bicicleta", 1000);

            costoTotal += (tiempo-horasExtra) * costosVehiculos.get(tipoVehiculo); // Costo por menos de 3h
            costoTotal += horasExtra * (costosVehiculos.get(tipoVehiculo)+incremento); // costo por horas extra (mayor de 3h)
            costoTotal += costoTotal * iva; // Le damos el iva

            return costoTotal;

        } catch (Exception e) {
            return -4f;
        }
    }

    // CREAMOS UNA FUNCION PARA CALCULAR EL COSTO CON DESCUENTO //
    public static float calcularCostoDescuento(float costoTotal, int descuento){
        try {

            float costoDescuento = 0f;
            costoDescuento += costoTotal - (costoTotal*(descuento/100)); // Le aplicamos el descuento al total de la cuenta
            return costoDescuento;

        } catch (Exception e) {
            return -5f;
        }
    }

}
