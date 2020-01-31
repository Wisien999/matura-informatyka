f = open("hasla.txt")
passwords = []

for pw in f.readlines():
    if pw[-1] == '\n':
        pw = pw[:-1]
    passwords.append(pw)

f.close()


start, stop = ord('0'), ord('9')
ammount = len(passwords)
for password in passwords:
    for c in password:
        if ord(c) < start or ord(c) > stop:
            ammount -= 1
            break

print("Ilość haseł złożonych tylko z cyfr:", ammount)
