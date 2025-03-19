n = 7
a = 2
flag = 0
while a<n:
    if n%a==0:
        print(n,'不是质数')
        flag = 1
        break
    a+=1
if flag ==0:
    print(n,'是质数')