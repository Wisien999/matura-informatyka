ammount = 0

for i in open("napisy.txt"):
    text1, text2 = i.split()
    len1 = len(text1)
    len2 = len(text2)
    if len1 >= len2*3 or len2 >= len1*3:
        ammount += 1
        if ammount == 1:
            print(i)
print(ammount)
