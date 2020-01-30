def fun(mult, x):
    s = 0
    for i in range(4):
        s += mult[i]*(x**i)
    return s


parts = [list(map(float, line.split())) for line in open("funkcja.txt")]

x = 0.0

while x < 5.0:
    val = round(fun(parts[int(x)], x), 5)
    if abs(val) <= 0.00001:
        print(x)
    x = round(x + 0.00001, 5)
