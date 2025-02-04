package JAVA.TallerJava1;


import java.util.Locale;
import java.util.Scanner;

public class Ejercicio10 {

    public static final String BLUE = "\u001B[34m";
    public static final String PURPURA = "\u001B[35m";
    public static final String NARANJA = "\u001B[33m";
    public static final String RESET = "\u001B[0m";

    public static void main(String[] args) {

        try{

            Scanner scan = new Scanner(System.in);
            scan.useLocale(Locale.US);

            float restPorcent = 1f;
            float restNote = 3f;
            float notaNecesaria = 0f;

            for (int i = 1; i < 5; i++) {
                System.out.println(PURPURA + "Ingrese la nota y porcentaje NOTA-PORCENTAJE: " + RESET);
                String[] nota = scan.nextLine().split("-");

                restPorcent -= Float.parseFloat(nota[1]) / 100;
                restNote -= Float.parseFloat(nota[0]) * (Float.parseFloat(nota[1]) / 100);

            }

            notaNecesaria = restNote/restPorcent;

            if (notaNecesaria > 5) {
                System.err.println(NARANJA + "Tiene mas futuro la semanama pasada que esta meteria, parse llorela..." + RESET);

            } else {
                System.err.println(BLUE + "La nota necesaria para ganar es: " + String.format("%.1f", notaNecesaria) + RESET);
                
            }

            scan.close();

        } catch(Exception error){
            System.err.println(error);

        }
    }
}
