from sys import stdin

a,b = map(int,stdin.readline().split())
li = list(map(int,stdin.readline().split()))
for i in range(a) :
    if li[i] < b :
        print(li[i],end=" ")
