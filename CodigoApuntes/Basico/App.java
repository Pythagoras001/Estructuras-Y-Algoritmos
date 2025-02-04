// package Basico;

// public class App {

//     // El objetivo de este proyecto es repasar los conceptos basicos de java
//     public static void main(String[] args) {
        
//         try{

//             // Crear variables numericas enteras
//             byte varByte = 0;
//             short varPequena = 200;
//             int varEntera = 10000;
//             long varLarga = 2030000;

//             // Crear variables Decimales
//             float varFloat = 9.5f;
//             double varDouble = 0.000023;

//             // Crear variables Booleanas
//             boolean esAdulto = true;
//             boolean esNino = false;

//             // Crear textos
//             String nombreUsuario = "Thor Mondragon";
//             char letra = 'a';

//             //Conversiones Directas
//             /*
//              * Las conversiones directas es cuando un tipo de dato de mayor almacenaje desea guardar
//              * el dato de un tipo dato inferior o de menor almacenamientos
//              */
//             varLarga = varPequena;
//             varDouble = varFloat;

//             //Conversiones Indirectas
//             /*
//              * La conversion indirecta es cuando deseamos poner un valor de mayor almacenamiento en un tipo de dato
//              * de menor almacenamiento
//              */
//             varByte = /*Cast*/(byte)varEntera;
//             varPequena = (short)varLarga;

//             //Conversiones Explicitas
//             String edadUsuario_1 = "20";
//             String edadUsuario_2 = "16";

//             short edadUsuario_1Numerico;
//             int edadUsuario_2Numerico;

//             edadUsuario_1Numerico = Short.parseShort(edadUsuario_1);
//             edadUsuario_2Numerico = Integer.parseInt(edadUsuario_2);
//             //Float.parseFloat(varString)
//             //Long.parseLong(varString)
//             //Double.parseDouble(varString)
//             //Byte.parseByte(varString)

//             //Imprimir datos
//             // sout + tabular = System.out.println --> permite mostrar mensajes por consola
//             System.out.println("Hola usuario ¿Como estas?");

//             // Concatenar datos
//             String nombre = "Goku";
//             String apellido = "Vegeta";

//             String nombreCompleto = nombre + " " + apellido;
//             System.out.println("Nombre completo del usuario: " + nombreCompleto);

//         }
//         catch(Exception error){
//             System.out.println("Error: " + error);
//         }

//     }

// }
