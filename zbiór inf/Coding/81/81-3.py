def L(points):
    AB = ((points[1][0]-points[0][0])**2 + (points[1][1]-points[0][1])**2)**(0.5)
    AC = ((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)**(0.5)
    BC = ((points[2][0]-points[1][0])**2 + (points[2][1]-points[1][1])**2)**(0.5)
    return AB + BC + AC


maxL = 0
pointsOfmaxL = []
for line in open("wspolrzedneTR.txt"):
    xy = list(map(int, line.split()))
    points = []
    for i in range(0, len(xy), 2):
        points.append([xy[i], xy[i+1]])
    currL = L(points)
    if maxL < currL:
        maxL = currL
        pointsOfmaxL = points

print("Największy obwód:", round(maxL, 2))
print("Wierzchołki okręgu o największym obwodzie:", pointsOfmaxL)
