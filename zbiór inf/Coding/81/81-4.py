def czyProstokatny(points):
    AB = ((points[1][0]-points[0][0])**2 + (points[1][1]-points[0][1])**2)
    AC = ((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)
    BC = ((points[2][0]-points[1][0])**2 + (points[2][1]-points[1][1])**2)
    return AB + AC == BC or AB + BC == AC or BC + AC == AB


count = 0
for line in open("wspolrzedneTR.txt"):
    xy = list(map(int, line.split()))
    points = []
    for i in range(0, len(xy), 2):
        points.append([xy[i], xy[i+1]])

    if czyProstokatny(points):
        count += 1

print("Ile prostokątnych:", count)
