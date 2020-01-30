f = open("liczby.txt")
ile = 0
last = 0
prelast = 0
for line in f.readlines():
    num = int(line)
    if num < 1000:
        ile += 1
        prelast = last
        last = num

f.close()
print("Ilość:", ile, "\nPrzed ostatnia:", prelast, "\nOstatnia:", last)
