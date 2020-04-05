def firstQuartet(xy):
    for a in xy:
        if a <= 0:
            return False
    return True


count = 0
for line in open("wspolrzedne.txt"):
    xy = list(map(int, line.split()))
    if firstQuartet(xy):
        count += 1

print(count)
