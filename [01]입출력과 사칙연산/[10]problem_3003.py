from sys import stdin
one = [1,1,2,2,2,8]
need = [0 for i in range(6)]
li = list(map(int,stdin.readline().rstrip().split()))
for i in range(len(one)) :
    need[i] = one[i] - li[i]
print(*need)