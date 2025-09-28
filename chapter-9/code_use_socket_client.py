import socket

# 创建一个socket对象
sk = socket.socket()

# 连接服务器
sk.connect(("127.0.0.1", 8994))

while True:
    data = input('input data: ')
    # 发送数据
    sk.send(data.encode('utf-8'))
    # 等待服务器响应数据
    accept_data = sk.recv(1024)
    # 打印服务器的响应
    print('接收到服务器的响应：',accept_data.decode('utf-8'))
