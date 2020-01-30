from math import sqrt


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

f = open("trojki.txt")

for line in f.readlines():
    a, b, c = line.split()
    if is_prime(int(a)) and is_prime(int(b)) and int(c)==int(a)*int(b):
        print(line)


f.close()
