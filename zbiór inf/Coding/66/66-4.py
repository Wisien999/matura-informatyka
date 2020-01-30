def is_triange(lis):
    a, b, c = sorted(map(int, lis))
    return a + b > c

    

f = open("trojki.txt")

last_c = False
max_leng = 0
leng = 0
ammount = 0
for line in f.readlines():
    corr = is_triange(line.split())
    if corr:
        leng += 1
        ammount += 1
        max_leng = max(max_leng, leng)
    else:
        leng = 0


print("Ilość wierszy:", ammount)
print("Największa długość:", max_leng)

f.close()
