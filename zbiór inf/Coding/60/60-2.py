def nadzielniki(num):
    div = []
    ile = 0
    for i in range(1, num+1):
        if num % i == 0:
            div.append(i)
            ile += 1
        if ile > 18:
            return False, []
    return ile == 18, div


f = open("liczby.txt")

for line in f.readlines():
    num = int(line)
    corr, divi = nadzielniki(num)
    if corr:
        print(num)
        print(divi)

f.close()
