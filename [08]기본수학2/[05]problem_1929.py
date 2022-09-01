from sys import stdin
import math

num1,num2 = stdin.readline().rstrip().split()
num1,num2 = int(num1),int(num2)+1

li = [True for i in range(0,num2)]
li[0] = False
li[1] = False
for i in range(2,int(math.sqrt(num2) + 1)) :
    if li[i] == True :
        j = 2
        while i * j < num2:
            li[i * j] = False
            j = j + 1
for i in range(num1, num2):
    if li[i]:
        print(i)