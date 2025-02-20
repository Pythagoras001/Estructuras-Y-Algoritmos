package EstudioJava.TallerJava3;

public class Ejercicio4 {
    
    public static void main(String[] args) {
        
        try {
            
            double x = 0;
            int  b = 0;
            int  a = 0;
            int  c = 0;
        
            // Expresion A //
            x = (-b + Math.pow((b * b - (4 * a * c)),0.5)) / (2 * a);

            // Expresion B //
            x = ((3*a + 4*b) / (5 + c)) + ((8*c - 10) / (3*a + b));

            System.out.println(x);

        } catch (Exception error) {
            System.out.println("Error: " + error.getMessage());
        }
    }
}