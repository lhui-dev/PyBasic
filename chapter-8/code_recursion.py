# 走n阶楼梯有多少种方法
def func(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return func(n - 1) + func(n - 2)


print(func(3))