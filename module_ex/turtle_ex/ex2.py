# 간단한 사각형 그리기
import turtle

t = turtle.Turtle()

# 픽셀수, 오른쪽 회전
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# 그래픽 그려지고 난 후 윈도우 닫을 때까지 대기
turtle.done()

