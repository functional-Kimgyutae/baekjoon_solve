from sys import stdin
import math

num1 = int(stdin.readline().rstrip())
num2 = int(stdin.readline().rstrip())+1
li = [True for i in range(0,num2)]
li[0] = False
li[1] = False
cnt = 0
for i in range(2,int(math.sqrt(num2) + 1)) :
    if li[i] == True :
        j = 2
        while i * j < num2:
            li[i * j] = False
            j = j + 1
cnt = 0 
f = True        
a = -1   
for i in range(num1, num2):
    if li[i]:
        cnt += i
        if f :
            a = i
            f = False
if f:
    print("-1")
else :
    print(cnt)
    print(a)
