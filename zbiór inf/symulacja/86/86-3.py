results = {}
for line in open("dane_wybory.txt"):
    result = line.split()
    results.update({result[0]: list(map(int, result[1:]))})


K = [0, 0, 0, 0, 0]

for area in results.keys():
    k = [0, 0, 0, 0, 0]
    for i in range(20):
        w = [0, 0, 0, 0, 0]
        for komitet in range(5):
            w[komitet] = results[area][komitet]/(2*k[komitet]+1)
        k[w.index(max(w))] += 1
    for i in range(len(K)):
        K[i] = max(K[i], k[i])

print(K)

