from random import randint, random,choice

# 生成0-1之间的小数
print(random())

# 生成1-100之间的随机整数
random_number = randint(1, 100)
print(random_number)



# 随机获取列表中的某个元素
random_list_data = [1,3,5,7,9,11]
random_dta = random_list_data[randint(0, len(random_list_data) - 1)]
print(random_dta)

# 利用random中工具包获取
print(choice(random_list_data))


# 生成一个随机字符组成的列表
result = []
count = 5
listOfElementsCount = 20
for idx in range(listOfElementsCount):
    str = ''
    for j in range(count):
        t = randint(ord('a'), ord('z'))
        str += chr(t)
    result.append(str)
print(result)


def generate_random_char(upper = True):
    if upper:
        return chr(randint(ord('A'), ord('Z')))
    else:
        return chr(randint(ord('a'), ord('z')))

def generate_random_string(length):
    s = ''
    for i in range(length):
        s += generate_random_char(choice([True, False]))
    return s


# 生成随机位数的验证码
def generate_random_capter(length):
    return generate_random_string(length)


print(generate_random_capter(5))