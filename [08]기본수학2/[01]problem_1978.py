from sys import stdin
import math

def primNumber(x) :
    if x < 2 :
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

num = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
cnt = 0
for i in li :
    if primNumber(i) :
        cnt = cnt+1
print(cnt)
    