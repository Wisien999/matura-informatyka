import math


f = open("dane_ulamki.txt")

ammount = 0
for line in f.readlines():
    a, b = map(int, line.split())
    if math.gcd(a, b) == 1:
        ammount += 1

print(ammount)
f.close()
