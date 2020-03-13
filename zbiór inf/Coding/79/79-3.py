circles = []

for line in open("okregi.txt"):
    x, y, r = map(float, line.split())
    circles.append([x, y, r])


def is_perpendicular_pair(circle1, circle2):
    if circle1[2] != circle2[2]:
        return 0
    nx1 = -circle1[1]
    ny1 = circle1[0]
    nx2 = -circle2[1]
    ny2 = circle2[0]
    # rotation 90 degree translates A(a, b) to B(-b, a)
    if nx1 == circle2[0] and ny1 == circle2[1]:
        return 1
    if nx2 == circle1[0] and ny2 == circle1[1]:
        return 1
    return 0


mirr = 0
for i in range(len(circles)):
    for j in range(i):
        mirr += is_perpendicular_pair(circles[i], circles[j])


print("Liczba prostopadłych par:", mirr)
