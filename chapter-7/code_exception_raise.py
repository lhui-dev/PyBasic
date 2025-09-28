# raise语法

try:
    pwd = input('please input your pwd: ')
    if pwd == '' or len(pwd) < 8:
        # 主动抛出异常
        raise Exception('please enter at least 8 characters.')
except Exception as e:
    print(e)
