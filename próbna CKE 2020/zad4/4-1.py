f = open("dane4.txt")

liczby = list(map(int, f.readlines()))
max_r = 0
min_r = float("inf")
for i in range(1, len(liczby)):
    r = abs(liczby[i] - liczby[i-1])
    max_r = max(max_r, r)
    min_r = min(min_r, r)


print("Największa luka:", max_r)
print("Najmniejsza luka:", min_r)    
