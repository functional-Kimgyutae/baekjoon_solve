from sys import stdin
str = stdin.readline().rstrip()
sum = 0
li = ["dz=","c=","c-","d-","lj","nj","s=","z="];
for i in range(len(li)) :
    if li[i] in str :
        str = str.replace(li[i],"!")
print(len(str))