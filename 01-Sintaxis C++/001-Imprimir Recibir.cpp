#include <iostream>
using namespace std;

/*
Este es un
comentario en varias
lineas
*/

int main() { // El compilador va a ejecutar todo lo que este dentro del main

    cout << "hola marte \n"; // Usamos el cout para imprimir datos numericos o letras
    cout << "hola saturno \n"; // Usamos el \n para hacer un salto de linea
    cout << 1 << "\n";

    // Usamos cin >> varible para recibir es como el "input()" de python

    string letras;

    cin >> letras;
    cout << "Las letras que ingreso son " << letras;

    return 0;
}