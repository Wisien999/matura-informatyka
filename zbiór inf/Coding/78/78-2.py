def endecryptA(signature, d, n):
    if signature[-1] == "\n":
        signature = signature[:-1]
    result = ""
    for elem in list(map(int, signature.split())):
        result += chr((elem * d) % n)
    return result


f = open("podpisy.txt")

signatures = f.readlines()

for line in signatures:
    print(endecryptA(line, 3, 200))
