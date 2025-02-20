
package EstudioJava.Quiz;

import java.util.Scanner;

public class Propuesta1 {
    
    public static void main(String[] args){
        
        try{
            
            Scanner sc = new Scanner(System.in);
            
            // Datos Entrada
            short tipoCombo = 0;
            short cantidadCombo = 0;
            short cantidadBoleta = 0;
            
            String tipoBoleta = "";
            
            // Datos Salida
            int valorCombo = 0;
            int valorBoleta = 0;
            
            float descuentoCombo = 0f;
            float valorTotal = 0f;
            
            // Variables Adicionales
            
            
            // Proceso
            
            //Paso #1 Solicitar los datos que el enunciado indica
            
            System.out.println(" * * * Cine * * *");
            
            System.out.print("Seleccione el tipo de Boleta: \n(G : General $10.000 | V : VIP $15.000) : ");
            tipoBoleta = sc.nextLine();
            
            System.out.print("Ingrese la cantidad de boletas de tipo " + tipoBoleta + " : ");
            cantidadBoleta = sc.nextShort();
            sc.nextLine();
            
            System.out.print("Seleccione el tipo de Combo: \n(1 : Hamburguesa y Perro $40.000 | 2 : Crispeta y Gaseosas $30.000 | 3 : Perros y Gaseosas $42.000) : ");
            tipoCombo = sc.nextShort();
            sc.nextLine();
            
            System.out.print("Ingrese la cantidad de Combos de tipo " + tipoCombo + " : ");
            cantidadCombo = sc.nextShort();
            sc.nextLine();
            
            // Paso #2 Implementar operaciones
            // En este punto del código, nuestras variables ya tendran un valor con el cual realizaremos operaciones
            
            // Como ya tengo el tipo de boleta y la cantidad que el usuario desea, ya puedo ejecutar la funcion calcularValorBoleta
            // y enviarle los dos recursos (parametros que solicita)
            
            // Recuerden que al invocar una funcion, como esta retorna un valor, lo debo de almacenar en una variable
            
            valorBoleta = calcularValorBoleta(tipoBoleta, cantidadBoleta);
            
            // Como ya tengo el tipo de combo y la cantidad que el usuario desea, ya puedo ejecutar la funcion calcularValorCombo
            // y enviarle los dos recursos (parametros que solicita)
            
            valorCombo = calcularValorCombo(tipoCombo, cantidadBoleta);
            
            // El enunciado especifica un paso adicional y agregarle un descuento al valor total del combo en caso de que el cliente sea V
            
            // En este punto de mi codigo ya tengo el tipo de boleta (solicitada en la linea 37
            // Tambien tengo el valor del combo (invocamos la funcion en la linea 64)
            // Con esos datos, ya puedo validar que tipo de cliente y si le asigno descuento o no
            
            if(tipoBoleta.equals("V")){
                // Invoco a la funcion para calcular el descuento
                
                descuentoCombo = calcularDescuentoCombo(tipoCombo, valorCombo);
            }
            else if(tipoBoleta.equals("G")){
                // No invoco la funcion ya que esta es solo util cuando el tipo de boleta es V
                // En este caso no hay descuento y lo pongo en cero
                
                descuentoCombo = 0f;
            }
            else{
                descuentoCombo = 0f;
            }
            
            valorTotal = valorCombo + valorBoleta - descuentoCombo;
            
            // En este punto de mi codigo, ya todos los procesos y aspectos a controlar fueron gestionados y puedo exponer la informacion a los usuarios
            
            System.out.println("Tipo de Silla : " + tipoBoleta + " - Cantidad : " + cantidadBoleta 
            + "\n - Valor Boletas : $" + valorBoleta + "\nNumero de Combo : " + tipoCombo + " - Cantidad : " + cantidadCombo
            + "\n - Valor Neto Combo : $" + valorCombo + "\nValor Descuento: $" + descuentoCombo + "\nValor Total : $" + valorTotal);
            sc.close();
        }
        catch(Exception e){
            System.out.println("Error: " + e.getMessage() + "\n\n" + e);
        }
        

        
    }
    
    // Funciones
    
    // Funcion Calcular valor Combo
    // Objetivo: Segun el tipo de combo y la cantidad, devolverle al usuario el valor del combo
    
    public static int calcularValorCombo(short comboSeleccionado, short cantidadSeleccionada){
        
        try{
            
            // Podemos crear variables dentro de funciones, pero, recuerden que solo seran usadas dentro de la funcion
            
            int valorNetoCombo = 0;
            
            // Recuerden usar variables al momento de realizar operaciones y no tener valores regados por todo el codigo
            
            int valorCombo_1 = 40000;
            int valorCombo_2 = 30000;
            int valorCombo_3 = 42000;
            
            
            switch(comboSeleccionado){
                case 1:
                    valorNetoCombo = valorCombo_1 * cantidadSeleccionada;
                break;
                case 2:
                    valorNetoCombo = valorCombo_2 * cantidadSeleccionada;
                break;
                case 3:
                    valorNetoCombo = valorCombo_3 * cantidadSeleccionada;
                break;
                default:
                    // En este caso, el default representa una opcion de combo erronea que el usuario ingreso
                    valorNetoCombo = 0;
                break;
            }
            
            return valorNetoCombo;
        }
        catch(Exception e){
            // La funcion retorna un valor numerico y recuerden que el catch es el apartado que debe de retornar un error
            // En este caso, me parece que el -1 puede indicarnos que sucedio un error dentro de esta funcion
            return -1;
        }
        
    }
    
    // funcion Calcular valor Boleta
    // Objetivo: Segun el tipo de boleta y la cantidad, devolverle al usuario el valor de la boleta
    
    public static int calcularValorBoleta(String boletaSeleccionada, short cantidadBoletaSeleccionada){
        
        try{
            
            int valorNetoBoleta = 0;
            
            int valorBoletaG = 10000;
            int valorBoletaV = 15000;
            
            // Para esta funcion utilice una serie de condiciones if para continuar con el aprendizaje y repaso
            // Pero, tambien podria haber implementado un switch y el proceso seria el mismo
            
            if(boletaSeleccionada.equals("V")){
                
                valorNetoBoleta = valorBoletaV * cantidadBoletaSeleccionada;
                
            }
            else if(boletaSeleccionada.equals("G")){
                
                valorNetoBoleta = valorBoletaG * cantidadBoletaSeleccionada;
                
            }
            else{
                
                // En este caso el else representa una opcion invalida que el usuario ingreso
                // En este caso especificarle que el valor Neto Boleta = 0 me parece que es pertinente
                
                valorNetoBoleta = 0;
            }
            
            return valorNetoBoleta;
                    
            
        }
        catch(Exception e){
            return -1;
        }
        
    }
    
    // Funcion Calcular Descuento Combo
    // Objetivo: Segun el tipo de combo, retornar su respectivo descuento
    
    public static float calcularDescuentoCombo(short tipoComboSeleccionado, int valorNetoComboCalculado){
        
        try{
            
            float valorDescuentoCombo = 0f;
            
            float porcentajeDctoCombo_1 = 0.05f;
            float porcentajeDctoCombo_2 = 0.06f;
            float porcentajeDctoCombo_3 = 0.03f;
                    
            if(tipoComboSeleccionado == 1){
                valorDescuentoCombo = (float)valorNetoComboCalculado * porcentajeDctoCombo_1;
            }
            else if(tipoComboSeleccionado == 2){
                valorDescuentoCombo = (float)valorNetoComboCalculado * porcentajeDctoCombo_2;
            }
            else if(tipoComboSeleccionado == 3){
                valorDescuentoCombo = (float)valorNetoComboCalculado * porcentajeDctoCombo_3;
            }
            else{
                valorDescuentoCombo = 0;
            }
            
            return valorDescuentoCombo;
            
        }
        catch(Exception e){
            return -1;
        }
        
    }
}
