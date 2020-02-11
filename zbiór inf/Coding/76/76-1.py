f = open("szyfr1.txt")
lines = f.readlines()

texts = []
for i in range(6):
    if lines[i][-1] == '\n':
        texts.append(lines[i][:-1])
    else:
        texts.append(lines[i])

key = [int(el) for el in lines[6].split()]

f.close()


def encrypt(word, key):
    word = list(word)
    for i in range(len(word)):
        word[i], word[key[i % len(key)] - 1] = word[key[i % len(key)] - 1], word[i]
    return ''.join(word)


for text in texts:
    print(encrypt(text, key))
