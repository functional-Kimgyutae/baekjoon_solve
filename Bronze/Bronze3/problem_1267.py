import math
from sys import stdin
n = int(stdin.readline())
li = list(map(int,stdin.readline().split()))
li1 = [0] * n
li2 = [0] * n
sum1 = 0
for i in range(n) :
    x = math.ceil(li[i]/30)
    if li[i]%30 == 0 :
        sum1+= (x+1) * 10
    else :
        sum1+= (x) * 10
    li1[i] = li[i]%30


sum2 = 0
for i in range(n) :
    x = math.ceil(li[i]/60)
    if li[i]%60 == 0 :
        sum2+= (x+1) * 15
    else :
        sum2+= (x) * 15
    li2[i] = li[i]%60

if sum1 == sum2 :
    print("Y M",sum1)
elif sum1 > sum2 :
    print("M",sum2)
else :
    print("Y",sum1)
