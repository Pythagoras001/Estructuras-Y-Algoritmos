import java.io.*;
import java.util.Scanner;

public class baccarat {
    public static String RUTA = "Recursos";

    public static void main(String[] args) {
        
        // Creamos las variables
        Scanner scan = new Scanner(System.in);

        int opcion = 0;
        int numJuegos = 0;

        String nameFile = "";
        String namesRegis = "";

        String nameSelect = "";
        String entrada = "";
        
        while (opcion != 3) {
            // Solicitamos la entrada

            do {
                System.out.print("1|Registrar Mazo\n2|Jugar Mazo\n3|Salir\nSeleccion -> ");
                entrada = scan.nextLine().trim();
            } while (!entrada.matches("[1-3]") || (entrada.equals("2") && namesRegis.length() <= 0));
            opcion = Integer.parseInt(entrada);
      
            if (opcion == 1){

                do {
                    System.out.print("Ingrese el nombre del mazo: ");
                    nameFile = scan.nextLine().trim();
                } while (nameFile.isEmpty());

                namesRegis += "+ " + nameFile + "\n";

                do {
                    System.out.print("Ingrese la cantidad de juegos del mazo: ");
                    entrada = scan.nextLine().trim();
                } while (!entrada.matches("\\d+"));
                numJuegos = Integer.parseInt(entrada);

                crearMazo(numJuegos, nameFile);

            }else{

                do {
                    System.out.print("Ingrese El Maso que desea jugar: \n" + namesRegis);
                    nameSelect = scan.nextLine().trim();

                    for (String creados : namesRegis.split("\\+")){
                        if (nameSelect.equals(creados.trim())){
                            entrada = "true";
                            break;
                        }
                    }
                    
                } while (!entrada.equals("true"));
                
                System.out.println(evaluarMazo(nameFile));
            }

            System.out.print("\n");
        }
        // Cerramos Archivos
            scan.close();
    }

    // Creamos una funcion que nos cree un mazo 
    public static void crearMazo(int numJuegos, String nameFile){
        try {

            FileWriter archivo = new FileWriter(RUTA + "/" + nameFile + ".txt", true);
            PrintWriter escribir = new PrintWriter(archivo);

            int totalCards = 4;
            String lineText = "";

            for (int i = 0; i < numJuegos; i++) {
                for (int j = 0; j < totalCards; j++) {
                    if (totalCards / 2 == j) lineText += " |";
                    lineText += " " + ((int)(Math.random() * 13) + 1);
                }

                escribir.println(lineText.trim());
                lineText = "";
            }

            escribir.close();
            
        } catch (IOException e) {
        }
    }

    // Creamos una funcion que leera el archivo y escriba los resultados
    public static String evaluarMazo(String nameFile){
        try {

            // Abrimos el archivo para leer
            File ubicacion = new File(RUTA + "\\" + nameFile + ".txt");
            FileReader leerArchivo = new FileReader(ubicacion);
            BufferedReader archivoMemoria = new BufferedReader(leerArchivo);

            // Escribimos archivo para poner los resultados
            FileWriter resultMazo = new FileWriter(RUTA + "/" + "0_Resultado.txt", false);
            PrintWriter escirbir = new PrintWriter(resultMazo);

            // Cremos las variables
            String lineText = "";
            String[] cartas;

            String pareja = "";
            int numCard = 0;

            int puntJugador = 0; 
            int puntCasa = 0; 
            String ganador = " Empate";

            String registro = "";
            
            while ((lineText = archivoMemoria.readLine()) != null) {

                // Calculamos las puntuaciones totales del jugador y de la casa
                cartas = lineText.split("\\|");

                for (int i = 0; i < 2; i++) {
                    pareja = cartas[i].trim();

                    for (String carta : pareja.split(" ")) {
                        numCard = Integer.parseInt(carta);

                        if (numCard >= 10) continue;
                        else if (i == 0) puntJugador += numCard;
                        else puntCasa += numCard;
                    }
                }

                puntJugador %= 10;
                puntCasa %= 10;

                // Escribimos las putuaciones totales y los ganadores
                if (puntJugador > puntCasa) ganador = " Ganaste";
                else if (puntJugador < puntCasa) ganador = " Perdiste";

                registro += puntJugador + " | " + puntCasa + ganador + "\n";
                escirbir.println(puntJugador + " | " + puntCasa + ganador);

                puntJugador = 0;
                puntCasa = 0;
            }

            // Cerramos los archivos de escirtura y texto
            escirbir.close();
            archivoMemoria.close();

            return registro;
            
        } catch (IOException e){
            return "Error";
        }
        
    }

}