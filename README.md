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