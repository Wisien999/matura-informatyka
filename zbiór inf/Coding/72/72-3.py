max_leng = 0

for i in open("napisy.txt"):
    text1, text2 = i.split()
    len1 = len(text1)
    len2 = len(text2)
    leng = 0
    for i in range(-1, -max(len1, len2), -1):
        if text1[i] == text2[i]:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            break

print(max_leng)

for i in open("napisy.txt"):
    text1, text2 = i.split()
    if text1[-max_leng:] == text2[-max_leng:]:
        print(text1, text2)
