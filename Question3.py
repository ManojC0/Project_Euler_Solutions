import math
num= 600851475143
factors = []
while num % 2 == 0:
    num = num / 2

for i in range(3,int(math.sqrt(num))+1,2):
    if num % i ==0:
        print(i)
        num = num /i
        factors.append(i)


x = sorted(factors)
print(x)

