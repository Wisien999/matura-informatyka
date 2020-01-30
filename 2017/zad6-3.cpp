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
    int con = 0;

    for (int i = 0; i < 200; i++)
    {
        for (int j = 0; j < 320; j++)
        {
            input >> pix[i][j];
        }
    }

    for (int i = 0; i < 200; i++)
    {
        for (int j = 0; j < 320; j++)
        {
            if (i > 0 && (std::abs(pix[i - 1][j] - pix[i][j]) > 128))
            {
                con++;
                continue;
            }
            if (i < 199 && (std::abs(pix[i + 1][j] - pix[i][j]) > 128))
            {
                con++;
                continue;
            }
            if (j > 0 && (std::abs(pix[i][j - 1] - pix[i][j]) > 128))
            {
                con++;
                continue;
            }
            if (j < 319 && (std::abs(pix[i][j + 1] - pix[i][j]) > 128))
            {
                con++;
                continue;
            }
        }
    }

    std::cout << "Kontrastujące sąsiednie: " << con << "\n";

    input.close();
    return 0;
}