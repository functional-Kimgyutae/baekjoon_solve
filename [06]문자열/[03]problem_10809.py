from sys import stdin
li = list(stdin.readline().rstrip())
ch = [-1 for i in range(26)]
for i in range(len(li)) :
    n = ord(li[i]) - 97
    ch[n] = i if ch[n]== -1 else ch[n]

print(*ch)