# 字典是无序的对象集合


# 定义一个空字典
emptyDictionary = {}
emptyDictionary_ = dict()

# 创建字典
userDictionary = {
    'firstName': 'John',
    'lastName': 'Doe',
    'email': 'lee@gmai.com',
}
print(userDictionary, type(userDictionary))

# 在字典中新增键值对
userDictionary['gender'] = 'male'
print(userDictionary)
# 根据 键 获取对应的值
print(userDictionary['gender'])

# 修改键值对
userDictionary['gender'] = 'female'
print(userDictionary)

# 字典的遍历
print(userDictionary.items())

#  获取key和value
for key, value in userDictionary.items():
    print('key: ', key, ' value: ', value)

# 获取所有的key
for key in userDictionary.keys():
    print('key: ', key, ' value: ', userDictionary[key])

# 获取所有的value
for value in userDictionary.values():
    print('value: ', value)
