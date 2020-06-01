def Pi(n):
    nk = 0
    with open("punkty.txt") as f:
        for line in f.readlines()[:n]:
            x, y = list(map(int, line.split()))
        
            if (x-200)**2 + (y-200)**2 <= 40000:
                nk += 1

    return (nk*4)/n



print("Przybliżenie pi na podstawie 100 punktów:", Pi(100))
print("Przybliżenie pi na podstawie 1000 punktów:", Pi(1000))
print("Przybliżenie pi na podstawie 5000 punktów:", Pi(5000))
print("Przybliżenie pi na podstawie 10000 punktów:", Pi(10000))
