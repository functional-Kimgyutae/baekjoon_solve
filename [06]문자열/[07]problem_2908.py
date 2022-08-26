from sys import stdin
a,b =stdin.readline().rstrip().split()
a,b = list(a),list(b)
a.reverse()
b.reverse()
a,b = "".join(a),"".join(b)
a,b = int(a),int(b)
print(a if a>b else b)