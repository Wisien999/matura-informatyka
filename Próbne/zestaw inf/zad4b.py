f = open("dane_anagramy.txt")
lines = f.read().split("\n")
f.close()

numbers = []
for line in lines:
    for number in line.split():
        numbers.append("".join(sorted(number)))

maxi = 0
count = 0
for number in numbers:
    count = numbers.count(number)
    maxi = max(maxi, count)
print(maxi)
