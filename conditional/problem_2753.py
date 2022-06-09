from sys import stdin
year = int(stdin.readline())
h = year % 100
a = year // 100

if h == 0 :
    if a % 4 == 0 :
        print("1") 
    else :
        print("0")
else :
    if h % 4 == 0 :
        print("1") 
    else :
        print("0")