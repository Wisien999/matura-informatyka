def encrypt(word, A, B):
    for i in range(len(word)):
        num = ord(word[i]) - ord("a")
        num = num * A + B
        word = word[:i] + chr(num % 26 + ord("a")) + word[i+1:]
    return word


words = [word for word in open("tekst.txt").readline().split()]

for word in words:
    if len(word) >= 10:
        print(encrypt(word, 5, 2))
