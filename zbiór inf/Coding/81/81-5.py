def pointD(points):
    u = [points[1][0]-points[0][0], points[1][1]-points[0][1]]
    x, y = points[2][0] - u[0], points[2][1] - u[1]
    return x == y, x


for line in open("wspolrzedneTR.txt"):
    xy = list(map(int, line.split()))
    points = []
    for i in range(0, len(xy), 2):
        points.append([xy[i], xy[i+1]])

    isDonyx, x = pointD(points)
    if isDonyx:
        points.append([x, x])
        print(points)
