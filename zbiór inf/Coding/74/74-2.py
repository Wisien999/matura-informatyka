f = open("hasla.txt")
passwords = []

for pw in f.readlines():
    if pw[-1] == '\n':
        pw = pw[:-1]
    passwords.append(pw)

f.close()

seen_in_past = []
doubled = []
for password in passwords:
    if password in seen_in_past:
        doubled.append(password)
    seen_in_past.append(password)

for pw in sorted(doubled):
    print(pw)
