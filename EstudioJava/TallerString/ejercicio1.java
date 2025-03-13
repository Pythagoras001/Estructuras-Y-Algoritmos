import java.util.Scanner;

public class ejercicio1 {

    public static String CONSTANTE = "HOLA";

    public static void main(String[] args) {

        // Creamos las varibles 
        Scanner scan = new Scanner(System.in);
        String estados = "";
        String[] partidos;

        int e1 = 0;
        int e2 = 0;

        // Solicitamos la entrda 
        System.out.println("Ingrese el resultado del partido");
        estados = scan.nextLine();
        partidos = estados.split("-");

        for (int i = 0; i < 2; i++) {
            e1 = e2 = 0;

            for (String gol : partidos[i].split(",")) {
                if(gol.trim().equals("equipo 1")) e1++;
                else e2 ++;
                
            }
            if (e2 < e1) System.out.println("Equipo 1 Gano");
            else if (e1 < e1) System.out.println("Equipo 2 Gano");
            else System.out.println("Empate");;
        
        }
        // Cerramos Scanner
        scan.close();

    }
}