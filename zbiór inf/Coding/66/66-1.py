def sum_digits(a, b):
    s = 0
    for d in a:
        s += int(d)
    for d in b:
        s += int(d)
    return str(s)

f = open("trojki.txt")

for line in f.readlines():
    a, b, c = line.split()
    if sum_digits(a, b) == c:
        print(line)


f.close()
