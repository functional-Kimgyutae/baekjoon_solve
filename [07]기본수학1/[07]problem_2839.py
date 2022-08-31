from sys import stdin
num = int(stdin.readline().rstrip())
n = num // 5

while True :
    if (num-(n*5))%3 == 0 :
        total = n + ((num-(n*5))//3)
        print(total)
        break
    n = n -1
    if n== -1:
        print("-1")
        break
