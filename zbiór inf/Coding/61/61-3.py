def find_err(seq):
    seq = list(map(int, seq))
    i = 2
    r = 0
    rs = []
    rs.append(seq[1]-seq[0])
    while i < len(seq):
        rs.append(seq[i]-seq[i-1])
        if rs.count(rs[-1]) > 1:
            r = rs[-1]
            break
        i += 1
    if rs.count(r) == len(rs):
        while i < len(seq):
            if seq[i] != seq[i-1] + r:
                return seq[i]
            i += 1
    else:
        i -= 1
        while i >= 0:
            if seq[i] != seq[i+1] - r:
                return seq[i]
            i -= 1


f = open("bledne.txt")
lines = f.readlines()
f.close()

for i in range(1, len(lines), 2):
    print(find_err(lines[i].split(" ")))
