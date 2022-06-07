from sys import stdin
li = [0,0,0,0,0,0,0,0]
for i in range(8) :
    li2 = list(input())
    li[i] = li2 
cnt = 0
for i in range(8) :
    for j in range(8) :
        if i%2 ==0 and j%2==0 :
            if li[i][j] == "F" :
                cnt+=1
        elif i%2==1 and j%2==1 :
            if li[i][j] == "F" :
                cnt+=1

print(cnt)
