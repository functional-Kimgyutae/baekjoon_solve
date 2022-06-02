money,user = input().split()
money = int(money)
user = int(user)
pay = money // user
drop = money % user
print(pay)
print(drop)