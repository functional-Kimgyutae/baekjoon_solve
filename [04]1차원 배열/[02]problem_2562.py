from sys import stdin
li = [0] * 9

for i in range(9) :
    li[i] = int(stdin.readline())

idx = 0
for i in range(1,9) :
    if li[idx] < li[i] :
        idx = i

print(li[idx])
print(idx+1)