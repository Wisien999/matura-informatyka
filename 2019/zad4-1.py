file = open("liczby.txt", "r")

answer = 0
numbers = file.readlines()
for number in numbers:
    number = int(number)
    while number % 3 == 0:
        number /= 3
    if number == 1:
        answer += 1

print(answer)
