# i controlls the number of times the each partition of the snake moves froward before taking a curve
i = 10
def right():
    segment[0].right(90)
    for part in segment[1:]:
        part.forward(i)
        i += 10
        part.right(90)