f = open("dane_obrazki.txt")

ammount = 0
lines = f.readlines()
first = ""
for pic in range(200):
    start_index = pic * 22
    pic1 = []
    pic2 = []
    pic3 = []
    pic4 = []
    for i in range(10):
        pic1.append(lines[start_index+i][:10])
    for i in range(10):
        pic2.append(lines[start_index+i][10:-2])
    for i in range(10):
        pic3.append(lines[start_index+10+i][:10])
    for i in range(10):
        pic4.append(lines[start_index+10+i][10:-2])
    if pic1 == pic2 and pic1 == pic3 and pic1 == pic4:
        ammount += 1
        if first == "":
            for i in range(20):
                first += lines[start_index+i][:-2] + "\n"


print(ammount)
print(first)
