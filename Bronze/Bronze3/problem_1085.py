x,y,w,h = map(int,input().split())

list = [x,y,abs(w-x),abs(h-y)]
print(min(list))