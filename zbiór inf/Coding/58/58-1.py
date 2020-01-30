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


for i in range(1, 4):
    f = open("dane_systemy" + str(i) + ".txt")
    lines = f.readlines()

    mini = float("inf")
    for line in lines:
        num = convertFrom(line.split(" ")[1], 2**i)
        if num < mini:
            mini = num
    if bin(mini)[0] == "-":
        print("-"+bin(mini)[3:])
    else:
        print(bin(mini)[2:])

    f.close()
