package EstudioJava.TallerStringP2;

import java.util.Scanner;

public class ejercicio5 {

    public static void main(String[] args) {
        
        // Creamos las variables 
        Scanner scan = new Scanner(System.in);
        String info = "";
        String[] infoArr;
        char[] caracteres;

        // Solicitamos la entrada
        System.out.println("Ingrese la informacion: ");
        info = scan.nextLine();

        // Procesamos la entrada
        infoArr = info.split("-");
        for (int i = 0 ; i < infoArr.length ; i++ ) infoArr[i] = infoArr[i].trim();

        // Remplazamos 
        caracteres = infoArr[0].toCharArray();

        for (int i = 0; i < infoArr[0].length(); i++) {
            int posicion = (infoArr[1].charAt(i)) - '0';
            caracteres[posicion] = infoArr[0].charAt(i);
        }
        
        // Damos la salida
        System.out.println(String.valueOf(caracteres));

        // Cerramos Scanner
        scan.close();

    }
}