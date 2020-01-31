f = open("hasla.txt")
passwords = []

for pw in f.readlines():
    if pw[-1] == '\n':
        pw = pw[:-1]
    passwords.append(pw)


f.close()
ammount = 0
for password in passwords:
    for i in range(len(password) - 3):
        chars = sorted(password[i:i+4])
        
        corr = True
        for j in range(1, 4):
            if ord(chars[0]) != ord(chars[j])-j:
                corr = False
                break
        if corr:
            ammount += 1
            break


print(ammount)
