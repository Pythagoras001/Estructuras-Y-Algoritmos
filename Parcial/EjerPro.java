import java.util.Scanner;
import java.io.*;

public class EjerPro {

    public static String RUTA_ARCHIVO = "Recursos\\";

    public static void main(String[] args) {
        
        try {
            
            Scanner sc = new Scanner(System.in);

            String resultadoFuncion = "";

            String archivosCreados = "";

            String nombreArchivo = "";

            int cantidadJugadas = 0;

            int opcionMenu = 0;

            do{

                System.out.println(" 1:Crear archivo | 2:Procesar jugada ");
                opcionMenu = Integer.parseInt(sc.nextLine());
                
                if(opcionMenu == 1){

                    System.out.print("Ingrese el nombre del archivo: ");
                    nombreArchivo = sc.nextLine();

                    System.out.print("Ingrese la cantidad de jugadas: ");
                    cantidadJugadas = Integer.parseInt(sc.nextLine());

                    resultadoFuncion = crearArchivo(nombreArchivo, cantidadJugadas);

                    archivosCreados += "\n* " + nombreArchivo + ".txt";

                }
                else if(opcionMenu == 2){

                    System.out.println("Escriba el nombre y extension de un archivo: " + archivosCreados + "\n >");
                    nombreArchivo = sc.nextLine();

                    resultadoFuncion = procesarArchivo(nombreArchivo);

                    System.out.println(resultadoFuncion);

                }
                else{

                    break;

                }

            }while(true);

            sc.close();

        } 
        catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

    }

    public static String crearArchivo(String nombreArchivo, int cantidadJugadas){

        try {

            int aleatorio = 0;

            String lineaEscritura = "";

            String procesoArchivo = "";

            String rutaArchivo = RUTA_ARCHIVO.replace("\\", "/") + nombreArchivo + ".txt";

            FileWriter archivoEscritura = new FileWriter(rutaArchivo, false);
            PrintWriter escritura = new PrintWriter(archivoEscritura);

            for(int j = 0; j < cantidadJugadas; j++){

                lineaEscritura = "";

                for(int i = 0; i < 4; i++){

                    aleatorio = (int)(Math.random() * 13  + 1);
    
                    lineaEscritura += aleatorio + " ";
    
                    if(i == 1){
                        lineaEscritura += "| ";
                    }
    
                }

                escritura.println(lineaEscritura);

            }

            escritura.close();
            
            procesoArchivo = "Proceso Exitoso";

            return procesoArchivo;
            
        } 
        catch (IOException io){
            return "Error en el archivo, funcion crearArchivo: " + io.getMessage();
        }
        catch (Exception e) {
            return "Error en la funcion crearArchivo: " + e.getMessage();
        }

    }

    public static String procesarArchivo(String nombreArchivo){

        try{

            String resultados = "";

            String linea = "";

            String rutaArchivo = RUTA_ARCHIVO + nombreArchivo;

            String [] jugadores;

            String [] cartasJugador;

            String [] cartasBanca;

            int sumaJugador = 0;

            int sumaBanca = 0;

            File ubicacionArchivo = new File(rutaArchivo);
            FileReader archivoLectura = new FileReader(ubicacionArchivo);
            BufferedReader datosArchivo = new BufferedReader(archivoLectura);

            while((linea = datosArchivo.readLine()) != null){

                if(linea.trim().isEmpty()) continue;

                jugadores = linea.split("\\|");

                cartasJugador = jugadores[0].trim().split(" ");

                cartasBanca = jugadores[1].trim().split(" ");

                for(int i = 0; i < cartasJugador.length; i++){

                    sumaJugador += Integer.parseInt(cartasJugador[i]);

                    sumaBanca += Integer.parseInt(cartasBanca[i]);

                }

                sumaJugador = sumaJugador % 10;
                
                sumaBanca = sumaBanca % 10;

                resultados += sumaJugador + " | " + sumaBanca;
                
                if(sumaJugador > sumaBanca){
                    resultados += " Gana Jugador \n";
                }
                else if(sumaJugador < sumaBanca){
                    resultados += " Gana Banca \n";
                }
                else{
                    resultados += " Empate \n";
                }

            }

            datosArchivo.close();

            return resultados;

        }
        catch (IOException io){
            return "Error en el archivo, funcion procesarArchivo: " + io.getMessage();
        }
        catch (Exception e) {
            return "Error en la funcion procesarArchivo: " + e.getMessage();
        }

    }

}

