x = 10
match  x:
    case 10:
        print('10')
    case 20:
        print('20')
    case _: # 匹配所有其他值
        print('other value')