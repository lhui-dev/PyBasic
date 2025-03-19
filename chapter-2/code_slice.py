"""
  切片sequence
  语法：   sequence[start:stop:step]
  - sequence 要切片的序列
  - start 切片开始的索引（包含），默认为0，可以省略
  - stop 切片结束的索引（不包含），默认为切片序列的长度，可以不写
  - step 切片中元素之间的步长，默认为1，可以不写
"""

# 切片类型
slice_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(slice_var))  # <class 'list'>

# 数据列表
element_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 获取前五个元素
print(element_list[0:5])  # [0, 1, 2, 3, 4]
# 获取索引3到7的元素
print(element_list[2:8])  # [2, 3, 4, 5, 6, 7]
# 获取开头到索引7的元素
print(element_list[:7])  # [0, 1, 2, 3, 4, 5, 6]
# 获取所有偶数索引的元素
print(element_list[::2])  # [0, 2, 4, 6, 8]
# 获取所有奇数索引的元素
print(element_list[1::2])  # [1, 3, 5, 7, 9]
# 反转列表
print(element_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
