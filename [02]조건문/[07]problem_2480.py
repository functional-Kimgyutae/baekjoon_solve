from sys import stdin
li = list(map(int,stdin.readline().split()))

li.sort(reverse=True)
if li[0] == li[1] :
    if li[1] == li[2] :
        print(10000 +(li[0]*1000))
    else :
        print(1000 +(li[0]*100))
elif li[1] == li[2] :
        print(1000 +(li[1]*100))
else :
    print(li[0] * 100)
