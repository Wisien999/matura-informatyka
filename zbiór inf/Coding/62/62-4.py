def naos(num):
    os_num = ""
    while num >= 1:
        os_num = str(num%8) + os_num
        num = num // 8
    return os_num

f = open("liczby2.txt")
lines = f.readlines()
f.close()

ammount = 0
for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    for c in line:
        if c == '6':
            ammount += 1


print("w ósemkowym:", ammount)


ammount = 0
for line in lines:
    for c in str(naos(int(line))):
        if c == '6':
            ammount += 1


print("w dziesiętnym:", ammount)
