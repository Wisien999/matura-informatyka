def corr(seq):
    if seq[-1] == '\n':
        seq = seq[:-1]
    for i in range(1, len(seq)):
        if seq[i] == '1' and seq[i-1] == '1':
            return False
    return True


f = open("ciagi.txt")
ammount = 0
for line in f.readlines():
    if corr(line):
        ammount += 1

f.close()
print(ammount)
