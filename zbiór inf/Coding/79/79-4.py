import math

circles = []

for line in open("okregi.txt"):
    x, y, r = map(float, line.split())
    circles.append([x, y, r])
circles = circles[:1000]


def has_contact(circle1, circle2):
    SO = math.sqrt((circle1[0]-circle2[0])**2 + (circle1[1]-circle2[1])**2)
    if SO < abs(circle1[2]-circle2[2]):
        return False
    return SO <= circle2[2] + circle1[2]


seqes = []
seq = 1
for i in range(1, len(circles)):
    contact = has_contact(circles[i], circles[i-1])
    if contact:
        seq += 1
    else:
        seqes.append(seq)
        seq = 1
seqes.append(seq)


print("Łańcuchy:", seqes)
print("Najdłuższy łańcuch:", max(seqes))
