from sys import stdin
num = int(stdin.readline().rstrip())
idx = 0
data = 0
while(num-1 > data):
    idx+= 1
    data = data+idx*6
print(idx+1)
