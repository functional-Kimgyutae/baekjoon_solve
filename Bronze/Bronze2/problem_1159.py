import readline
from sys import stdin
n = int(stdin.readline())
dic = {
    'a':0,'b':0,'c':0,'d':0,
    'e':0,'f':0,'g':0,'h':0,
    'i':0,'j':0,'k':0,'l':0,
    'm':0,'n':0,'o':0,'p':0,
    'q':0,'r':0,'s':0,'t':0,
    'u':0,'v':0,'w':0,'x':0,
    'y':0,'z':0}
lis = []
for i in range(n) :
    name = stdin.readline()[0:1] 
    dic[name]+=1
    if dic[name] == 5 :
        lis.append(name)
if not lis :
    print("PREDAJA")
else :
    lis.sort()
    str = ""
    for i in range(len(lis)) :
        str+=lis[i]
    print(str)
