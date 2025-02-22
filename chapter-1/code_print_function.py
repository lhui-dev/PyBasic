# 打印遍历
a = 10
print(a)

# 在一行中打印多个内容，可以在print函数中使用英文逗号隔开
print("hello", '2025', sep=",")
print(1, 2, 3, 4)

# sep：设置多个打印内容的分隔符
# 将默认的空格分隔符变为*号
print("hello", '2025', sep="*")

print("\n")

# 输出换行
print(end='\n')

print("yes,yes", "you are right", sep=" ", end='\n')
print()

"""
格式化输出
"""
year = 2025
month = 2
day = 22
weak = "——"
weather = "阴"
temperature = 26.5
print("今天是%d年%.2d月%d日,天气%s,温度%.1f度" % (year, month, day, weather, temperature), end="\n")
