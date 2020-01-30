f = open("liczby.txt")
ammount = 0
for i in range(1000):
    string = f.readline()
    rev_string = ''.join(reversed(string))
    su = int(string) + int(rev_string)
    su = str(su)
    leng = len(su)
    if leng % 2 == 0:
        first = su[:(leng//2)]
        second = su[(leng//2):]
    else:
        first = su[:(leng//2)]
        second = su[((leng//2)+1):]
    if first == ''.join(reversed(second)):
        ammount += 1

f.close()

print(ammount)
