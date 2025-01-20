#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    // Asi es como creamos una matriz con varios valores y como podemos acceder a ellos
    string nombres[3] = {"Pepe", "Juan", "Pedro"};
    cout << nombres[0] << "\n";

    // Asi es como un for itera en la lista
    for (string i : nombres)
    {
        cout << i<< "\n";

    }

    // Asi se pueden meter elementos en la matriz
    string cars[5]; //Se debe dejar asi al declarar la matriz
    cars[0] = "Volvo";
    cars[1] = "BMW";
    cars[2] = "Ford";
    cars[3] = "Mazda";
    cars[4] = "Tesla";

    for (string i : cars)
    {
        cout << i << "\n";

    }

    // Para ver el tama;o de la matriz usamos la fucion sizeof()
    // Esta da el tama;o en bits por tanto tenemos que dividirlo por el peso en bits de tipo de dato

    int myNumbers[5] = {10, 20, 30, 40, 50};
    cout << sizeof(myNumbers) << "\n";
    cout << sizeof(myNumbers) / sizeof(myNumbers[0]);
    
    
    return 0;
}
