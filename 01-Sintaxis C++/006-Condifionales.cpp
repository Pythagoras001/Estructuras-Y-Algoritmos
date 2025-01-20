#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    // Asi son los condicionales
    if (20 > 10)
    {
        cout << "20 es menor que 10";

    } else if (2 < 1)
    {
        cout << "Puede que si sea verdad";

    }else
    {
        cout << "No es cierto";

    }
    
    // Se puede abreviar con el siguiente formato en una solo linea
    // variable = (condition) ? expressionTrue : expressionFalse;

    int time = 20;
    string result = (time < 18) ? "Good day." : "Good evening.";
    cout << result;

    // Si hay muchos elif se puede usar ell swicht

    int day = 4;
    switch (day) {
    case 6:
        cout << "Today is Saturday";
        break;
    case 7:
        cout << "Today is Sunday";
        break;
    default:
        cout << "Looking forward to the Weekend";
    }
        
    return 0;
}
