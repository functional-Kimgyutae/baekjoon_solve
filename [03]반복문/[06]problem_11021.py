from sys import stdin

n = int(stdin.readline())
for i in range(n) :
    a,b = map(int,stdin.readline().split())
    print("Case #{0}: {1}".format(i+1,a+b))
