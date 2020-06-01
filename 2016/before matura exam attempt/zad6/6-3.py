def encrypt(c, k):
    code = ord(c) - 65
    code += k
    code = code % 26
    code += 65
    return chr(code)


def check(word, encrypted):
    k = ord(encrypted[0]) - ord(word[0])
    if k < 0:
        k = 26 + k

    for i in range(len(word)):
        if encrypt(word[i], k) != encrypted[i]:
            print(word)
            print(i, k, word[i], encrypted[i])
            
            return False
    return True

with open("dane_6_3.txt") as f:
    with open("wyniki_6_3.txt", "w") as ff:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            word, encrypted = line.split()
            if not check(word, encrypted):
                ff.write(word + "\n")
        
