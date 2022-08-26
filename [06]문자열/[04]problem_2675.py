from sys import stdin
num = int(stdin.readline().rstrip())
for i in range(num) :
    r,s = stdin.readline().rstrip().split()
    s = list(s)
    sen = ""
    for j in s :
        sen = sen+(j*int(r))
    print(sen)