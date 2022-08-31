from sys import stdin
import math
A,B,V = stdin.readline().rstrip().split()
A,B,V = int(A),int(B),int(V)
if A == V :
    print(1)
else :
    print(int(math.ceil((V-A)/(A-B)+1)))
