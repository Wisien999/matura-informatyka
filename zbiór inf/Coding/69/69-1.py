gatunki = {}
for i in open("dane_geny.txt"):
    if i[-1] == '\n':
        i = i[:-1]
    if len(i) not in gatunki.keys():
        gatunki.update({len(i): 1})
    else:
        gatunki[len(i)] += 1

print(len(gatunki.keys()))
print(max(gatunki.values()))
