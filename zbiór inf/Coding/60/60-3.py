import math


f = open("liczby.txt")
lines = f.readlines()

maxi = 0
for i in range(200):
    wzp = True
    for j in range(200):
        if i != j:
            if math.gcd(int(lines[i]), int(lines[j])) != 1:
                wzp = False
                break
    if wzp and int(lines[i]) > maxi:
        maxi = int(lines[i])

print(maxi)

f.close()
