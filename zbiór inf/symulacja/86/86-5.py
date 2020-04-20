def do(m):
    for q in range(0, 100000):
        results = [q, 100000 - q]
        k = [0, 0]
        for i in range(2*m):
            w = [0, 0]
            for komitet in range(2):
                w[komitet] = 1.0*results[komitet]/(2*k[komitet]+1)
            k[w.index(max(w))] += 1
        if k[0] == k[1]:
            print("m =", m, " : ", q)
            return 0


do(10)
do(20)
do(50)

