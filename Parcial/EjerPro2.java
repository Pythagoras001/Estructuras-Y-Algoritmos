import java.util.Scanner;
import java.io.*;

public class EjerPro2 {

    public static String RUTA_ARCHIVO = "Recursos\\";

    public static void main(String[] args) {
        
        try {
            
            Scanner sc = new Scanner(System.in);

            String nombreArchivo = "";
            String resultadoArchivo = "";

            int opcionMenu = 0;
            int opcionArchivo = 0;

            do{

                System.out.print("1: Leer archivo votaciones \n2: Salir\n >");
                opcionMenu = sc.nextInt();
                sc.nextLine();

                if(opcionMenu > 2 || opcionMenu < 1){
                    System.out.println("Dato invalido");
                    continue;
                }

                if(opcionMenu == 1){

                    do{

                        System.out.print("Seleccione un archivo ( 1 : 2) \n >");
                        opcionArchivo = sc.nextInt();
                        sc.nextLine();

                    }while(opcionArchivo > 2 || opcionArchivo < 1);

                    if(opcionArchivo == 1){
                        nombreArchivo = "votos1.txt";
                    }
                    else if(opcionArchivo == 2){
                        nombreArchivo = "votos2.txt";
                    }

                    RUTA_ARCHIVO += nombreArchivo; 

                    resultadoArchivo = procesarArchivoVotos();

                    System.out.println(resultadoArchivo);

                    RUTA_ARCHIVO = RUTA_ARCHIVO.replace(nombreArchivo, "");
                    
                }


            }while(opcionMenu != 2);

            sc.close();

        }
        /*catch (IOException io){
            System.out.println("Error de archivos: " + io.getMessage() + "\n" + io);
        }*/
        catch (Exception e) {
            System.out.println("Error: " + e.getMessage() + "\n" + e);
        }

    }

    public static String procesarArchivoVotos(){

        try {
            
            String linea = "";
            String resumenVotos = "";

            int votoA = 0;
            int votoB = 0;
            int votoC = 0;
            int votoBlanco = 0;
            int votoNulo = 0;

            File ubicacionArchivo = new File(RUTA_ARCHIVO);
            FileReader lecturaArchivo = new FileReader(ubicacionArchivo);
            BufferedReader datosArchivo = new BufferedReader(lecturaArchivo);

            while((linea = datosArchivo.readLine()) != null){

                if (linea.trim().isEmpty()){

                    continue;

                }

                switch (linea.toLowerCase()) {
                    case "a":votoA++; break;

                    case "b":votoB++; break;

                    case "c":votoC++; break;

                    case "#":votoBlanco++; break;

                    case "?":votoNulo++; break;
                
                    default: votoNulo++; break;
                }

            }

            resumenVotos = "A:" + votoA + "\nB:" + votoB + "\nC:" + votoC + "\n#:" + votoBlanco + "\n?:" + votoNulo;

            datosArchivo.close();

            return resumenVotos;
            
        }
        catch (IOException io){
            return "Error de archivos: " + io.getMessage() + "\n" + io;
        }
        catch (Exception e) {
            return "Error: " + e.getMessage() + "\n" + e;
        }

    }

}
