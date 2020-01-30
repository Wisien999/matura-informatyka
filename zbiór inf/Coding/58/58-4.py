import math


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


lines = open("dane_systemy1.txt").readlines()

max_jump = 0

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        t1 = convertFrom(lines[i].split(" ")[1], 2)
        t2 = convertFrom(lines[j].split(" ")[1], 2)
        jump = math.ceil((t1-t2)*(t1-t2)/abs(i-j))
        if max_jump < jump:
            max_jump = jump
print(max_jump)
