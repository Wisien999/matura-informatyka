file = open("przyklad.txt", "r")
words = file.readlines()
file.close()


amount = 0
maxword = ""

for i in range(len(words)):
    letters = []
    word = words[i]
    for j in range(len(words[i])-1):
        if word[j] not in letters:
            letters.append(word[j])
    if amount < len(word):
        amount = len(letters)
        maxword = word
print(maxword, amount)