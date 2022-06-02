cnt = int(input())

two = [2,4,8,6]
three = [3,9,7,1]
four = [4,6]
five = [5]
six = [6]
seven = [7,9,3,1]
eight = [8,4,2,6]
nine = [9,1]

arr = []
for i in range(cnt) :
    arr.append([])
    a,b= input().split()
    if int(a)%10 == 0 :
        arr[i].append(10)
    else :
        arr[i].append(int(a)%10)
    arr[i].append(int(b))

for i in range(cnt) :
    if arr[i][0] == 1 :
        print(1)
    elif arr[i][0] == 2 :
        print(two[arr[i][1]% len(two)-1])
    elif arr[i][0] == 3 :
        print(three[arr[i][1]% len(three)-1])
    elif arr[i][0] == 4 :
        print(four[arr[i][1]% len(four)-1])
    elif arr[i][0] == 5 :
        print(5)
    elif arr[i][0] == 6 :
        print(6)
    elif arr[i][0] == 7 :
        print(seven[arr[i][1]% len(seven)-1])
    elif arr[i][0] == 8 :
        print(eight[arr[i][1]% len(eight)-1])
    elif arr[i][0] == 9 :
        print(nine[arr[i][1]% len(nine)-1])
    elif arr[i][0] == 10 :
        print(10)
    

