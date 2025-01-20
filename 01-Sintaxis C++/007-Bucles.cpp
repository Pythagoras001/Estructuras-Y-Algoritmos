#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{

    // Asi es como implementamos un while 
    int i = 1;
    while (i <= 10)
    {
        cout << i << "\n";
        i++;
    }

    // Existe una variante que es el do while se ejecuta siempre por lo menos 1 vez
    // Aunque la condicion del while sea falsa
    int a = 3;
    do
    {
        cout << a << "\n";
        a--;
    } while (a > 5);

    // Asi es como se implementa un for
    // (Donde empieza, donde termina, cuando avanza)

    for (int i = 0; i < 10; i++)
    {
        cout << i << "\n";
    }

    // Asi recorremos una lista
    int nums[5] = {1,2,3,4,5};
    for (int i: nums)
    {
        cout << i << "\n";
    }
     
    
    
    
    return 0;
}
