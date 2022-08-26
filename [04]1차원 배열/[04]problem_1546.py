from sys import stdin
i = int(stdin.readline())
list = list(map(int,stdin.readline().split()))
ma = max(list)
sum = 0
for a in range(i) :
    sum += list[a] / ma * 100
print(sum / len(list))
#가장 작은 값 찾고 나누기 