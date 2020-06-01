from math import pi

def Pi(n):
    nk = 0
    with open("punkty.txt") as f:
        for line in f.readlines()[:n]:
            x, y = list(map(int, line.split()))
        
            if (x-200)**2 + (y-200)**2 <= 40000:
                nk += 1

    return (nk*4)/n


with open("epsilons1.txt", "w") as ff:
    for i in range(1, 1701):
        ff.write("n="+ str(i) + ";"+ str(abs(pi - Pi(i)))+"\n")

with open("epsilons2.txt", "w") as ff:
    for i in range(1000, 1701):
        ff.write("n="+ str(i) + "; "+ str(round(abs(pi - Pi(i)), 4))+"\n")


    
