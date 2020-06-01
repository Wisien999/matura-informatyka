counter = 0
with open("punkty.txt") as f:
    for line in f.readlines():
        x, y = list(map(int, line.split()))
        
        if (x-200)**2 + (y-200)**2 == 40000:
            print(x, y)
        elif (x-200)**2 + (y-200)**2 < 40000:
            counter += 1

print("Punktów we wnętrzu koła:", counter)
