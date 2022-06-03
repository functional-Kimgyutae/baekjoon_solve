from sys import stdin
n,m = map(int,stdin.readline().split())
li = list(map(int,stdin.readline().split()))
li2 = [0,0,0,0,0]
str1 = ""
for i in range(5) :
    li2[i] = li[i]-(m*n)
print(li2[0],li2[1],li2[2],li2[3],li2[4])
