#include <fstream>
#include <iostream>
#include <string>

// char signs[] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'G', 'H', 'I', 'J', 'K'};
int k = 0;

int main() {
    std::ifstream input;

    input.open("dane_6_2.txt");

    if(input.fail())
    {
        std::cout << "Błąd" << std::endl;
        input.close();
        return 0;
    }
    int x = 90 - 64;
    std::string word;
    std::string kChar;
    std::cout << k << "\n";
    while(!input.eof()){
        std::getline(input, word, ' ');
        std::getline(input, kChar);

        k = atoi(kChar.c_str()) % x;

        std::cout << word << "\n" << kChar << "\n";
        int i = 0;
        while(word[i] != '\0'){
            word[i] = (char)((int)word[i] - k);
            if((int)word[i] < 65) word[i] = (char)((int)word[i] + x);
            i++;
        }

        std::cout << word << "\n";
        word.clear();
        kChar.clear();
    }

    input.close();
    return 0;
}
