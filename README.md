# 尚硅谷python学习笔记

## 简单函数使用

### print函数

- print() 输出/打印指定内容

### 格式化输出

- `%s` 字符串
- `%d` 有符号十进制整数
- `%f` 浮点数
    - `%.2f` 小数点后只显示两位
- `%%` 输出%

### input函数

- 接收控制台输入的内容

- 利用变量接收input函数输入的内容

```python
keyword = input()
```

- 利用变量接收input函数输入的内容，附加提示信息

```python
keyword = input("请输入关键字：")
```

## 变量定义

### 创建变量

- 语法： `变量名 = 变量值`

## 常量声明

大写字母，一般采用下划线方式命名

```python
PROJECT_NAME = "python"
```

### 利用type和isinstance可以测试和判断变量的数据类型

```python
print(type(100), type('str'))
# <class 'int'> <class 'str'>


print(isinstance(100, int))
# True

print(isinstance('100', int))
# False
```

# 切片（同go语言的切片一样）

- 语法：`变量名[起始索引:结束索引:步数]`
- 步数默认为1，可省略不写
- 起始索引默认为0，可以不写
- 结束索引默认为-1，可以不写


- ### 字符串反转

```python
strNumber = '123456789'
print(strNumber[-1:-10:-1])  # 987654321
print(strNumber[::-1])  # 987654321
```

# 简单数据类型转换

- `int(x, [基数])`  将数字或字符串转换为整数，如果x为浮点数，则自动截断小数部分

- `float(x)`  将x转换为浮点数

- `bool(x)` 将x转换为bool类型的True或者False

- `str(x)` 将x转换为字符串

# 组合数据类型

## 序列

> 特点：成员有序排列，并且可以通过下标访问成员。
>
> 包括：列表、range、元组和字符串

### 列表(即其他语言中的数组)

相关操作

- 创建一个列表

```python
# 创建一个空列表
emptyListData = []
emptyList = list()
print(emptyListData)
print(emptyList)
print(type(emptyListData))
print(type(emptyList))
```

- 将字符串转换为列表

```python
transformData = list('123456')  # 类型转换： str-->list
print(transformData)
```

- 计算容器中元素个数

```python
listData = [10, 9, True, 'lee']
print(listData)
length = len(listData)
print(length)
```

- 根据列表的索引访问列表元素

```python
listData = [10, 9, True, 'lee']

# 列表的索引
# 索引从0开始，-1表示从末尾开始
print(listData[-1])
print(listData[0])
```

- 利用切片形式访问列表

```python
listData = [10, 9, True, 'lee']

# 列表的切片
# 切片：左闭右开   start_idx:end_idx:
print(listData[::-1])
print(listData[1:3:1])
```

- 列表的加法运算【类似合并】

```python
# 列表的加法
addListData_1 = [1, 2, 3]
addListData_2 = [4, 5, 6]
print(addListData_1 + addListData_2)
```

- 列表的乘法运算

```python
# 列表的乘法
multiplyListData = ['l', 'e', 'e', 'f', 'u', 'c', 'k']
print(multiplyListData * 2)  # 会被打印两次
```

- 列表的成员运算 ：通过`in` `not in`等关键字判断一个元素是否在列表内

```python
# 列表的成员运算
print('lee' in ['lee', 'fuck'])
print('fuck' not in ['l', 'fuck'])
```

- 列表的比较运算：从第一个元素开始比较，如果可以确定大小关系，则不会比较后续元素了

```python
# 列表比较会从第一个元素开始，如果能确定大小关系（如 1 < 2），就不会再比较后续元素了
print([1, 2, 3] < [2, 3])  # True
print([1, 2, 3] < [-1, -2, 0])  # False
```

内置函数

- 求列表的长度：`len()`

```python
# -- 求列表的长度 len()
listLengthData = [1, 2, 3]
print(len(listLengthData))
```

- 求列表元素的最大值：`max()`

```python
# -- 求列表元素的最大值 max()
listMaxValueData = [1, 2, 3]
print(max(listMaxValueData))
```

- 求列表元素的最小值：`min()`

```python
# -- 求列表元素的最小值 min()
listMinValueData = [1, 2, 3]
print(min(listMinValueData))
```

- 求列表元素的总和：`sum()`

```python
# -- 求列表元素的总和 sum()
sumListData = [1, 2, 3, 4, 5]
print(sum(sumListData))
```

- 删除列表 使用`del`关键字

```python
delListData = [1, 2, 3]
del delListData
```

- 列表的遍历

```python
# 遍历方式1：for循环
iterateListData = [9, 2, 3, 4]
for item in iterateListData:
    print(item)

# 遍历方式2：通过enumerate()函数
for idx, item in enumerate(iterateListData):
    print('idx:', idx, 'item:', item)

# 遍历方式3： 通过for range
for idx in range(len(iterateListData)):
    print('idx:', idx, 'item:', iterateListData[idx])
```

列表的增删改查操作

- pop() 获取列表的末尾元素

```python
crudListData = [1, 2, 3, 4, 5]

lastValue = crudListData.pop()
print(lastValue)  # 5
```

- pop(idx) 返回给定索引处的元素

```python
crudListData = [1, 2, 3, 4, 5]
print(crudListData.pop(0))  # 1
```

- remove(val) 删除列表中第一个出现的给定元素，如果元素值不存在报错

```python
crudListData = [1, 2, 3, 4, 5]
crudListData.remove(2)
print(crudListData)  # [1,3,4,5]
```

- append(val) 向列表末尾添加元素

```python
crudListData = [1, 2, 3, 4, 5]
crudListData.append('6666')
print(crudListData)
```

- insert(idx,val) 在指定索引处插入元素

```python
# insert(idx,val) 在指定索引处插入元素
crudListData = [1, 2, 3, 4, 5]
crudListData.insert(0, '7777')
print(crudListData)
```

- 复制列表元素

```python
crudListData = [1, 2, 3, 4, 5]
copiedCrudListData = crudListData.copy()
```

- count(val) 计算给定元素在列表中出现次数

```python
countListData = [1, 1, 2, 4, 5]
# count(val) 计算给定元素在列表中出现次数
print('occur count: ', countListData.count(1))
```

- extend

```python
oldListValue = [0, 22, 333]
extendValueList = [1, 2]
oldListValue.extend(extendValueList)
print(oldListValue)
```

- reverse() 反转

```python
reverseListData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverseListData.reverse()
print(reverseListData)
```

- clear() 清空列表元素

```python
oldListValue = [0, 22, 333]
oldListValue.clear() 
```

### 元组

- 元组的定义

```python
# 元组的定义
tuple_info = ("lee", 25, '1.75')
print(tuple_info)
print(type(tuple_info))

# 只有一个元素的元组
only_one_element_tuple = (1,)  # 元组里只有一个元素时，加一个逗号

# 空元组 利用tuple()类型转换
empty_tuple = tuple()
empty_tuple_2 = ()
```

- 数据类型转换(x->元组；元组->x)

```python
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
```

- 求元组的长度 `len(tupleVar)`

```python
# 求元组的长度 len()
lengthTupleData = (1, 2)
print(len(lengthTupleData))
```

- 元组的 和 操作 `+`

```python
# 元组的 和 操作
oneTupleData = (1, 2)
anotherTupleData = (3, 4)
print('和操作：', oneTupleData + anotherTupleData)
```

- 求元组中元素的最大值 `max(val)`

```python
# 求元组中元素的最大值 max()
maxValueTupleData = (1, 2, 3, 99)
print(max(maxValueTupleData))
```

- 求元组中元素的最小值 `min(val)`

```python
# 求元组中元素的最小值 min()
minValueTupleData = (1, 2, 3, 99)
print(min(minValueTupleData))
```

- 求元组中元素的和 sum()

```python
sumTupleData = (1, 2, 3, 4, 5, 6, 7)
print(sum(sumTupleData))
```

- 根据索引下标访问元组中元素

```python
idxTupleData = (66, 88, 99)
print(idxTupleData[-1])  # 最后一个元素
print(idxTupleData[0])  # 第一个元素
```

- 切片方式访问元组中元素

```python
# 切片方式访问元组中元素
sliceTupleData = (1, 2, 3, 4, 5, 6, 7)
print(sliceTupleData[::-1])
print(sliceTupleData[1:5:2])
```

元组的常用操作

```python
crudTupleData = (1, 2, 3, 4, 5)

# count(val) 统计给定元素在元组中出现的次数
print('count: ', crudTupleData.count(1))

# index(idx) 返回元组中给定索引处的元素
print('the element at idx 2 is :', crudTupleData.index(2))
```

元组的遍历

```python
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
```

### range

> range是系统提供的内建函数。range序列属于不可变序列，不支持元素修改操作，不支持+和*操作。
>
> range一般用于for-in遍历

range生成一个等差序列`[start,end)`

- 语法：`range(start,end,[step=1])`

### 字典

> - 字典使用`{}`定义。
> - 字典使用键值对存储数据，键值对之间使用逗号分割
> - 键key是索引
> - 值value是数据
> - 键和值之间使用`:`分隔
> - 键是唯一的
> - 值可以取任何数据类型
> - 键只能使用 `字符串`，`数字`或者`元组`

### 集合

- 集合的创建

```python
# 集合的创建
empty_set = set()
print(empty_set, type(empty_set))

# 创建一个带元素的集合
int_values_set = set(range(1, 10))
print(int_values_set, type(int_values_set))

# 集合内的元素有序，且不重复
common_values_set = {'l', 'e', 'e', 'f', 'u', 'c'}
common_values_set.remove('l')
print(common_values_set)

# 添加单个元素
common_values_set.add('k')
print(common_values_set)

# 更新集合信息
common_values_set.update(['h', 'e', 'a', 'd', 'x', 'p'])
print(common_values_set)

```

- 求两个集合的交集和并集

```python
# 求两个集合的交集和并集
set_value_1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
set_value_2 = {'a', 'b', 'c', 'd', 'e', 'g', 'h'}
# 求并集
print(set_value_1 | set_value_2)
# 求交集
print(set_value_1 & set_value_2)
```

- 统计每个分数的人数

```python
score_list = [60, 70, 80, 70, 90, 60]
score_value_set = set(score_list)
dict_value = {}

# 统计每个分数的人数
for score in score_value_set:
    t = score_list.count(score)
    dict_value[score] = t
# 遍历内容
for k, v in dict_value.items():
    print(k, v)
```

### 可变与不可变类型

#### 不可变类型

- 数字（int、float、complex）
- 字符串（str）
- 元组（tuple）
- 布尔类型（bool）

#### 可变类型

- 列表（list）
- 字典（dict）
- 集合（set）