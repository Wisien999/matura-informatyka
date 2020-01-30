def jednolity(a):
    if a.count(a[0]) == len(a):
        return True
    return False


ammount = 0
for line in open("dane_napisy.txt"):
    a, b = line.split()
    if jednolity(a) and a == b:
        ammount += 1


print(ammount)
