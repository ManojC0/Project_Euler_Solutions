i = 0
backP = 0
forwardP = 1
total = 0
while (forwardP <= 4000000):
    forwardP, backP = backP+forwardP, forwardP
    if forwardP % 2 ==0:
        total += forwardP
  

print(total)
