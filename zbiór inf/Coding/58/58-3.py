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

# f = [["1 1", "1 10", "1 1", "1 0", "1 1"],
#      ["1 0", "1 1", "1 -1", "1 -2", "1 2"],
#      ["1 -1", "1 -1", "1 -1", "1 0", "1 1"]]

maximum = [float("-inf"), float("-inf"), float("-inf")]

max_day = 0

for i in range(len(f[0])):
    new_max = False
    for j in range(3):
        curr = convertFrom(f[j][i].split(" ")[1], 2**(j+1))
        # print("Curr:", curr, "max for j=", j, maximum[j])
        if maximum[j] < curr:
            maximum[j] = curr
            new_max = True
            # print("true")
    if new_max:
        max_day += 1
        # print("added")
print(max_day)
