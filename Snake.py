from random import *
from turtle import *
from base import *


speed = 10
food = vector(0, 0)
snake = [vector(10, 10)]
aim = vector(0, -speed)


def change(x, y):
    aim.x = x
    aim.y = y


def inside(head):
    return head.x<240 and head.x>-240 and head.y>-240 and head.y<240


def move():
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        for i in snake:
            square(i.x,i.y,10,"red")
        return
    snake.append(head)
    if head == food:
        food.x = randrange(-200,200,10)
        food.y = randrange(-200,200,10)
        update()
    else:
        snake.pop(0)
    clear()
    for body in snake:
        square(body.x,body.y,10,"blue")
    square(food.x,food.y,10,"orange") 
    ontimer(move,100)


setup(500, 500, None,None)
ht()
tracer(False)
listen()
onkey(lambda: change(speed, 0), "Right")
onkey(lambda: change(-speed, 0), "Left")
onkey(lambda: change(0, speed), "Up")
onkey(lambda: change(0, -speed), "Down")
move()
done()
