import os

# 打开文件
# f = open('demo.txt', 'r')  # 相对路径

path = os.getcwd()
f = open(file=path + '/demo.txt', mode='r')  # 绝对路径

# 读取文件
content = f.read()
print('content:', content)
# 关闭文件
f.close()
