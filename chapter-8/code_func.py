# 声明函数
def func():
    print('i am a simple function')


# 调用函数
func()


# 默认参数
def calculateSum(num1=0, num2=0):
    return num1 + num2


print(calculateSum(num1=1, num2=2))


# 可变参数
def varParamFunc(*args):  # 可变参数: 接收参数后转换为元组
    print('varParamFunc: ', args)


varParamFunc('1')
varParamFunc('a', 'b', 'c')

# 传递列表类型参数
list_data = [1, 2, 3]
#  传递的实参类型为 列表 类型时：需要在前面加一个*
varParamFunc(*list_data)


# 可变参数：接收字典
def varParamFunc2(**kwargs):  # 可变参数：接收字典
    print('varParamFunc2: ', kwargs)
    for k, v in kwargs.items():
        print(k, '=', v)


dict_1 = {'name': 'xiao', 'age': 20}
# 传递实参类型为 字典 时：也需要加两个*
varParamFunc2(**dict_1)




