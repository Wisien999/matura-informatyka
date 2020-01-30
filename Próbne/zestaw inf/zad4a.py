f = open("dane_anagramy.txt")
lines = f.read().split("\n")
f.close()
print(lines)

count = 0
for line in lines:
    amountofdigitsa = {}
    amountofdigitsb = {}
    a = line.split()[0]
    b = line.split()[1]
    for digit in a:
        amountofdigitsa[int(digit)] = a.count(digit)
    for digit in b:
        amountofdigitsb[int(digit)] = b.count(digit)
    if amountofdigitsa == amountofdigitsb:
        count += 1

print(count)
