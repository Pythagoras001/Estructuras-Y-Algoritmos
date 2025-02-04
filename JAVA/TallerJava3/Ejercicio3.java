package JAVA.TallerJava3;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        

        try {
            
            // Creamos las varibles //
            Scanner scan = new Scanner(System.in);
            int selecUser = 0;
            int selecBot = 0;
            String estado = "";
            String[] options = {"Piedra", "Papel", "Tijera"};

            // Solicitamos la entrada //
            System.out.println(
                "Ingrese su jugada: \n" +
                "1 - Piedra\n"+
                "2 - Papel\n"+
                "3 - Tijera"
            );

            selecUser = Integer.parseInt(scan.nextLine());

            // Creamos la eleccion del bot //
            selecBot = (int) (Math.random()*3)+1;

            switch (selecUser) {
                case 1:
                    estado = (selecBot == 3) ? "Ganaste" : "Perdiste";
                    break;
                case 2:
                    estado = (selecBot == 1) ? "Ganaste" : "Perdiste";
                    break;
                case 3:
                    estado = (selecBot == 2) ? "Ganaste" : "Perdiste";
                    break;
                default:
                    break;
            }

            // Damos la salida //
            System.out.println(options[selecUser-1] + " VS " + options[selecBot-1]);
            System.out.println((selecUser == selecBot) ? "Empate" : estado);
            
            // Cerramos Scanner //
            scan.close();

        } catch (Exception error) {
            System.out.println("Error: " + error.getMessage());
        }
    }
    
}
