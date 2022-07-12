from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
sum = str(a* b* c)
for i in range(10) :
    print(sum.count(str(i)))