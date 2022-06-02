import math
a,b,c =input().split()
a = int(a)
b = int(b)
c = int(c)
n = b-c
if n < 0 :
    num = math.ceil(a / abs(n))

    if a % abs(n) == 0 :
        num+=1
    print(num)
else : 
    print(-1)