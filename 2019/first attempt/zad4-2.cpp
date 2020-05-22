#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

int factory(int x){
    int fac = 1;
    for(int i=x;i>1;i--)
    {
		fac*=i;
    }
    return fac;
}

int main() {
    std::fstream file;
    int sum = 0;
    int number = 0;

    file.open("liczby.txt");
    for (int i = 0; i < 500; i++)
    {
        sum = 0;
        file >> number;
        std::string num = std::to_string(number);
        for (int j = 0; j < num.length(); j++)
        {
            // std::cout << num[j] << " " << factory(num.at(j)-48) << "\n";
            sum += factory(num[j]-48);
        }

        file.close();
        // std::cout << number << " " << num << std::endl;
        
        if (sum == number)
        {
            std::cout << number << std::endl;
        }
    }

    return 0;
}
