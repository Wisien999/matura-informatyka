f = open("dane_ulamki.txt")

max_b = 4*9*25*49*13
suma = 0
for line in f.readlines():
    a, b = map(int, line.split())
    q = max_b // b
    suma += a*q

print(suma)
f.close()
