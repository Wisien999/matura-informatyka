f = open("dane_ulamki.txt")


mini_a = 12000
mini_b = 1
for line in f.readlines():
    a, b = map(int, line.split())
    x = mini_a
    y = mini_b
    ac, bc = a, b
    if y != b:
        x, ac = x * bc, ac * y
    if ac < x:
        mini_a = a
        mini_b = b
    elif ac == x:
        if b < mini_b:
            mini_a = a
            mini_b = b

print(mini_a, mini_b)

f.close()
