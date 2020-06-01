def decrypt(txt, k):
    encrypted = []
    for i in range(len(txt)):
        code = ord(txt[i]) - 65
        code -= k
        code = code % 26
        code += 65
        encrypted.append(chr(code))
    return "".join(encrypted)

with open("dane_6_2.txt") as f:
    with open("zad2.txt", "w") as ff:
        for line in f.readlines():
            if line[-1] == "\n":
                line = line[:-1]
            x = line.split()
            if len(x) > 1:
                text, k = x
            else:
                text = x[0]
                k =0
            k = int(k)
        
            ff.write(str(decrypt(text, k))+ "\n")
        
