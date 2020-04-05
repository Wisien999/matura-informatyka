def oneLine(points):
    u = [points[1][0]-points[0][0], points[1][1]-points[0][1]]
    v = [points[2][0]-points[0][0], points[2][1]-points[0][1]]
    W = u[0]*v[1] - v[0]*u[1]
    if W == 0:
        return True
    return False


count = 0
for line in open("wspolrzedne.txt"):
    xy = list(map(int, line.split()))
    points = []
    for i in range(0, len(xy), 2):
        points.append([xy[i], xy[i+1]])
    if oneLine(points):
        count += 1

print(count)
