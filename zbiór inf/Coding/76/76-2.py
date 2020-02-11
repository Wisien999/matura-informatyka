f = open("szyfr2.txt")
lines = f.readlines()

text = lines[0][:-1]

key = [int(el) for el in lines[1].split()]

f.close()


def encrypt(word, key):
    word = list(word)
    for i in range(len(word)):
        word[i], word[key[i % len(key)] - 1] = word[key[i %
                                                        len(key)] - 1], word[i]
    return ''.join(word)


print(encrypt(text, key))
