f = open("szyfr.txt")
text = f.readline()[:-1]
key = f.readline()[:-1]
f.close()


def decrypt(text, key):
    text = list(text)
    i = 0
    for c in range(len(text)):
        if ord(text[c]) >= ord("A") and ord(text[c]) <= ord("Z"):
            k = ord(key[i % len(key)]) - ord("A")
            new_letter = ord(text[c]) - k
            if new_letter < ord("A"):
                new_letter += 26
            text[c] = chr(new_letter)
            i += 1
    return ''.join(text)


print(decrypt(text, key))
