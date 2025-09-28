def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def listPowTotal(listParam):
    """
     参数list：列表

     :return list列表中每个元素的平方和
    """
    result = 0
    for item in listParam:
        result = result + item ** 2
    return result


author = 'lee'
