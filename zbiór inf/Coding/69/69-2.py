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


def have_mutation(genotyp):
    gens = findGen(genotyp)

    for gen in gens:
        if gen.find("BCDDC") > -1:
            return True

    return False


ammount = 0
for i in open("dane_geny.txt"):
    if have_mutation(i):
        ammount += 1
print(ammount)
