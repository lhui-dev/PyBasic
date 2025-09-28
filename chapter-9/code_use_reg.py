import re


# 正则表达式


idCard = input('please input your idCard:')
# 前18位数
# 前17位数 最后一位为X？
print(re.match(r'^\d{6}\d{4}\d{7}[\dX]$', idCard))

#  以^开始； 以$结尾
#  \d 数字
#  \w 数字字母下划线
#  \s 空白字符
#  \S 非空白字符
#  . 任意字符
#  [] 区间
#  | 或者
#  {} 精准匹配


