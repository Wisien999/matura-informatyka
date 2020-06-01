def divisable(num):
    if num[-1] == "\n":
        num = num[:-1]
    if num[-1] == '1':
        return 0, 0
    
    if num[-2] == '1' or num[-3] == '1':
        return 1, 0
    return 1, 1

with open("liczby.txt") as file:
    by2, by8 = 0, 0
    for line in file:
        x = divisable(line)
        by2 += x[0]
        by8 += x[1]

print("Przez 2:", by2)
print("Przez 8:", by8)
