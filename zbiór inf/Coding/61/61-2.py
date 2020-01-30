def is_cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        return True
    else:
        return False


def find_perfect_cube(seq):
    maxi = -1
    for i in seq:
        if is_cube(int(i)):
            maxi = int(i)
    return maxi


f = open("ciagi.txt")
lines = f.readlines()
f.close()

for i in range(1, len(lines), 2):
    r = find_perfect_cube(lines[i].split(" "))
    if r > 0:
        print(r)
