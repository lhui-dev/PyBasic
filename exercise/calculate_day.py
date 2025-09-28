# 计算给定日期是这一年中的第几天
# 输入格式：2025-09-24
inputDay = input('请输入日期格式（yyyy-MM-dd）：')

# 分割为单个字符
splitDay = inputDay.split('-')

# 获取年月日
splitYear = int(splitDay[0])
splitMonth = int(splitDay[1])
splitDay = int(splitDay[2])
print(splitYear, splitMonth, splitDay)

# 定义每个月多少天：1、3、5、7、8、10、12为31天；其余按照规则；正常为30天
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 判断是否是闰年
if (not splitYear % 4 and splitYear % 100) or (not splitYear % 400):
    # 当前是闰年
    days[2] += 1

result = 0
for i in range(splitMonth):
    result += days[i]
result += splitDay
print('输入的日期 %s 是该年的第 %d 天' % (inputDay, result), end='\n')
