def convertFrom(num, base):
    if num[-1] == '\n':
        num = num[:-1]
    x = 1
    if num[0] == "-":
        x = -1
        num = num[1:]
    power = 1
    numb = 0
    for i in reversed(num):
        numb += int(i)*power
        power *= base
    return numb*x


f = [open("dane_systemy1.txt").readlines(),
     open("dane_systemy2.txt").readlines(),
     open("dane_systemy3.txt").readlines()]

expected = [convertFrom(f[i-1][0].split(" ")[0], 2**i) for i in range(1, 4)]

err = 0

for i in range(len(f[0])):
    correct = False
    for j in range(3):
        if expected[j] == convertFrom(f[j][i].split(" ")[0], 2**(j+1)):
            correct = True
    if not correct:
        err += 1
    expected = [x+24 for x in expected]

print(err)
