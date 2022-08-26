from sys import stdin
pay = int(stdin.readline().rstrip())
n = int(stdin.readline().rstrip())
total = 0
for i in range(n) :
    price,cnt = stdin.readline().rstrip().split()
    total = total+(int(price)* int(cnt))
print("Yes" if total == pay else "No")