def find_sequence(seq):
    max_len = 0
    max_first_elem = 0
    for i in range(len(seq)):
        leng = 1
        for j in range(i+1, len(seq)):
            if seq[j-1] > seq[j]:
                if max_len < leng:
                    max_len = leng
                    max_first_elem = seq[i]
                break
            leng += 1
    return max_len, max_first_elem


f = open("liczby2.txt")
lines = list(map(int, f))
f.close()

print(find_sequence(lines))

