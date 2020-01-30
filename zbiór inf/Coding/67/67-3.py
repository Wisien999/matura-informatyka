fib = [1, 1]
for i in range(38):
    fib.append(fib[-1] + fib[-2])

maxi = len(bin(fib[-1])[2:])
for elem in fib:
        bin_f = bin(elem)[2:]
        print("0"*(maxi-len(bin_f))+bin_f)
