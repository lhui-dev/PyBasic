# 字符串

# 单引号字符串
str_single = 'single'
print(str_single)

# 声明空字符串
empty_string_1 = ''
print(empty_string_1)
empty_string_2 = str()
print(empty_string_2)

# 双引号字符串
double_quoted_string = "double quoted string"
print(double_quoted_string)

# 三引号字符串
# 多行字符串
triple_quoted_string = """triple
 quoted string"""
print(triple_quoted_string)

# 字符串乘法
print('♥' * 10)

complex_str = "hello,world"
# 根据索引获取字符串内容
# 索引从0开始
# complex_str[0]表示从第一个元素
# complex_str[-1]表示从字符串末尾开始数，即倒着数第几个
print(complex_str[0], complex_str[-1])  # h d
# 从第一个到最后一个位置之前的值（最后一个不算）
# 切片写法,【包头不包尾】
print(complex_str[0:-1])  # hello,worl
print(complex_str[6:-2])  # wor
print(complex_str[:])  # hello,world
print(complex_str[0:-1:2])  # hlowr

# 字符串反转
strNumber = '123456789'
print(strNumber[-1:-10:-1]) # 987654321
print(strNumber[::-1]) # 987654321
