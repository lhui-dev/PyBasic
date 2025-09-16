# 元组内的元素不能修改

# 元组的定义
tuple_info = ("lee", 25, '1.75')
print(tuple_info)
print(type(tuple_info))

# 只有一个元素的元组
only_one_element_tuple = (1,)  # 元组里只有一个元素时，加一个逗号

# 空元组 利用tuple()类型转换
empty_tuple = tuple()
empty_tuple_2 = ()

# 将一个字符串转换为一个元组
strRaw = 'hello'
str_tuple = tuple(strRaw)
print(str_tuple)

# 将一个列表转换为元组
listRaw = ['fuck', 'jwy']
list_tuple = tuple(listRaw)
print(list_tuple)

# 将一个元组转换为列表
tupleRaw = ('f', 'u', 'c', 'k')
tuple_2_list = list(tupleRaw)
print(tuple_2_list)

# 将一个元组转换为字符串
tuple_ss = (2, 'b')
str_2_tuple = str(tuple_ss)
print(str_2_tuple, type(str_2_tuple))

# 求元组的长度 len()
lengthTupleData = (1, 2)
print(len(lengthTupleData))

# 元组的 和 操作
oneTupleData = (1, 2)
anotherTupleData = (3, 4)
print('和操作：', oneTupleData + anotherTupleData)

# 求元组中元素的最大值 max()
maxValueTupleData = (1, 2, 3, 99)
print(max(maxValueTupleData))

# 求元组中元素的最小值 min()
minValueTupleData = (-1, 2, 3, 99)
print(min(minValueTupleData))

# 求元组中元素的和 sum()
sumTupleData = (1, 2, 3, 4, 5, 6, 7)
print(sum(sumTupleData))

# 根据索引下标访问元组中元素
idxTupleData = (66, 88, 99)
print(idxTupleData[-1])  # 最后一个元素
print(idxTupleData[0])  # 第一个元素

# 切片方式访问元组中元素
sliceTupleData = (1, 2, 3, 4, 5, 6, 7)
print(sliceTupleData[::-1])
print(sliceTupleData[1:5:2])

# 元组的常用操作
crudTupleData = (1, 2, 3, 4, 5)

# count(val) 统计给定元素在元组中出现的次数
print('count: ', crudTupleData.count(1))

# index(idx) 返回元组中给定索引处的元素
print('the element at idx 2 is :', crudTupleData.index(2))

#  元组的遍历
iterateTupleData = (1, 2, 3, 4, 5, 6, 7)

# 遍历方式1
for item in iterateTupleData:
    print(item)

# 遍历方式2
for idx, index in enumerate(iterateTupleData):
    print("idx: ", idx, " index: ", index)

# 遍历方式3
for idx in range(len(iterateTupleData)):
    print("idx: ", idx, " iterateTupleData[idx]: ", iterateTupleData[idx])
