import math


def is_prime(x):
    if x == 2:
        return True
    elif x < 2:
        return False
    elif x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 2, 2):
        if x % i == 0:
            return False
    return True


def to_decimal(seq):
    s = 0
    power = 1
    for c in reversed(seq):
        s += power*int(c)
        power *= 2
    return s


def is_halfprime(seq):
    if seq[-1] == '\n':
        seq = seq[:-1]
    num = to_decimal(seq)
    for i in range(2, num):
        if num % i == 0:
            b = num // i
            if is_prime(i) and is_prime(b):
                return True, num
    return False, num


f = open("ciagi.txt")
ammount = 0
maxi, mini = 0, float("inf")
for line in f.readlines():
    is_h, num = is_halfprime(line)
    if is_h:
        ammount += 1
        maxi = max(maxi, num)
        mini = min(mini, num)

print(ammount, "\nMax:", maxi, "\nMin:", mini)
