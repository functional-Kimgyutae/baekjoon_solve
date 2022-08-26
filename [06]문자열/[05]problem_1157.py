from sys import stdin
str = stdin.readline().rstrip().upper()
se = list(set(str))
cn = []
for i in se :
    cn.append(str.count(i))
if cn.count(max(cn)) >= 2:
    print("?")
else :
    print(se[cn.index(max(cn))])