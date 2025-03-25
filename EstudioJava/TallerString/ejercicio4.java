
public class ejercicio4 {
    
    // Función para cifrar el mensaje
    public static String cifrar_mensaje(String mensaje, int desplazamiento) {
        StringBuilder mensajeCifrado = new StringBuilder();

        // Itera sobre cada carácter del mensaje
        for (char c : mensaje.toCharArray()) {
            // Verifica si es una letra minúscula
            if (c >= 'a' && c <= 'z') {
                char nuevaLetra = (char) ((c - 'a' + desplazamiento) % 26 + 'a');
                mensajeCifrado.append(nuevaLetra);
            } 
            // Verifica si es una letra mayúscula
            else if (c >= 'A' && c <= 'Z') {
                char nuevaLetra = (char) ((c - 'A' + desplazamiento) % 26 + 'A');
                mensajeCifrado.append(nuevaLetra);
            } 
            // Si no es una letra, lo agrega sin cambios
            else {
                mensajeCifrado.append(c);
            }
        }
        return mensajeCifrado.toString();
    }

}