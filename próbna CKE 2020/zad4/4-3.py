f = open("dane4.txt")

liczby = list(map(int, f.readlines()))

luki = {}

for i in range(1, len(liczby)):
    curr_r = abs(liczby[i] - liczby[i-1])
    if curr_r not in luki.keys():
        luki.update({curr_r: 1})
    else:
        luki[curr_r] += 1

naj_krotnosc = max(luki.values())

print("Krotność najczęstszej luki:", naj_krotnosc)
print("Wartosci najczestszych luk:")

for gap in luki.keys():
    if luki[gap] == naj_krotnosc:
        print(gap, end=", ")
