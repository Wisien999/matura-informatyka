def count(num):
    zeros = 0
    ones = 0
    for c in num:
        if c == '0':
            zeros += 1
        elif c =='1':
            ones += 1
    return zeros, ones

with open("liczby.txt") as file:
    counter = 0
    for line in file:
        zeros, ones = count(line)
        if zeros > ones:
            counter += 1

    print(counter)
