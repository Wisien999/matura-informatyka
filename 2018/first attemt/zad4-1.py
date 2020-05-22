file = open("sygnaly.txt", "r")

words = file.readlines()

for i in range(39, 1000, 40):
    print(words[i][9], end="")
print("")