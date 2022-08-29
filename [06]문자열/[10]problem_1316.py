from sys import stdin
n = int(stdin.readline().rstrip())

for i in range(n) :
    str = list(stdin.readline().rstrip())
    s = set(str)
    s = list(s)
    a = 0
    out = 0
    for char in str :
        if char == s[a] :
            continue;
        elif char == s[++a] :
            continue;
        elif char == s[++a] :
            out += 1
            break;
print(n - out)