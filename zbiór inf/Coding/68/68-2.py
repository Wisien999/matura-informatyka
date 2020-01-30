ammount = 0
for line in open("dane_napisy.txt"):
    a, b = line.split()
    if sorted(a) == sorted(b):
        ammount += 1


print(ammount)
