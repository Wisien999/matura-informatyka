maxi = 0
maxi_word = ""
with open("sygnaly.txt") as f:
    lines = f.readlines()
    for i in range(1000):
        if lines[i][-1] == "\n":
            lines[i] = lines[i][:-1]
        letters = len(set((lines[i])))
        if maxi < letters:
            maxi = letters
            maxi_word = lines[i]

print(maxi_word, maxi)
