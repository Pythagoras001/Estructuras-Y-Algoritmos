public class patron {

    public static void main(String[] args) {
        
        // Creamos las variables 
        int total = 21;
        int mitad = (total / 2) + 1;
        int anterior = 0;

        String[] historial = new String[((Integer)total/2) + 1];
        historial[0] = String.valueOf(mitad);

        // COnstruimos el patron
        constructor(historial, mitad, 1);

        // Espaciamos el inicio de cada fila 
        for (int i = historial.length - 1, h = 0; i > -1 && h <= mitad; i--, h ++) {

            for (int j = 0; j < anterior; j++){
                historial[i] = " " + historial[i];
            }
            anterior += String.valueOf(h+1).length();
        }

        // Damos la salido
        for (int i = historial.length-1 ; i > 0; i--) System.out.println(historial[i]);

        for (String string : historial) {
            System.out.println(string);
        }
    }

    // Creamos una funcion para construir el patron
    public static String[] constructor(String[] hist, int num, int index){
        String p1 = String.valueOf(num-1);
        String p2 = "";
        String p3 = String.valueOf(num+1 + ((index-1)*2));

        for (int i = 0; i < hist[index-1].length(); i++) {
            p2 += " ";
        }

        hist[index] = p1+p2+p3;

        if (num-1 != 1) constructor(hist, num-1, index+1);

        return hist;
    }
}