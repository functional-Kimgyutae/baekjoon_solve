from sys import stdin
h,m = map(int,stdin.readline().split())
t = int(stdin.readline())

m = m + t
t = m // 60
m = m % 60
h = (h + t) % 24

print(h,m)
