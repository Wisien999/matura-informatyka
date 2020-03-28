f = open("dane_trojkaty.txt")
lines = list(map(int, f.readlines()))
f.close()

notmatching = 0

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(j+1, len(lines)):
            a, b, c = lines[i], lines[j], lines[k]
            if a == max(a, b, c):
                if b + c > a:
                    notmatching += 1
            if b == max(a, b, c):
                if a + c > b:
                    notmatching += 1
            if c == max(a, b, c):
                if b + a > c:
                    notmatching += 1

print(notmatching)
