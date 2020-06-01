def encrypt(txt, k):
    encrypted = []
    for i in range(len(txt)):
        code = ord(txt[i]) - 65
        code += k
        code = code % 26
        code += 65
        encrypted.append(chr(code))
    return "".join(encrypted)

with open("dane_6_1.txt") as f:
    k = 107
    for line in f.readlines():
        if line[-1] == "\n":
            line = line[:-1]
        print(encrypt(line, k))
        
