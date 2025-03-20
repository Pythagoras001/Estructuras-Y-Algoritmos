
package archivos;

import java.io.*;

public class App {
    
    public static void main(String[] args) {
        
        try {
            
            // Paso #1 Identificar ruta del archivo
            String rutaArchivo = "app\\src\\main\\java\\archivos\\recursos\\temperaturas.txt";
            File ubicacionArchivo = new File(rutaArchivo);

            // Paso #2 Apertura Lectura
            FileReader archivoLectura = new FileReader(ubicacionArchivo);

            // Paso #3 Abrir el archivo en memoria
            BufferedReader datosMemoria = new BufferedReader(archivoLectura);

            // Paso #4 Recorrido Archivo
            String dato = "";
            int acumularTemp = 0;
            int contadorTemp = 0;
            int promedio = 0;

            //opcion #1
            while ((dato = datosMemoria.readLine()) != null) {
                
                acumularTemp += Integer.parseInt(dato.trim());
                contadorTemp++;

            }

            //opcion #2
            /*dato = datosMemoria.readLine();

            while (dato  != null) {
                
                System.out.println(dato);

                dato = datosMemoria.readLine();

            }*/

            // Escritura Archivo
            FileWriter archivoEscritura = 
            new FileWriter("app/src/main/java/archivos/recursos/promedioTemp.txt", false);

            PrintWriter escritura = new PrintWriter(archivoEscritura);

            promedio = acumularTemp / contadorTemp;

            escritura.println("El promedio de la temperatura es: " + promedio);

            datosMemoria.close();
            escritura.close();

        }
        catch (IOException io){
            System.out.println("Error de arhivos: " + io.getMessage() + "\n" + io);
        } 
        catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

    }

}
