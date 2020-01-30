#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

int GCD(int a, int b)
{
    int pom;

    while (b != 0)
    {
        pom = b;
        b = a % b;
        a = pom;
    }

    return a;
}

int main()
{
    std::fstream file;
    int leng = 1;
    int numbers[500];
    int _leng = 0, _gcd, _firstNumber;

    file.open("liczby.txt");
    for (int i = 0; i < 500; i++)
        file >> numbers[i];

    for (int i = 0; i < 500; i++)
    {
        leng = 1;
        int gcd = numbers[i];
        for (int j = i + 1; j < 500; j++)
        {
            if (GCD(gcd, numbers[j]) > 1)
            {
                gcd = GCD(gcd, numbers[j]);
                leng++;
            }
            else
            {
                break;
            }
        }
        if (leng > _leng)
        {
            _leng = leng;
            _gcd = gcd;
            _firstNumber = numbers[i];
        }
    }

    std::cout << _firstNumber << " (pierwsza liczba ciągu) " << _leng << " (długość ciągu) ";
    std::cout << _gcd << " (największy wspólny dzielnik) " << std::endl;

    file.close();

    return 0;
}
