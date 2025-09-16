# 计算和
total = 0
for i in range(101, 10001, 2):
    total += i
print(total)



# 求水仙花数
for i in range(100,1000):
    a = i %10
    c = i // 100 %10
    b = i // 100
    if a*a*a + b*b*b*b + c*c*c == i:
        print(i,"是水仙花数.")
