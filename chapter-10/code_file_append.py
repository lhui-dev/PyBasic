# 文件内容的追加

# 打开文件
f = open(file='file_append.txt', mode='a', encoding='utf-8')
# 写入内容
f.write('i am the writing content.\n')

# 关闭文件
f.close()
