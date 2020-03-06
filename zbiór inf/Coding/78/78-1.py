def skrot(message):
    S = list(map(ord, "ALGORYTM"))
    if message[-1] == "\n":
        message = message[:-1]
    to_fill = 8 - (len(message) % 8)
    message = message + ("." * to_fill)
    for start in range(0, len(message), 8):
        for j in range(8):
            S[j] = (S[j] + ord(message[start+j])) % 128
    result = ""
    for j in range(8):
        result += chr(65 + S[j] % 26)
    return len(message), S, result


f = open("wiadomosci.txt")

msg = f.readline()
answer = skrot(msg)
print("Liczba znakóœ wiadomości po uzupełnieniu:", answer[0])
print("Wartości liczbowe 8 kolejnych bajtów skrótu:", answer[1])
print("Skrót wiadomości:", answer[2])
