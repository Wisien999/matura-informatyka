ammount = 0

for i in open("napisy.txt"):
    text1, text2 = i.split()
    len1 = len(text1)
    if text1 == text2[:len1]:
        ammount += 1
        print(text1, text2, text2[len1:])
print(ammount)
