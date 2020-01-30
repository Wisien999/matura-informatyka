f = open("dane_obrazki.txt")

maxi = 0
poprawne = 0
naprawialne = 0
nienaprawialne = 0
lines = f.readlines()
for num_pic in range(200):
    start_index = num_pic * 22
    bad_lines = 0
    for i in range(20):
        if lines[start_index+i][-1] == '\n':
            line = lines[start_index+i][:-1]
        else:
            line = lines[start_index+i]
        even_bit = int(line[-1])
        line = line[:-1]
        if line.count("1") % 2 != even_bit:
            bad_lines += 1

    bad_columns = 0
    for i in range(20):
        column = ""
        for j in range(20):
            column += lines[start_index+j][i]
        even_bit = int(lines[start_index+20][i])
        if column.count("1") % 2 != even_bit:
            bad_columns += 1

    if bad_columns + bad_lines == 0:
        poprawne += 1
    elif bad_columns < 2 and bad_lines < 2:
        naprawialne += 1
    else:
        nienaprawialne += 1
    maxi = max(maxi, bad_lines + bad_columns)


print("Poprawne:", poprawne)
print("Naprawialne:", naprawialne)
print("Nienaprawialne:", nienaprawialne)
print("Największa liczba błędnych bitów parzystości:", maxi)
