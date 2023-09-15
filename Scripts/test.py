from main import segment
from turtle import Screen
screen = Screen()
screen.listen()

def turn_left():
    segment[0].left(90)
    segment[0].forward(50)
    segment[1].forward(10)
    segment[1].left(90)
    segment[1].forward(10)
    segment[2].forward(20)
    segment[2].left(90)

while True:
    for partitions in segment:
        screen.onkey(turn_left, "a")
    break