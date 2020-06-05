with open("dane.txt") as f:
    count = 0
    for line in f.readlines():
        pixels = list(map(int, line.split()))
        for i in range(len(pixels)//2 + 1):
            if pixels[i] != pixels[len(pixels)-1-i]:
                count += 1
                break

print("Ile wierszy należy usunąć:", count)
        
