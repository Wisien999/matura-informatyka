#include <iostream>
#include <fstream>

int main()
{
    std::ifstream input;

    input.open("przyklad.txt");

    if (input.fail())
    {
        std::cout << "Err \n";
        input.close();
        return 0;
    }

    int pix[320];
    int min = 0;

    for(int j = 0; j < 200; j++)
    {
        for (int i = 0; i < 320; i++)
        {
            input >> pix[i];
        }

        for(int i = 0; i < 160; i++)
        {
            if(pix[i] != pix[319 - i])
            {
                min++;
                break;
            }
        }
    }

    std::cout << "Minimum: " << min << "\n";

    input.close();
    return 0;
}