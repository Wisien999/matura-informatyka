#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char const *argv[])
{
    std::ifstream numbers;
    std::string number;
    int by2 = 0, by8 = 0;

    numbers.open("liczby.txt");

    if(numbers.fail())
    {
        std::cout << "Błąd" << std::endl;
        numbers.close();
        return 0;
    }

    while(!numbers.eof())
    {
        numbers >> number;
        if(number.back() == '0')
        {
            by2++;
            if(number[number.length() - 2] == '0' && number[number.length() - 3] == '0') by8++;
        }
    }
    std::cout << "Ilość liczb podzielnych przez 2: " << by2 << std::endl;
    std::cout << "Ilość liczb podzielnych przez 8: " << by8 << std::endl;

    numbers.close();
    return 0;
}
