#include <iostream>
#include <string>
using namespace std;

int main()
{
    string nombre = "Thomas";
    string apellido  = "Gomez";

    cout << nombre.append(apellido) << "\n"; // Asi es como se concatena 
    cout << nombre + apellido << "\n";

    // Asi podemos ver de cuanto es la longitud de una cadena
    string cadena = "abcde";
    cout << cadena.length()  << "\n";

    // Ingresar a un elemento en especifico
    cadena = "123456";
    cout << cadena[0] << "\n";

    // Asi se cambuia un indice del texto
    cadena[2] = 'A';
    cout << cadena  << "\n";

    // Asi ponemos entre comillas un texot sin confundirse con las comilla de los string
    cout << "Hola como estas este es mi numero \"104322\""  << "\n";

    // \n nueva linea
    // \t tab en la impresion

    // Asi recibes un input() solo recibe hasta encontrar un espacio
    string info;
    cin >> info;
    cout << info << "\n" ;

    string info2;
    getline (cin, info2); // De esta manera recibimos toda una linea de texto
    cout << info2;

    return 0;
}
