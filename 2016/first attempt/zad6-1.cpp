#include <fstream>
#include <iostream>

// char signs[] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'G', 'H', 'I', 'J', 'K'};

int k = 107;

int main() {
    std::ifstream input;

    input.open("dane_6_1.txt");

    if(input.fail())
    {
        std::cout << "Błąd" << std::endl;
        input.close();
        return 0;
    }
    int x = 90 - 64;
    char word[30];
    k = k % x;
    std::cout << k << "\n";
    while(!input.eof()){
        input >> word;
        std::cout << word << "\n";
        int i = 0;
        while(word[i] != (char)0){
            word[i] = (int)word[i] + k;
            if((int)word[i] > 90) word[i] = (int)word[i] - x;
            i++;
        }
        i = 0;

        std::cout << word << "\n";

        while(word[i] != (char)0){
            word[i] = '\0';
            i++;
        }

    }

    input.close();
    return 0;
}
