def nadzies(num):
    power = 1
    suma = 0
    for c in reversed(num):
        suma += int(c)*power
        power *= 8
    return suma


f1 = open("liczby1.txt")
lines1 = f1.readlines()
f1.close()
f2 = open("liczby2.txt")
lines2 = f2.readlines()
f2.close()

ammount = 0
for i in range(1000):
    if lines1[i][-1] == '\n':
        lines1[i] = lines1[i][:-1]
    if lines2[i][-1] == '\n':
        lines2[i] = lines2[i][:-1]
    if nadzies(lines1[i]) == int(lines2[i]):
        ammount += 1

print("a)", ammount)

ammount = 0
for i in range(1000):
    if nadzies(lines1[i]) > int(lines2[i]):
        ammount += 1
        
print("b)", ammount)
