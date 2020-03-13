def fit_in(x, y, r):
    if abs(x) > r and abs(y) > r:
        if x > 0 and y > 0:
            return 0
        if x < 0 and y > 0:
            return 1
        if x < 0 and y < 0:
            return 2
        if x > 0 and y < 0:
            return 3
    else:
        return 4


quarts = [0, 0, 0, 0, 0]

for line in open("okregi.txt"):
    x, y, r = map(float, line.split())
    index = fit_in(x, y, r)
    quarts[index] += 1

print("Ćwiartka I:", quarts[0])
print("Ćwiartka II:", quarts[1])
print("Ćwiartka III:", quarts[2])
print("Ćwiartka IV:", quarts[3])
print("Nie mieszczą się:", quarts[4])
