def count(num, deep=1):
    il = 1
    for c in str(num):
        il *= int(c)
    if il < 10:
        return deep
    return count(il, deep+1)


f = open("liczby.txt")
ammount = [0, 0, 0, 0, 0, 0, 0, 0]
mini = float("inf")
maxi = 0
for i in range(1000):
    string = f.readline()
    if string[-1] == '\n':
        string = string[:-1]
    num = int(string)
    power = count(num)
    if power >= 0 and power < 9:
        ammount[power-1] += 1
    if power == 1:
        maxi = max(maxi, num)
        mini = min(mini, num)


print(ammount, "\nMin:", mini, "\nMax:", maxi)
f.close()
