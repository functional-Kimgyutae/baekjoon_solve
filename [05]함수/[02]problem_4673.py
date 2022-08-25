l = list(range(1,10000))
def self_num(n) :
    ls = list(map(int,list(str(n))))
    s = n
    for i in ls :
        s+= i
    return s

for i in range(1,10000) :
    re = self_num(i)
    if re < 10000 :
        l[re-1] = -1
for i in l :
    if i != -1 :
        print(i)