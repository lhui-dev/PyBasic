# lambda匿名函数
func = lambda a, b: a + b
print(func(1, 2))

list_data = [1, 2, 3]
# map 映射
result = map(lambda x: x ** 3, list_data)  # 映射
print(list(result))

# reduce 累积
from functools import reduce

result = reduce(lambda x, y: x * y, list_data)
print(result)

# filter 过滤
# 过滤全部偶数
list_filter_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2, list_filter_data)
print(list(result))
