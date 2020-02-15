f = open("szyfr.txt")
text = f.readline()[:-1]
key = f.readline()[:-1]
f.close()

letters = {}

for i in range(ord("A"), ord("Z") + 1, 1):
    letters.update({chr(i): 0})

for c in text:
    if ord(c) >= ord("A") and ord(c) <= ord("Z"):
        letters[c] += 1

print(letters)

n = 0
for c in text:
    if ord(c) >= ord("A") and ord(c) <= ord("Z"):
        n += 1


k = 0
for letter in letters.values():
    k += letter*(letter - 1)

k = k / (n*(n - 1))

d = 0.0285/(k-0.0385)

print("Szacowana długość klucza:", round(d, 2))
print("Dokładna długość klucza:", len(key))
