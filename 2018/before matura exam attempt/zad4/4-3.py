def passTest(word):
    for c1 in word:
        for c2 in word:
            if abs(ord(c1) - ord(c2)) > 10:
                return False
    return True


with open("sygnaly.txt") as f:
    lines = f.readlines()
    for i in range(1000):
        if lines[i][-1] == "\n":
            lines[i] = lines[i][:-1]
        if passTest(lines[i]):
            print(lines[i])

