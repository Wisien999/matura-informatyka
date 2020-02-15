import math


f = open("dokad.txt")
text = f.readline()
f.close()
key = "LUBIMYCZYTAC"


def encrypt(text, key):
    text = list(text)
    i = 0
    for c in range(len(text)):
        if ord(text[c]) >= ord("A") and ord(text[c]) <= ord("Z"):
            k = ord(key[i % len(key)]) - ord("A")
            new_letter = ord(text[c]) + k
            if new_letter > ord("Z"):
                new_letter -= 26
            text[c] = chr(new_letter)
            i += 1
    return ''.join(text)


le = 0
for c in text:
    if ord(c) >= ord("A") and ord(c) <= ord("Z"):
        le += 1


print("Ilość wystąpień klucza:", math.ceil(le/len(key)), end="\n\n")
print(encrypt(text, key))
