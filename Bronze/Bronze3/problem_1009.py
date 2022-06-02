cnt = int(input())
arr = []
for i in range(cnt) :
    arr.append([])
    a,b= input().split()
    arr[i].append(int(a)%10)
    arr[i].append(int(b))

for i in range(cnt) :
    total = arr[i][0] ** arr[i][1]
    if total%10 == 0: 
        print(10)
    else :
        print(total%10)
    

