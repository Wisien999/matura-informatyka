import math

file = open("liczby.txt", "r")

numbers = file.readlines()

maxleng, maxGCD, firstNumber = 0, 0, 0

for i in range(len(numbers)):
    number = int(numbers[i])
    gcd = int(numbers[i])
    leng = 1
    for j in range((i+1), 500):
        if math.gcd(gcd, int(numbers[j])) > 1:
            leng += 1
            gcd = math.gcd(gcd, int(numbers[j]))
        else:
            break
    if leng > maxleng:
        maxleng = leng
        maxGCD = gcd
        firstNumber = numbers[i]

print("Pierwsza liczba ciągu:", firstNumber)
print("Długość ciągu:", maxleng)
print("Największy Wspólny Dzielnik:", maxGCD)
