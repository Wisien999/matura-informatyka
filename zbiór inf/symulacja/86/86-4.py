results = {}
for line in open("dane_wybory.txt"):
    result = line.split()
    results.update({result[0]: list(map(int, result[1:]))})


K = [0, 0, 0, 0, 0]

for area in results.keys(): # standardowy
    k = [0, 0, 0, 0, 0]
    for i in range(20):
        w = [0, 0, 0, 0, 0]
        for komitet in range(5):
            w[komitet] = 1.0*results[area][komitet]/(2*k[komitet]+1)
        k[w.index(max(w))] += 1
    for i in range(len(K)):
        K[i] += k[i]

print("a) standardowy:", K)



# łącz okręgi
res = {}
for letter in ["A", "B", "C", "D"]:
    res.update({letter: [0, 0, 0, 0, 0]})
    for kom in range(5):
        for i in range(5):
            res[letter][kom] += results[letter + str(i+1)][kom]


K = [0, 0, 0, 0, 0]
for area in res.keys(): # regionalny
    k = [0, 0, 0, 0, 0]
    for i in range(100):
        w = [0, 0, 0, 0, 0]
        for komitet in range(5):
            w[komitet] = 1.0*res[area][komitet]/(2*k[komitet]+1)
        k[w.index(max(w))] += 1
    for i in range(len(K)):
        K[i] += k[i]

print("b) regionalny:", K)
