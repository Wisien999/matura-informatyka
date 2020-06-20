import math

max_gcd = 1
max_i, max_j = 0, 0

with open("liczby.txt") as f:
    num = list(map(int, f.read().splitlines()))
    for i in range(len(num)):
        gcd = num[i]
        for j in range(i+1, len(num)):
            if math.gcd(gcd, num[j]) == 1:
                if j-1 - i > max_j - max_i:
                    max_j = j - 1
                    max_i = i
                    max_gcd = gcd
                break
            gcd = math.gcd(gcd, num[j])

print("Pierwsza liczba:", num[max_i])
print("Długość ciągu:", max_j - max_i + 1)
print("NWD:", max_gcd)

