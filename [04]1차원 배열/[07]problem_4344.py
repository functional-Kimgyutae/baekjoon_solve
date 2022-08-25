from sys import stdin
num = int(stdin.readline())
for i in range(num) :
    li = list(map(int,stdin.readline().split()))
    ss = (sum(li)-li[0])/li[0]
    cnt = 0
    for l in range(1,len(li)) :
        if li[l] > ss :
            cnt+=1
    print(format(round(cnt/li[0]*100,3),".3f")+"%")
     
