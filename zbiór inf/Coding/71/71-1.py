def fun(mult, x):
    s = 0
    for i in range(4):
        s += mult[i]*(x**i)
    return s


parts = [list(map(float, line.split())) for line in open("funkcja.txt")]

x = 1.5

print(round(fun(parts[int(x)], x), 5))
