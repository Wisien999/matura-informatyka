with open("dane.txt") as f:
    pixel = f.readlines()
    for i in range(len(pixel)):
        pixel[i] = list(map(int, pixel[i].split()))
    maxi = 0
    for x in range(320):
        counter = 1
        for y in range(1, 200):
            if pixel[y][x] == pixel[y-1][x]:
                counter += 1
            else:
                maxi = max(maxi, counter)
                counter = 1
        maxi = max(counter, maxi)


        
print(maxi)
