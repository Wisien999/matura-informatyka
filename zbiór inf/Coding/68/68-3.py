lines = open("dane_napisy.txt").readlines()
strings = [el for sublist in lines for el in sublist.split()]

max_ammount = 0
for i in range(len(strings)):
    ammount = 0
    for j in range(len(strings)):
        if sorted(strings[j]) == sorted(strings[i]):
            ammount += 1
    max_ammount = max(max_ammount, ammount)
    
print(max_ammount)
