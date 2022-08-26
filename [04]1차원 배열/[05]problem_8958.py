from sys import stdin
le = int(stdin.readline())
sum = ic = 0
str = ""
for i in range(le) :
    sum = ic = 0
    str = list(stdin.readline())
    for char in str :
        if char == "O" :
            ic+=1
            sum+= ic
        else :
            ic = 0
    print(sum)

