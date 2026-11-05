from turtle import *

tracer(0)
screensize(10000, 10000)
r = 25

lt(90)

for _ in range(4):
    fd(10 * r)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')

update()
done()