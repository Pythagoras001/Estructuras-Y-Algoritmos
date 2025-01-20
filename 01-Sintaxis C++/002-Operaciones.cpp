#include <iostream>
using namespace std;

int main()
{
    /* Operadores Aritmeticos */ 
    cout << 2 + 3;
    cout << 2 - 3;
    cout << 2 * 3;
    cout << 10 / 2;
    cout << 2 % 3;

    int valor = 5;
    ++valor; // Incrementa en 1
    --valor; // Incrementea en 2
    cout << valor;

    /* Operadores de asigncaion */ 

    int x = 6; // En binario: 0110
    x &= 3;    // x = x & 3 (AND bit a bit con 0011)
    // Resultado: x = 0010 (2 en decimal)

    int y = 5;
    y += 1; // Incrementa el valor de y segun el numero dado
    y -= 1;
    y *= 1;
    y /= 1;
    y %= 1;

    /* Operaciones de Comparacion */ 

    int a = 1;
    int b = 2;
    cout << (a < b);
    cout << (a <= b);
    cout << (a > b);
    cout << (a >= b);
    cout << (a == b);
    cout << (a != b);

    /* Operadores Logicos */

    a = 1;
    b = 2;
    cout << (a > b && b > 1); // Operador and
    cout << (a > b || b > 1); // Operador or 
    cout << !(a > b); // Operador not

    return 0;
}
