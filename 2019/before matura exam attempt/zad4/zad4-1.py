tab = set()
for i in range(12):
    tab.add(3**i)

counter = 0
with open("liczby.txt") as f:
    for num in f.read().splitlines():
        num = int(num)
        if num in tab:
            counter += 1

print(counter)
