def nadzies(num):
    power = 1
    suma = 0
    for c in reversed(num):
        suma += int(c)*power
        power *= 8
    return suma

print(nadzies("13"))

f = open("liczby1.txt")
maxi, mini = "0", "77777777777"
for line in f.readlines():
    if line[-1] == '\n':
        line = line[:-1]
    num = nadzies(line)
    if num > nadzies(maxi):
        maxi = line
    if num < nadzies(mini):
        mini = line

print("Max:", maxi, "Min:", mini)
