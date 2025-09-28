# with 无需自己关闭打开的文件
with open(file="file_with_test.txt", mode="r", encoding="utf-8") as f:
    content = f.read()
    print(content)