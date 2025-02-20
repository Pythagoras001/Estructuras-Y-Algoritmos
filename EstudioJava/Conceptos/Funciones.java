package EstudioJava.Conceptos;

public class Funciones {
    
    // Método sin parámetros ni retorno
    public void saludar() {
        System.out.println("¡Hola, mundo!");
    }

    // Método con parámetros
    public int sumar(int a, int b) {
        return a + b;
    }

    // Método estático (se puede llamar sin instanciar la clase)
    public static void mostrarMensaje(String mensaje) {
        System.out.println(mensaje);
    }

    public static void main(String[] args) {
        // Crear un objeto de la clase para usar métodos no estáticos
        Funciones objeto = new Funciones();
        objeto.saludar();

        int resultado = objeto.sumar(5, 3);
        System.out.println("La suma es: " + resultado);

        // Llamar a un método estático directamente
        mostrarMensaje("Este es un mensaje.");
    }
}
