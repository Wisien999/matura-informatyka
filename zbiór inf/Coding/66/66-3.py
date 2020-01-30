def is_c_triange(lis):
    a, b, c = sorted(map(int, lis))
    return a*a + b*b == c*c

    

f = open("trojki.txt")

last_c = False
last = ""
for line in f.readlines():
    corr = is_c_triange(line.split())
    if corr:
        if last_c:
            print(last)
            print(line)
        last = line[:-1]
        last_c = True
    else:
        last_c = False


f.close()
