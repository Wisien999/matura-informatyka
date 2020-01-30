#include <fstream>
#include <iostream>
#include <string>

int k = 0, ka;

int main() {
    std::ifstream input;

    input.open("dane_6_3.txt");

    if(input.fail())
    {
        std::cout << "Błąd" << std::endl;
        input.close();
        return 0;
    }
    int x = 26;
    std::string word;
    std::string code;
    while(!input.eof()){
        std::getline(input, word, ' ');
        std::getline(input, code);

        // Wyznacz prawdopodobne k
        k = (int)code[0] - (int)word[0];
        if (k < 0) k += 26;

        int i = 1;
        while(word[i] != '\0'){     // Wyznacz k dla pozostałych liter i porównaj do prawdopodobnego
            ka = (int)code[i] - (int)word[i];
            if (ka < 0) ka += 26;
            if (ka != k) {
                std::cout << word << "\n";      // Jeżeli prawdopodobne k i aktualne ka się nie zgadza to wypisz słowo
                break;
            }
            i++;
        }

        word.clear();
        code.clear();
        k = 0;
    }

    input.close();
    return 0;
}
