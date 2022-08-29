from sys import stdin
str = list(str(stdin.readline()))
sum = 0
for i in range(len(str)) :
    if str[i] in "ABC" :
        sum += 3
    elif str[i] in "DEF" :
        sum += 4
    elif str[i] in "GHI" :
        sum += 5
    elif str[i] in "JKL" :
        sum += 6
    elif str[i] in "MNO" :
        sum += 7
    elif str[i] in "PQRS" :
        sum += 8
    elif str[i] in "TUV" :
        sum += 9
    elif str[i] in "WXYZ" :
        sum += 10
    
print(sum)