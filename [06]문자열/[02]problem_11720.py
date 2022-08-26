from sys import stdin
a = stdin.readline()
li = list(map(int,list(stdin.readline().rstrip())))
num = 0
for i in li :
    num+= i
print(num)