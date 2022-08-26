from sys import stdin
list = [0]*10
for i in range(10) :
    list[i] = int(stdin.readline()) % 42

list = set(list)
print(len(list))