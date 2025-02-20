package EstudioJava.TallerJava4;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        try {

            for (int i = 1; i <= 100 ; i++) {
                System.out.print(i);

                if(i<100){
                System.out.print("-");
                }
            }
            
        } catch (Exception e) {
            System.out.println("Error" + e.getMessage());
        }


    }
}