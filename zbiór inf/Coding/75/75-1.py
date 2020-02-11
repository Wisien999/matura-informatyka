words = [word for word in open("tekst.txt").readline().split()]

for word in words:
    if word[0] == 'd' and word[-1] == 'd':
        print(word)