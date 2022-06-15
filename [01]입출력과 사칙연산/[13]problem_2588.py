from sys import stdin
num1 = int(stdin.readline())
num2 =  int(stdin.readline())
h = num2 // 100
m = num2 // 10 - (h*10)
s = num2 - (m*10) - (h*100)

print(num1 * s)
print(num1 * m)
print(num1 * h)
print(num1 * num2)