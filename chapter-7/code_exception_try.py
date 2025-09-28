# try


try:
    # 除数异常
    1 / 0
except ZeroDivisionError as e:
    print(e)  # division by zero
else:
    print('运行没有被except语句捕获，执行else模块....')
finally:
    print('finally.....')
