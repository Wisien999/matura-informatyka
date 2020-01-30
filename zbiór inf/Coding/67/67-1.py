fib = [1, 1]
for i in range(38):
    fib.append(fib[-1] + fib[-2])


print("Fib10:", fib[9])
print("Fib20:", fib[19])
print("Fib30:", fib[29])
print("Fib40:", fib[39])
