from turtle import *

tracer(0)
screensize(10000, 10000)
r = 25

def сместиться(a, b):
    goto(xcor() + a * r, ycor() + b * r)

def в_точку(x, y):
    goto(x * r, y * r)

for _ in range(10):
    сместиться(3, 6)
    сместиться(7, -2)
    сместиться(-10, -4)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')

update()
done()