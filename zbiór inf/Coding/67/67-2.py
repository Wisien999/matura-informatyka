from math import sqrt
def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(sqrt(num))+1, 2):
            if num%i == 0:
                return False
        return True

fib = [1, 1]
for i in range(38):
    fib.append(fib[-1] + fib[-2])


for elem in fib:
    if is_prime(elem):
        print(elem)
