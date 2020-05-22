#include <iostream>
#include <fstream>
#include <cmath>

int main()
{
    std::ifstream input;

    input.open("./dane.txt");

    if (input.fail())
    {
        std::cout << "Err \n";
        input.close();
        return 0;
    }

    int pix[200][320];
    int max = -1;

    for (int y = 0; y < 200; y++)
    {
        for (int x = 0; x < 320; x++)
        {
            input >> pix[y][x];
        }
    }
    for (int x = 0; x < 320; x++)
    {
        int ac = 1;
        for (int y = 1; y < 200; y++)
        {
            if (pix[y][x] != pix[y - 1][x])
            {
                if (ac > max)
                    max = ac;
                ac = 1;
                continue;
            }
            ac++;
        }
    }

    std::cout << "Najdłuższe: " << max << "\n";

    input.close();
    return 0;
}