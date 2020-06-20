import math

def sumOfDigits(num):
    s = 0
    for c in num:
        s += math.factorial(int(c))

    return s

        
with open("liczby.txt") as f:
    for line in f.read().splitlines():
        num = int(line)
        if num == sumOfDigits(line):
            print(num)

