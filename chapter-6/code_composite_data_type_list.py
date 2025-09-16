# 创建一个空列表
emptyListData = []
emptyList = list()
print(emptyListData)
print(emptyList)
print(type(emptyListData))
print(type(emptyList))

# 将字符串转换为列表
transformData = list('123456')  # 类型转换： str-->list
print(transformData)

listData = [10, 9, True, 'lee']
print(listData)
# 计算容器中元素个数
length = len(listData)
print(length)

# 列表的索引
# 索引从0开始，-1表示从末尾开始
print(listData[-1])
print(listData[0])

# 列表的切片
# 切片：左闭右开   start_idx:end_idx:
print(listData[::-1])
print(listData[1:3:1])

# 列表的加法
addListData_1 = [1, 2, 3]
addListData_2 = [4, 5, 6]
print(addListData_1 + addListData_2)

# 列表的乘法
multiplyListData = ['l', 'e', 'e', 'f', 'u', 'c', 'k']
print(multiplyListData * 2)

# 列表的成员运算
print('lee' in ['lee', 'fuck'])
print('fuck' not in ['l', 'fuck'])

# 列表比较会从第一个元素开始，如果能确定大小关系（如 1 < 2），就不会再比较后续元素了
print([1, 2, 3] < [2, 3])
print([1, 2, 3] < [-1, -2, 0])


# 内置函数

# -- 求列表的长度 len()
listLengthData = [1, 2, 3]
print(len(listLengthData))

# -- 求列表元素的最大值 max()
listMaxValueData = [1, 2, 3]
print(max(listMaxValueData))

# -- 求列表元素的最小值 min()
listMinValueData = [1, 2, 3]
print(min(listMinValueData))

# -- 求列表元素的总和 sum()
sumListData = [1, 2, 3, 4, 5]
print(sum(sumListData))



# -- 删除列表 --> 使用del关键字
delListData = [1, 2, 3]
del delListData

print('-' * 10)

# 列表的遍历
iterateListData = [9, 2, 3,4]
for item in iterateListData:
    print(item)
#
for idx, item in enumerate(iterateListData):
    print('idx:' , idx, 'item:', item)

for idx in range(len(iterateListData)):
    print('idx:' , idx, 'item:', iterateListData[idx])


# 列表的增删改查等操作
crudListData = [1, 2, 3, 4, 5]

# pop() 获取列表的末尾元素
lastValue = crudListData.pop()
print(lastValue)

# pop(idx) 返回给定索引处的元素
print(crudListData.pop(0))

# remove(val) 删除列表中第一个出现的给定元素，如果元素值不存在报错
crudListData.remove(2)
print(crudListData)

# append(val) 向列表末尾添加元素
crudListData.append('6666')
print(crudListData)

# insert(idx,val) 在指定索引处插入元素
crudListData.insert(0, '7777')
print(crudListData)

# 复制列表元素
copiedCrudListData = crudListData.copy()
# print(copiedCrudListData)

countListData = [1, 1, 2, 4, 5]
# count(val) 计算给定元素在列表中出现次数
print('occur count: ',countListData.count(1))

oldListValue = [0,22,333]
extendValueList = [1,2]
oldListValue.extend(extendValueList)
print(oldListValue)


# clear() 清空列表元素
oldListValue.clear()

reverseListData = [1, 2, 3, 4, 5,6,7,8,9,10]
reverseListData.reverse()
print(reverseListData)