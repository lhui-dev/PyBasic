
import turtle

# 获取画笔
pen = turtle.Pen()
pen.speed(0)
# 画直线
for i in range(100):
    pen.forward(100 + i)
    pen.right(65)
input()