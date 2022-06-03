from sys import stdin
li = list(map(int,stdin.readline().split()))

sum = 0
for i in range(5) :
    sum += li[i]*li[i]

print(sum%10)