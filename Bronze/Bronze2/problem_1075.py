from sys import stdin
import math
n = int(stdin.readline())
f = int(stdin.readline())

x = (n//100)*100 #10의자리 지우기
d = math.ceil(x/f) #x보다 큰 수중 가장 몪이 작은거 구하기
x = (d*f)-x

if x < 10 :
    print("0"+str(x))
else :
    print(x)
 


