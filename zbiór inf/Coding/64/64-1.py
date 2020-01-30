f = open("dane_obrazki.txt")

maxi = 0
ammount = 0
curr_pic_black = 0
for line in f.readlines():
    if line[-1] == '\n':
        line = line[:-1]
    if len(line) == 0:
        if curr_pic_black > 200:
            ammount += 1
            maxi = max(maxi, curr_pic_black)
        curr_pic_black = 0
        continue
    if len(line) == 21:
        curr_pic_black += line[:-1].count("1")


f.close()
if curr_pic_black > 200:
    ammount += 1
    maxi = max(maxi, curr_pic_black)


print("Ile:", ammount, "\nMax:", maxi)
