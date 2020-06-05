with open("dane.txt") as f:
    count = 0
    pixel = f.readlines()
    for i in range(len(pixel)):
        pixel[i] = list(map(int, pixel[i].split()))
    for y in range(len(pixel)):
        for x in range(len(pixel[y])):
            if x > 0 and abs(pixel[y][x] - pixel[y][x-1]) > 128:
                count += 1
            elif x < len(pixel[y]) - 1 and abs(pixel[y][x] - pixel[y][x+1]) > 128:
                count += 1
            elif y < len(pixel) - 1 and abs(pixel[y][x] - pixel[y+1][x]) > 128:
                count += 1
            elif y > 0 and abs(pixel[y][x] - pixel[y-1][x]) > 128:
                count += 1


        
print(count)
