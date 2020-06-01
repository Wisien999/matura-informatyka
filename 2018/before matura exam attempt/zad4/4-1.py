with open("sygnaly.txt") as f:
    lines = f.readlines()
    for i in range(39, 1000, 40):
        print(lines[i][9], end="")
