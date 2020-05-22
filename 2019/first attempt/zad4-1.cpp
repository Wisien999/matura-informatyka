#include <iostream>
#include <fstream>

int main() {
    std::fstream file;
    int ile = 0;
    int number = 0;

    file.open("liczby.txt");
    for (int i = 0; i < 500; i++)
    {
        file >> number;
        while (number % 3 == 0)
        {
            number /= 3;

        }
        if (number == 1)
        {
            ile++;
        }

    }

    file.close();
    std::cout << ile << std::endl;


    return 0;
}
