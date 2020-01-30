import math
def naczynniki(x):
  ile = 0
  if x%2 == 0:
    return False
  i=3
  while x > 1:
    if x%i == 0:
      ile += 1
    while x%i == 0:
      x = x//i
    i += 2
    if ile > 3:
      return False
  return ile==3


f = open("liczby.txt")
ammount = 0
for i in range(1000):
  x = f.readline()
  if x[-1] == '\n':
    x = x[:-1]
  print(x)
  num = int(x)
  #czynniki = naczynniki(num)
  if naczynniki(num):
    ammount += 1

f.close()

print(ammount)
