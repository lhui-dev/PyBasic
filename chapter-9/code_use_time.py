
import time

print(time.time()) # 返回时间戳
print(time.localtime())


def get_current_time(pattern = '%Y-%m-%d %H:%M:%S'):
    return time.strftime(pattern, time.localtime())