from sys import stdin
num = int(stdin.readline())

def hanso(num) :
    han = 0
    if num <= 99 :
        han = num
        return han
    else : 
        han = 99
        num = num  if num <= 999 else 999
        for i in range(100,num+1) :
            li = list(map(int,list(str(i))))
            han = han + 1 if li[1]*2 == li[0] + li[2] else han
    return han

print(hanso(num))