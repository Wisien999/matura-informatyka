f = open("hasla.txt")
passwords = []

for pw in f.readlines():
    if pw[-1] == '\n':
        pw = pw[:-1]
    passwords.append(pw)

f.close()


ammount = 0
for password in passwords:
    digit = False
    small_letter = False
    big_letter = False

    for c in password:
        if ord(c) >= ord("0") and ord(c) <= ord("9"):
            digit = True
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            big_letter = True
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            small_letter = True

    if digit and big_letter and small_letter:
        ammount += 1

print(ammount)
