from sys import stdin
n = int(stdin.readline())

newNumber = n
topNumber = n // 10
cnt = 0

while True :
    first = topNumber
    c = newNumber % 10
    a = c + first
    newNumber = c*10 + a%10
    topNumber = c
    cnt += 1
    if n == newNumber :
        print(cnt)
        break
