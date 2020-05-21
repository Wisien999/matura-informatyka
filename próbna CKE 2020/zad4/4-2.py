f = open("dane4.txt")

liczby = list(map(int, f.readlines()))

p = 0
max_leng = 0
r = abs(liczby[1] - liczby[0])
first, last = 0, 0

for i in range(2, len(liczby)):
    curr_r = abs(liczby[i] - liczby[i-1])
    if curr_r != r:
        if i - p > max_leng:
            first = liczby[p]
            last = liczby[i-1]
            max_leng = i - p
        p = i - 1
        r = curr_r


print("Długość:", max_leng)
print("Liczba na początku:", first)
print("Liczba na końcu:", last)
