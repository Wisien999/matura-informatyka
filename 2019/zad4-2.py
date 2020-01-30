import math

file = open("liczby.txt", "r")

numbers = file.readlines()
for number in numbers:
    # print(number)
    s = 0
    for char in number[:-1]:
        s += math.factorial(int(char))
        # print(s)
    if s == int(number):
        print(s)
