import java.util.Random;

public class Parcial {
    public static void main(String[] args) {

        // Creamos las varibles //
        int potreto_1 = rand.nextInt(50 - 20 + 1) + 20;
        int potreto_2 = rand.nextInt(50 - 20 + 1) + 20;
        int potreto_3 = rand.nextInt(50 - 20 + 1) + 20;
        
        int origen = 0;
        int destino = 0;

        int cantOrigen = 0;
        int cantDestino = 0;
        
        int iteraciones = 100;
        int transporte = 0;
        boolean valido = false;

        for (int i = 0; i < iteraciones; i++) {
        
            // Definimos origen-destino //
            origen = rand.nextInt(3)+1;
            destino = calcularDestino(origen);
            
            // Asignamos cantidades //
            switch (origen) {
                case 1:
                    cantOrigen = potreto_1;
                    cantDestino = (destino == 2)? potreto_2 : potreto_3;
                    break;
                case 2:
                    cantOrigen = potreto_2;
                    cantDestino = (destino == 1)? potreto_1 : potreto_3;
                    break;
                case 3:
                    cantOrigen = potreto_3;
                    cantDestino = (destino == 1)? potreto_1 : potreto_2;
                    break;
            }

            // Definimos la cantidad a transportar //
            transporte = autorizarTransporte(origen, destino, potreto_1, potreto_2, potreto_3, cantOrigen, cantDestino);

            // Validamos si es posible hacer el transporte //
            valido = transporte > 0;

            // Damos la salida //
            System.out.println("============="+ (valido  ? "A U T O R I Z A D O":"R E C H A Z A D O" ) + "=============");
            System.out.println("Movimiemto #"+i);
            System.out.println("-Potrero Origen = P-"+origen);
            System.out.println("-Cantidad de vacas = V-"+cantOrigen);
            System.out.println("-Potrero Destino = P-"+destino);
            System.out.println("-Cantidad de vacas = V-"+cantDestino);

            // Acabamos el proceso si no esta autorizado //
            if (!valido) continue;

            // Imprimimos la cantidad de vacas a mover //
            for (int j = 0; j < transporte; j++) {
                System.out.print("Y");
                if (j == 0) {
                    System.out.print("Potreno #" + origen);
                }else if(j == transporte-1){
                    System.out.println("Potreno #" + destino);
                }
            }

            // Realizamos el transporte //
            switch (origen) {
                case 1:
                    potreto_1 -= transporte;
                    if (destino == 2) potreto_2 += transporte;
                    else potreto_3 += transporte;
                    break;
                case 2:
                    potreto_2 -= transporte;
                    if (destino == 1) potreto_1 += transporte;
                    else potreto_3 += transporte;
                    break;
                case 3:
                    potreto_3 -= transporte;
                    if (destino == 1) potreto_1 += transporte;
                    else potreto_2 += transporte;
                    break;
            }
            
        }

    }
    
    // ##################### Funciones ##################### //

    // CREAMOS UNA FUNCION PARA CALCULAR EL DESTINO //
    public static int calcularDestino(int origen){
        int destino = 0;
        do {
            destino = rand.nextInt(3)+1;    
        } while (destino == origen);

        return destino;
    }

    // CREAMOS UNA FUNCION PARA CALCULAR EL TRANSPORTE CANTIDAD-SI ES POSIBLE //
    public static int autorizarTransporte(int origen, int destino, int p1, int p2, int p3, int cantOrigen, int cantDestino){
        int transporte = rand.nextInt(25-15+1)+15;
        int limite = 100;

        if ((transporte > cantOrigen) || ((transporte + cantDestino) > limite)) {
            return -1;
        }else{
            return transporte;
        }
    }


    // METEMOS COLORES Y CREAMOS UN STATICO PARA RAMDOM //
    public static Random rand = new Random();
    public static final String BLUE = "\u001B[34m";
    public static final String PURPURA = "\u001B[35m";
    public static final String NARANJA = "\u001B[33m";
    public static final String RESET = "\u001B[0m";
    
}
