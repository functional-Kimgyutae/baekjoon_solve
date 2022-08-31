from sys import stdin

def prob(k,n) :
    if k == 0:
        return n
    elif n == 1 :
        return n
    else :
        return prob(k-1,n) + prob(k,n-1)

test = int(stdin.readline().rstrip())
for i in range(test) :
    k = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    print(prob(k,n))
