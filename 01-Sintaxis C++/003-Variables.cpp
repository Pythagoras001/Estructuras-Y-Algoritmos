#include <iostream>
using namespace std;

int main()
{

    // type variableName = value;
    // Asignamos el tipo de variable luego el nombre y por ultimo el valor

    int numeroEntero = 10;
    double numeroDecimal = 19.0;
    string texto = "hola";
    bool verdaderoFalso = true; // Los booleanos sacan 1 en caso de ser verdadero y 0 si es false 
    char caracter = 'a';

    cout << verdaderoFalso << endl;

    // Asi juntamos variables con texto

    cout << "Yo tengo el numero " << numeroEntero << " en mi notebook" << "\n";

    // Podemos asignarle el valor a varias variables el mismo tiempo 

    int x, y, z;
    x = 12;
    y = 23;
    z = 0;

    cout << x + z + y;

    return 0;

    // Como asignar una constante de este modo esta variable no se puede cambiar
    // Modificar este numero daria error en al compilar

    const int numeroConstante = 0;
    
}


