# 字符串的通用操作
str_1 = 'lee'

# 字符串的加法
print(str_1 + ' fuck')

# 字符串的乘法
print(str_1 * 3)

# 获取字符串的长度
print('length is: ', len(str_1))

# 获取字符串中元素的最大最小值： 比较单个字符的Unicode code
print(max(str_1))
print(min(str_1))
print(ord('l'))
print(ord('2'))

# 字符串的遍历
iteraStr = "lee fuck"

# 遍历方式1
for item in iteraStr:
    print(item)
# 遍历方式2
for idx, item in enumerate(iteraStr):
    print(idx, item)
# 遍历方式3
for idx in range(len(iteraStr)):
    print(idx, iteraStr[idx])

# 字符串的类型转换
print(str(12), type(str(12)))  # int ->str
print(str([1, 2, 3, 4]), type(str([1, 2, 3, 4])))  # list ->str
print(str((1,)), type(str((1,))))  # tuple ->str

# 字符串的常用方法
simpleStr = "lee learn python"
# 判断字符串中是否都是小写
print(simpleStr.islower())
# 判断字符串中是否都是大写
print(simpleStr.isupper())
# 判断字符串中是否都是数字
print(simpleStr.isdigit())

# 分割字符串
print(simpleStr.split(' '))

# 分割为两个字符串
print(simpleStr.split(' ', 1))

# 寻找给定字符在字符串中的索引位置
print(simpleStr.find('l'))  # 0

# 字符串连接
print('@'.join(['a', 'b', 'c']))  # a@b@c
