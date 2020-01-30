import math


f = open("dane_ulamki.txt")

suma = 0
for line in f.readlines():
    a, b = map(int, line.split())
    suma += a // math.gcd(a, b)

print(suma)
f.close()
