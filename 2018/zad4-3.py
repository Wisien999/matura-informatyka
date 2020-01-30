file = open("przyklad.txt", "r")
words = file.readlines()
file.close()

for word in words:
    letters = [ord(char) for char in word]
    letters.pop()
    if max(letters) - min(letters) <= 10:
        print(word, end="")
