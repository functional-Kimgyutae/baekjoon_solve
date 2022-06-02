import math
D,H,W = input().split()
D = int(D)
H = int(H)
W = int(W)

inc = (D*D)/(H*H+W*W)
inc = math.sqrt(inc)
print(math.floor(inc*H))
print(math.floor(inc*W))