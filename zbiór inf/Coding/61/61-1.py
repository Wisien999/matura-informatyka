def isaritmetic(seq):
    r = int(seq[1]) - int(seq[0])
    for i in range(2, len(seq)):
        if int(seq[i]) - int(seq[i-1]) != r:
            return False, r
    return True, r


# print(list(map(int, ["4", "52", "2", "345", "12"])))

f = open("ciagi.txt")
lines = f.readlines()
f.close()

maxi = 0
ammount = 0
for i in range(1, len(lines), 2):
    corr, r = isaritmetic(lines[i].split(" "))
    if corr:
        ammount += 1
        maxi = max(maxi, r)
print(ammount, maxi)
