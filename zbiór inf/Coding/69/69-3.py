def analyze(genotyp):
    koduje = False
    ilosc = 0
    max_leng = 0
    start = 0
    for i in range(1, len(genotyp)):
        if (not koduje) and genotyp[i-1] == "A" and genotyp[i] == "A":
            koduje = True
            start = i-1
        elif koduje and genotyp[i-1] == "B" and genotyp[i] == "B":
            koduje = False
            ilosc += 1
            if max_leng < i - start + 1:
                max_leng = i - start + 1
    return ilosc, max_leng


max_leng, max_ammount = 0, 0
for i in open("dane_geny.txt"):
    ammount, leng = analyze(i)
    max_ammount = max(max_ammount, ammount)
    max_leng = max(max_leng, leng)
print(max_ammount, max_leng)
