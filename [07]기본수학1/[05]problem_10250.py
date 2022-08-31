from sys import stdin
num = int(stdin.readline().rstrip())
for i in range(num) :
    H,W,N = stdin.readline().rstrip().split()
    H,W,N = int(H),int(W),int(N)
    MM = N // H + 1
    YY = N % H 
    if YY == 0 :
        YY = H
        MM = MM -1
    if MM < 10 :
        MM = "0"+str(MM)
    print("{}{}".format(YY,MM))