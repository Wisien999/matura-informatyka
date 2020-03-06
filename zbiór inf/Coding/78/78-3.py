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
    return result


def endecryptA(signature, d, n):
    if signature[-1] == "\n":
        signature = signature[:-1]
    result = ""
    for elem in list(map(int, signature.split())):
        result += chr((elem * d) % n)
    return result


signatures = open("podpisy.txt")
msgs = open("wiadomosci.txt")

for i in range(11):
    if skrot(msgs.readline()) == endecryptA(signatures.readline(), 3, 200):
        print(i+1, end=" ")

print()
