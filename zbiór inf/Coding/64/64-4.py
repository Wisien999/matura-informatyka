f = open("dane_obrazki.txt")


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
            bad_line = i + 1

    bad_columns = 0
    for i in range(20):
        column = ""
        for j in range(20):
            column += lines[start_index+j][i]
        even_bit = int(lines[start_index+20][i])
        if column.count("1") % 2 != even_bit:
            bad_columns += 1
            bad_column = i + 1

    if bad_columns == 1 and bad_lines == 1:
        print("Pic", num_pic + 1, ": wiersz", bad_line, "kolumna", bad_column)
    elif bad_columns == 1 and bad_lines == 0:
        print("Pic", num_pic + 1, ": wiersz", 21, "kolumna", bad_column)
    elif bad_columns == 0 and bad_lines == 1:
        print("Pic", num_pic + 1, ": wiersz", bad_line, "kolumna", 21)

