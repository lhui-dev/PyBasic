# 打开文件
f = open(file='write_info.txt', mode='w',encoding='utf-8')

# 写入内容
f.writelines('i am the writing content.\n')

# 关闭
f.close()