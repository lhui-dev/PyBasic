# 声明变量名并赋值
num = 10

# 元组方式对变量名声明并赋值
name, age = '小米', 22
print("我的名字叫做%s, 我的年龄是%d" % (name, age), end="\n")

# 声明变量
number = 1
print(number)
# 修改变量number的值
number = 10
print(number)

# 声明变量并使用
apple_price = 2.5
new_apple_price = apple_price - 1.2
apple_amount = 5
total_price = new_apple_price * apple_amount
print("🍎单价为%.2f,买了%d斤,总价为：%.2f" % (new_apple_price, apple_amount, total_price))

# 利用type和isinstance可以测试和判断变量的数据类型
print(type(100),type('str'))
print(isinstance(100, int))
print(isinstance('100', int))