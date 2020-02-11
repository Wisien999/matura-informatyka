def encrypt(word, A, B):
    for i in range(len(word)):
        num = ord(word[i]) - ord("a")
        num = num * A + B
        word = word[:i] + chr(num % 26 + ord("a")) + word[i+1:]
    return word


words = [line.split() for line in open("probka.txt")]

for word, encr in words:
    for a in range(1, 26):
        skip = False
        for b in range(1, 26):
            if encr == encrypt(word, a, b):
                print("Klucz szyfrujący:", a, b)
                skip = True
                break
        if skip:
            break

    for a in range(1, 26):
        skip = False
        for b in range(1, 26):
            if word == encrypt(encr, a, b):
                print("Klucz deszyfrujący:", a, b)
                skip = True
                break
        if skip:
            break
