f = open("dane_trojkaty.txt")
lines = list(map(int, f.readlines()))
f.close()

for i in range(2, len(lines)):
    maxi = max(lines[i-2], lines[i-1], lines[i])
    sides = []
    for j in range(3):
        if maxi != lines[i-j]:
            sides.append(lines[i-j])
    if sides[0]**2 + sides[1]**2 == maxi**2:
        print(sides[0], sides[1], maxi)
    sides.clear()
