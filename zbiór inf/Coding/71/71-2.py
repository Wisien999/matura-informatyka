def fun(mult, x):
    s = 0
    for i in range(4):
        s += mult[i]*(x**i)
    return s


parts = [list(map(float, line.split())) for line in open("funkcja.txt")]

maxi = 0
maxi_x = 0
x = 4.0

while x < 5.0:
    val = round(fun(parts[int(x)], x), 5)
    if val > maxi:
        maxi = val
        maxi_x = x
    elif val == maxi:
        print("x =", x, "\nf(x) =", val)
    x = round(x + 0.001, 3)


print("x =", maxi_x, "\nf(x) =", maxi)
