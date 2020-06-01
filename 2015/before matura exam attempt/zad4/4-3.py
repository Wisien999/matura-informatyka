def find_max(nums):
    leng = list(map(len, lines))
    max_leng = max(leng)
    max_num_i = -1
    max_num_0pos = -1
    
    for i in range(len(nums)):
        zero_i = nums[i].find("0")
        if len(nums[i]) == max_leng and zero_i > max_num_0pos:
            max_num_0pos = zero_i
            max_num_i = i+1

    return max_num_i

def find_min(nums):
    leng = list(map(len, lines))
    min_leng = min(leng)
    min_num_i = 0
    min_num_0pos = float("+inf")
    min_num_sec0pos = -1
    
    for i in range(len(nums)):
        zero_i = nums[i].find("0")
        second_zero = nums[i][zero_i+1:].find("0")
        
        if zero_i == -1:
            zero_i = 1000
        if len(nums[i]) == min_leng and zero_i < min_num_0pos:
            if second_zero > min_num_sec0pos:
                min_num_0pos = zero_i
                min_num_i = i+1

    return min_num_i

with open("liczby.txt") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if lines[i][-1] == "\n":
            lines[i] = lines[i][:-1]
    print("Indeks największej:", find_max(lines))
    print("Indeks najmniejszej:", find_min(lines))

