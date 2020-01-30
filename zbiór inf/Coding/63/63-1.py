def is_dual(seq):
    if seq[-1] == '\n':
        seq = seq[:-1]
    if len(seq)%2 == 1:
        return False
    if seq[:(len(seq)//2)] == seq[(len(seq)//2):]:
        return True
    return False

f = open("ciagi.txt")
for line in f.readlines():
    if is_dual(line):
        print(line, end="")


f.close()
