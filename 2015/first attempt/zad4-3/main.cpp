#include <iostream>
#include <fstream>
#include <string>

int comp(std::string a, std::string b)
{
    if(a.length() < b.length()) return -1;
    else if(a.length() > b.length()) return 1;
    else {
        for(int i = 0; i < a.length(); i++)
        {
            if(a[i] < b[i]) return -1;
            else if(a[i] > b[i]) return 1;
        }
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    std::ifstream numbers;
    std::string number;
    std::string minNumber;
    std::string maxNumber;
    int minLine = 0, maxLine = 0, line = 0;

    numbers.open("liczby.txt");

    if(numbers.fail())
    {
        std::cout << "Błąd" << std::endl;
        numbers.close();
        return 0;
    }

    while(!numbers.eof())
    {
        line++;
        numbers >> number;
        if(minLine == 0 && maxLine == 0)
        {
            minLine = line;
            maxLine = line;
            minNumber = number;
            maxNumber = number;
        }
        else if(comp(number, minNumber) == -1)
        {
            minNumber = number;
            minLine = line;
        }
        else if(comp(number, maxNumber) == 1)
        {
            maxNumber = number;
            maxLine = line;
        }
    }
    std::cout << "Numer wiersza z najmniejszą liczbę: " << minLine << std::endl;
    std::cout << "Numer wiersza z największą liczbę: " << maxLine << std::endl;

    numbers.close();
    return 0;
}
