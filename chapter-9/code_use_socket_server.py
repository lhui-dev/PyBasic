import socket

# 创建一个socket对象
sk = socket.socket()

# 绑定ip和端口号
sk.bind(("127.0.0.1", 8994))

# 设置监听
sk.listen(2)

# 等待客户端连接
conn, addr = sk.accept()

print(conn, addr)

while True:
    accept_data = conn.recv(1024)
    print('收到客户端发送的消息：', accept_data.decode('utf-8'))
    # 发生服务器的响应
    send_data = 'ok'
    conn.send(send_data.encode('utf-8'))
