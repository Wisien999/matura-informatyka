circles = []

for line in open("okregi.txt"):
    x, y, r = map(float, line.split())
    circles.append([x, y, r])


def is_mirror(circle1, circle2):
    if circle1[2] != circle2[2]:
        return 0
    if (circle1[0] == circle2[0] and circle1[1] == -circle2[1]):
        return 1
    if (circle1[0] == -circle2[0] and circle1[1] == circle2[1]):
        return 1
    return 0


mirr = 0
for i in range(len(circles)):
    for j in range(i):
        mirr += is_mirror(circles[i], circles[j])


print("Liczba lustrzanuch par:", mirr)
