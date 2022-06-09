from sys import stdin
h,m = map(int,stdin.readline().split())
t = m + (h*60)
if t < 45 :
    t = t + (24*60)
t = t - 45
h = t // 60
m = t % 60
print(h,m)