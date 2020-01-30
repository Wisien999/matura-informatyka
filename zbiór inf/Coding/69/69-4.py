def findGen(line):
    gens = []
    endingPostition = 0  # last end postition
    # go through all characters
    for i in range(0, len(line) - 1):
        # find start pattern
        if line[i] == "A" and line[i+1] == "A":
            # Found AA
            gen = ""
            # Ensure that end was found
            if i >= endingPostition:
                k = i  # select start index
                # go through chars (i -> end - 1)
                for k in range(i, len(line) - 1):
                    # find end pattern
                    if(line[k] == "B" and line[k+1] == "B"):
                        # found ending
                        endingPostition = k  # define where should start
                        gen += "BB"
                        break
                    else:
                        # not found ending. Add next char
                        gen += line[k]

            # won't add gen if not have ending
            if gen.find("BB") > 0:
                gens.append(gen)

            gen = ""

    return gens


def analyze(genotyp):
    if genotyp == genotyp[::-1]:
        return 0
    gens = findGen(genotyp)

    counter = 0
    for gen in gens:
        # find reversed gens in it
        if genotyp.find(gen[::-1]) > -1:
            counter += 1

    if counter == len(gens):
        return 1
    return 2


ammount = [0, 0, 0]
for i in open("dane_geny.txt"):
    pass
    if i[-1] == '\n':
        i = i[:-1]
    ammount[analyze(i)] += 1
print(ammount[0], ammount[1])
