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

# 求两个集合的交集和并集
set_value_1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
set_value_2 = {'a', 'b', 'c', 'd', 'e', 'g', 'h'}
# 求并集
print(set_value_1 | set_value_2)
# 求交集
print(set_value_1 & set_value_2)

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
