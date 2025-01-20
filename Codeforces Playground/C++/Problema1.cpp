#include <iostream>
using namespace std;

int main()
{
    int cant; cin >> cant;

    for (int _ = 0; _ < cant; _++)
    {   
        int dias; cin >> dias;
        int suma = 0;
        int c = 0;

        for (int i = 0; i < dias; i++)
        {
            int num; cin >> num;
            suma += num;

            for (int n = 1; n <= suma; n+=2)
            {
                int poten = n*n;
                if (poten == suma)
                {
                    c += 1;
                } else if (poten > suma)
                {
                    break;
                }
            }
        }
        cout << c << "\n";
    }
    return 0;
}
