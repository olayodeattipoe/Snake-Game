import time
from turtle import Turtle, Screen
from snake import Snake
from movement import right
screen = Screen()
screen.screensize(600, 600, "green")
screen.listen()
segment = []
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
for location in COORDINATES:
    new_seg = Snake()
    new_seg.goto(location)
    segment.append(new_seg)


def turn_left():
    i = 10
    segment[0].left(90)
    segment[0].forward(20)
    for part in segment[1:]:
        part.forward(i)
        i += 10
        part.left(90)
        part.forward(i)


while True:
    for partitions in segment:
        partitions.forward(10)
        screen.onkey(turn_left, "a")

# screen.exitonclick()