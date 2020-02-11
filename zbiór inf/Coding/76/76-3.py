f = open("szyfr3.txt")
lines = f.readlines()

text = lines[0]

f.close()


def decrypt(word, key):
    word = list(word)
    for i in reversed(range(len(word))):
        word[i], word[key[i % len(key)] - 1] = word[key[i %
                                                        len(key)] - 1], word[i]
    return ''.join(word)


print(decrypt(text, [6, 2, 4, 1, 5, 3]))
