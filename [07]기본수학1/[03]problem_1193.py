from sys import stdin
num = int(stdin.readline().rstrip())
icc = 1
sum = 1
while(num > sum) :
    icc+= 1
    sum += icc

num = num -(sum - icc)
a = icc - num+1
if icc % 2 == 0 :
    print("{}/{}".format(num,a))
else :
    print("{}/{}".format(a,num))

