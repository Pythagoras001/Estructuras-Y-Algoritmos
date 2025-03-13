import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        
        // Creamos las varibles 
        Scanner scan = new Scanner(System.in);

        String cadenaSig = "";
        String[] signos;

        String cadeGrupo = "";
        String[] grupos;

        // Solicitamos la entrada 

        System.out.println("Ingrese los signos a identificar");
        cadenaSig = scan.nextLine();
        signos = cadenaSig.split("-");

        System.out.println("Ingrese los grupos");
        cadeGrupo = scan.nextLine();
        grupos = cadeGrupo.split("-");

        // Procesamos ? - ! - .
        System.out.println(grupos[0].trim() + "->" + simboloMayor(grupos[0], signos));
        System.out.println(grupos[1].trim() + "->" + simboloMayor(grupos[1], signos));

    }

    public static String simboloMayor(String grupo, String[] simbolos){

        String simMax = "";
        int maxRepet = 0;
        int contador = 0;

        for (String sim : simbolos){
            contador = 0;

            for (String ind : grupo.split(" ")) {
                if(ind.equals(sim.trim())) contador ++;
            }

            if (contador > maxRepet){
                maxRepet = contador;
                simMax = sim.trim();
            }

        }

        return simMax;
    }
}
